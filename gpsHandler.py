print("start")
import dbConnectionTest
from geopy.distance import vincenty
print("end")




def setConnection(dbConnection):
    global connection
    try:
        connection = dbConnection
        return True
    except:
        return False


def compareCoordinates(carLat,carLong):
    try:
        #find out what 'square'- to put in the where clause in SQL query.
        minLat, maxLat = getBetween(carLat)
        minLong, maxLong = getBetween(carLong)
        query = ("SELECT Latitude, Longitude FROM Coordinates WHERE ")
        resultSet = connection.getResultset(query)
        validateCoordinates(carLat,carLong,resultSet)
    except Exception as e:
        return None

def validateCoordinates(carLat, carLong, resultSet):
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


def getBetween(coordinate):
    precision = len(str(coordinate).split(".")[1])
    number = "0."+'0'*(precision-2)+"2"
    maxNumber = round((coordinate + float(number)),precision)
    minNumber = round((coordinate - float(number),precision))
    return minNumber,maxNumber


def main():
    con = dbConnectionTest
    con.getConnection()
    setConnection(con)

main()

