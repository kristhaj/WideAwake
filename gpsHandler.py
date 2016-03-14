import dbConnection
from geopy.distance import vincenty

class GPSHandler:
    connection = None

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
            minLat, maxLat = self.getBetween(carLat)
            minLong, maxLong = self.getBetween(carLong)
            query = ("SELECT Latitude, Longitude FROM Coordinates WHERE (carLat BETWEEN minLat AND maxLat) AND (carLong BETWEEN minLong AND maxLong)")
            resultSet = self.connection.getResultset(query)
            self.validateCoordinates(carLat,carLong,resultSet)
        except Exception as e:
            return None

    def validateCoordinates(self, carLat, carLong, resultSet):
        '''
        This validates the car distance difference in km and/or meters against the coordinates in the resultset.

        :carPos: Car position (lat,long)
        :distKm: Distance in km between car pos, and coordinate in resultSet
        :distM: Distance in m between car pos, and coordinate in resultSet
        :param carLat: The car latitude coordinate
        :param carLong: The car longitude coordinate
        :param resultSet: The resultset containing the coordinates to compare the cars given coordiantes against.
        :return 'C' =< 100m < 'A' < 1km < 'N']:
        '''
        carPos = (carLat, carLong)
        #check if car coordinates is close to the resultSet (slippery Coordinates)
        for (lat, long) in resultSet:
            distKM = vincenty(carPos, (lat,long)).km
            if(distKM < 1):
                #calculates new distance to slippery path
                distM = vincenty(carPos, (lat,long)).meters
                if(distM <= 100):
                    return 'C',(lat,long) #C for close
                else:
                    return 'A',(lat,long) #A for approaching

        #If not stopped by now, by one of the returns. That means that nearby coordinates are not slippery
        return 'N',None #N for none


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
        maxNumber = round((coordinate + float(number)),precision)
        minNumber = round((coordinate - float(number),precision))
        return minNumber,maxNumber


def main():
    con = dbConnection
    con.getConnection()
    handler = GPSHandler()
    handler.setConnection(con)

#main()

