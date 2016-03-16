import dbConnection
from geopy.distance import vincenty

class GPSHandler:
    '''
    This class takes in the cars positions, database connection and car speed. Then calculates nearby coordinates, makes a SQL query
    compares cars position against coordinates in resultset fram db. returns tuples (comparison, nearby coordinates, eta)
    '''
    def __init__(self):
        '''
        Sets the class variables static.
        :return:  Nothing
        '''
        self.connection = None

    def setConnection(self,dbConnection):
        """
        This sets the already established database connection, to a variable, which the gps handler
        then can use, to compare the cars coordinates against coordiantes in the database.

        :param dbConnection: Already established database connection
        :connection: variable to conntain the connection
        :return: True if established database connection is set to variable connection, returns False else.
        """
        try:
            self.connection = dbConnection
            return True
        except:
            return False


    def compareCoordinates(self, carLat,carLong):
        '''
        This takes in the car's coordiantes, calculates the minimum and maximum distance coordinates from the car to comapre to.
        creates a SQL query S-F-W statement. Executes the query, and saves the result set. Then checks car position in distance
        aginst the coordinates in the resultset

        :param carLat: Car latitude coordinate
        :param carLong: Car longitude coordinate
        :minLat: The calculated minimum distance difference between car and database coordinates
        :maxLat: The calculated maximum distance difference between car and database coordinates
        :resultSet: The resultset from the query
        :query: SQL-query that uses the min and max values in the where clause.
        :return 'C' =< 100m < 'A' < 1km < 'N']:
        '''
        try:
            lat = self.getBetween(carLat)
            long = self.getBetween(carLong)
            query = ("SELECT Latitude, Longitude FROM Coordinates WHERE ("+str(carLat)+" BETWEEN "+str(lat[0])+" AND "+str(lat[1])+") AND ("+str(carLong)+" BETWEEN "+str(long[0])+" AND "+str(long[1])+")")
            resultSet = self.connection.getResultSet(query)
            return self.validateCoordinates(carLat,carLong,resultSet,None)
        except Exception as e:
            return "compare: " +str(e)

    def validateCoordinates(self, carLat, carLong, resultSet, carSpeed):
        '''
        This validates the car distance difference in km and/or meters against the coordinates in the resultset.

        :carPos: Car position (lat,long)
        :distKm: Distance in km between car pos, and coordinate in resultSet
        :distM: Distance in m between car pos, and coordinate in resultSet
        :param carLat: The car latitude coordinate
        :param carLong: The car longitude coordinate
        :param resultSet: The resultset containing the coordinates to compare the cars given coordiantes against.
        :return 'C' =< 100m < 'A' < 1km < 'N', SlipperyCoordinates, time:
        '''
        carPos = (carLat, carLong)
        #check if car coordinates is close to the resultSet (slippery Coordinates)
        for tup in resultSet:
            distKM = vincenty(carPos, tup).km
            if(distKM < 1):
                #calculates new distance to slippery path
                distM = vincenty(carPos, tup).meters
                if(carSpeed != None):
                    time = (distKM/carSpeed*1.6)*60
                else:
                    time = None

                if(distM <= 100):
                    return 'C', tup, time #C for close
                else:
                    return 'A', tup, time #A for approaching

        #If not stopped by now, by one of the returns. That means that nearby coordinates are not slippery
        return ('N', None) #N for none


    def getBetween(self, coordinate):
        """
        This calculates the allowed difference between the car coordinates, and the coordinates in the database
        Takes in car coordinates, then calculates the precision on the coordinates, and maintains that precision but adds
        two to the least significant number.

        :param coordinate: car position (lat || long) ex. 10.123456
        :precision: Finds the precision of the coordinates
        :number: Addes 2 to the least significant number in the coordinates
        :maxNumber: Adds the precision number to the car coordinates
        :minNumber: Subtracts the precision number from the car coordinates
        :return: minNumber(car coordinates - two on least significant number),maxNumber (car coordinates + two on least significant number)
        """
        precision = len(str(coordinate).split(".")[1])
        number = "0."+'0'*(precision-2)+"2"
        maxNumber = (coordinate + float(number))
        minNumber = (coordinate - float(number))
        return (minNumber, maxNumber)


def main():
    print("start")
    con = dbConnection.DBConnection()
    print("con should be object now")
    con.getConnection()
    print("con should have connection")
    handler = GPSHandler()
    print("created handler")
    state = handler.setConnection(con)
    print("handler set connection " + str(state))
    luck = handler.compareCoordinates(40.768967,-73.993202) #Car pos that should match 'C' with coordinates in database.
    print("handler compared coordinates")
    print(luck)
    print(luck[0])
    print("Shall now try and print resultset")
    print(con.getResultSet(query = ("SELECT Latitude, Longitude FROM Coordinates")))


#main()

