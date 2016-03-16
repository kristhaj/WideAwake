#from Interface import LEDcontrols
from dbConnection import DBConnection
from gpsHandler import GPSHandler
from car import Car
from jsonParser import JsonParser
import time
import sys




def main():
    try:
        connection = DBConnection()
        connection.connectToDB()
        cache = connection.getResultSet("SELECT Latitude,Longitude FROM Coordinates")
        handler = GPSHandler()

        #car = Car()
        #car.setTrip(parser.getPath(),parser.getWantedAttributes())
        #while(car.next()):
         #   print(car.long)



    except:
        print("Kunne ikke koble til database")

   # while(connection):
    #    print("hei")

    print(cache)
    connection.closeConnection()
    parser = JsonParser()
    car = Car(parser.getPath(),parser.getWantedAttributes())

main()
