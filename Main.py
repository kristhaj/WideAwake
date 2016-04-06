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
    '''
    WideAwake main process.
    '''

    #set global variables gshHandler and connection. This will be tried to initialized, if successfull wideawake is online, else offline-mode.
    gsmHandler = None
    connection = None


    #Create a controller/object to controll the interface. Uncomment this when LED interface is connected
    #ledKontroll = LEDcontrols.LEDcontrols()
    #ledKontroll.setUpLeds(ledKontroll.leds)
    try:
        try:
            gsmHandler = GSMHandler()
            #connect to database
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






        #Retrives data from database so that the data can be saved to local database(SQLite)
        cache = connection.getResultSet("SELECT Latitude,Longitude FROM Coordinates")

        #Uploads latest verson of database (retrived data) to the local database
        localdbConnection = SQLLite("Resources/WideAwakeCoordinates.db")
        localdbConnection.establishConnection()
        #localdbConnection.updateLocalDatabase(cache)
        localdbConnection.closeConnection()

        #Initialize a GPSHandler, and set the connection to the external/cloud database, GPShandler also calculates the distance between car and slippery spot.
        handler = GPSHandler()
        handler.setConnection(connection)

        #Creates a testobject with the testdata
        car = Car()

        #Iterates through the testdata, when connected to cloud database
        while(car.next()):
            if(car.tripCounter % 50 == 0):
                carSpeed = car.speed[0]
                if(carSpeed > 5):
                    #Detect if there is dangerous road condition ahead
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
        #Creates a testobject with thestData
        offlineCar = Car()

        #Connects to local dataabase
        offlineConnection = SQLLite("Resources/WideAwakeCoordinates.db")
        offlineConnection.establishConnection()

        #Initialize a offline GPShandler, that connects to the local database, and calculates distance between car and slippery spot.
        offlineHandler = GPSHandler()
        offlineHandler.setConnection(offlineConnection)

        #iterates through testdata, when connected to local database
        while(offlineCar.next()):
            if(offlineCar.tripCounter % 50 == 0):
                carSpeed = offlineCar.speed[0]
                if(carSpeed > 5):
                    #Detect if there is's a dangerous road condition ahead.
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




    finally:
        #closes connection to cloud-database
        if(not connection == None):
            connection.closeConnection()
        #closes the gsmHandler
        if(not gsmHandler == None):
            gsmHandler.closeModem()
        #closes the offlineConnetion to the local database
        if(not offlineConnection == None):
            offlineConnection.closeConnection()



main()
