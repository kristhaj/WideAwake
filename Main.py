#from Interface import LEDcontrols
from dbConnection import DBConnection
from sqlLiteHandler import SQLLite
from gpsHandler import GPSHandler
from car import Car
from offlineMode import OfflineMode
from jsonParser import JsonParser
import sqlite3
import time
import sys




def main():
    try:
        #Kobler til database
        connection = DBConnection()
        connection.connectToDB()

        #Oppretter et ledkontroll objekt
        #ledKontroll = LEDcontrols.LEDcontrols()
        #ledKontroll.setUpLeds(ledKontroll.leds)
        #ledKontroll.safe(True)


        #Henter data fra database slik at den kan lagres på lokal database(SQLite)
        cache = connection.getResultSet("SELECT Latitude,Longitude FROM Coordinates")

        #Laster opp nyeste versjon av database til lokal "database"
        localdbConnection = SQLLite("Resources/WideAwakeCoordinates.db")
        localdbConnection.establishConnection()
        #localdbConnection.updateLocalDatabase(cache)
        localdbConnection.closeConnection()

        #Oppretter et GPSHandler objekt som finner avstand fra bil til farlig veistrekke
        handler = GPSHandler()
        handler.setConnection(connection)

        #Objekt med testdata
        car = Car()

        #Går gjennom testdata når koblet til database
        while(car.next()):
            if(car.tripCounter % 50 == 0):
                carSpeed = car.speed[0]
                if(carSpeed > 5):
                    #Finner om det er innkommende farlig veistrekke
                    gpsState = handler.compareCoordinates(car.lat[0], car.long[0])
                    if (gpsState[0] == 'A'):
                        print("DANGER")
         #               ledKontroll.dangerMode(True)
                    elif(gpsState[0] == 'C'):
                        print("Warning")
          #              ledKontroll.warningMode()
                    elif(gpsState[0] == 'N'):
                        print("Carry on")
           #             ledKontroll.safe(True)


    except:
        print("Kunne ikke koble til database")
        #Oppretter testobjekt
        offlineCar = Car()

        #Kobler til lokal database
        offlineConnection = SQLLite("Resources/WideAwakeCoordinates.db")
        offlineConnection.establishConnection()

        #Oppretter et GPSHandler objekt som finner avstand fra bil til farlig veistrekke
        offlineHandler = GPSHandler()
        print("Funker det?")
        offlineHandler.setConnection(offlineConnection)
        print("oh'yes")

        #Går gjennom testdata når koblet til lokal database
        while(offlineCar.next()):
            if(offlineCar.tripCounter % 50 == 0):
                carSpeed = offlineCar.speed[0]
                if(carSpeed > 5):
                    #Finner om det er innkommende farlig veistrekke
                    gpsState = offlineHandler.offlineCompareCoordinates(offlineCar.lat[0], offlineCar.long[0])
                    if (gpsState[0] == 'A'):
                        print("DANGER")
         #               ledKontroll.dangerMode(True)
                    elif(gpsState[0] == 'C'):
                        print("Warning")
          #              ledKontroll.warningMode()
                    elif(gpsState[0] == 'N'):
                        print("Carry on")
           #             ledKontroll.safe(True)




        #Lukker kobling til sqlite-databasen
        offlineConnection.closeConnection()






    # Lukker kobling til mysql-database
    connection.closeConnection()



main()
