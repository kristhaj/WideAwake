#from Interface import LEDcontrols
from dbConnection import DBConnection
from sqlLiteHandler import SQLLite
from gpsHandler import GPSHandler
from gsmHandler import GSMHandler
from car import Car
import UnusableSystemException
from offlineMode import OfflineMode
from jsonParser import JsonParser
import sqlite3
import time
import sys




def main():
    gsmHandler = None
    connection = None

    #Oppretter et ledkontroll objekt, Un comment this when LED interface is connected.
    #ledKontroll = LEDcontrols.LEDcontrols()
    #ledKontroll.setUpLeds(ledKontroll.leds)
    try:
        try:
            gsmHandler = GSMHandler()
            #Kobler til database
            connection = DBConnection()
            connection.connectToDB()
            #ledKontroll.safe(True)
        except UnusableSystemException as e:
            print(str(e))
            #Since this exception occured, it means that there is something wrong with the gsmHandler. It could not
            #connect to the gsm module, or the connection did not connect correctly. Notify user that in offline mode.
            #ledKontroll.safe(False)
            raise e # rais this to exit the try online, and go to expect offline
        except Exception as e:
            print(str(e))
            #ledKontroll.safe(False)
            raise e # rais this to exit the try online, and go to expect offline






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
            if car.tripCounter%300 == 0: #This is just under 2 seconds time
                
                pass
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
        offlineHandler.setConnection(offlineConnection)

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

    finally:
        # Lukker kobling til mysql-database
        if(not connection == None):
            connection.closeConnection()
        if(not gsmHandler == None):
            gsmHandler.closeModem()



main()
