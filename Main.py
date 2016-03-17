from Interface import LEDcontrols
from dbConnection import DBConnection
from gpsHandler import GPSHandler
from car import Car
from jsonParser import JsonParser
import sqlite3
import time
import sys




def main():
    try:
        #Kobler til database
        connection = DBConnection()
        connection.connectToDB()

        ledKontroll = LEDcontrols.LEDcontrols()
        ledKontroll.setUpLeds(ledKontroll.leds)
        ledKontroll.safe(True)


        #Henter data fra database slik at den kan lagres på lokal database(SQLite)
        cache = connection.getResultSet("SELECT Latitude,Longitude FROM Coordinates")

        #Oppretter et GPSHandler objekt som finner avstand fra bil til farlig veistrekke
        handler = GPSHandler()
        handler.setConnection(connection)

        #Objekt med testdata
        car = Car()

        #Går gjennom testdata når koblet til database
        while(car.next()):
            if(car.tripCounter % 50 == 0):
                print(car.tripCounter)
                carSpeed = car.speed[0]
                if(carSpeed > 5):
                    #Finner om det er innkommende farlig veistrekke
                    gpsState = handler.compareCoordinates(car.lat[0], car.long[0])
                    if (gpsState[0] == 'A'):
                        print("DANGER")
                        ledKontroll.dangerMode(True)
                    elif(gpsState[0] == 'C'):
                        print("Warning")
                        ledKontroll.warningMode()
                    elif(gpsState[0] == 'N'):
                        print("Carry on")
                        ledKontroll.safe(True)


    except:
        print("Kunne ikke koble til database")
        #ledKontroll = LEDcontrols
        #ledKontroll.setUpLeds()
        #ledKontroll.safeMode()









    connection.closeConnection()



main()
