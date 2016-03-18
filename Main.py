#from Interface import LEDcontrols
from dbConnection import DBConnection
from sqlLiteHandler import SQLLite
from gpsHandler import GPSHandler
from car import Car

import argparse
import time

def database(connection):
    # Oppretter et GPSHandler objekt som finner avstand fra bil til farlig veistrekke
    handler = GPSHandler()
    handler.setConnection(connection)

    # Objekt med testdata
    car = Car()

    # Går gjennom testdata når koblet til database
    while(car.next()):
        if car.tripCounter % 50 == 0:
            carSpeed = car.speed[0]
            if(carSpeed > 5):
                #Finner om det er innkommende farlig veistrekke
                gpsState = handler.compareCoordinates(car.lat[0], car.long[0])
                if (gpsState[0] == 'A'):
                    print("DANGER")
                    # ledKontroll.dangerMode(True)
                elif(gpsState[0] == 'C'):
                    print("Warning")
                    # ledKontroll.warningMode()
                elif(gpsState[0] == 'N'):
                    print("Carry on")
                    # ledKontroll.safe(True)


def main():

    #Oppretter et ledkontroll objekt, Un comment this when LED interface is connected.
    #ledKontroll = LEDcontrols.LEDcontrols()
    #ledKontroll.setUpLeds(ledKontroll.leds)
    #ledKontroll.safe(True)

    parser = argparse.ArgumentParser(description="Tool for extracting music")
    parser.add_argument(
        "-p", "--pause",
        dest="pause",
        help="Pause updates of the database in a given interval",
        default=0
    )
    args = parser.parse_args()

    if args.pause < 0:
        print("Pause interval can't be negative")

    endtime = time.time() + args.pause

    try:
        # We fall back to the offline database for the supplied interval to save internet usage.
        # We do this by triggering an exception which makes the code to use the offline database.
        if time.time() <= endtime:
            raise Exception()

        #Kobler til database
        connection = DBConnection()
        connection.connectToDB()

        #Henter data fra database slik at den kan lagres på lokal database(SQLite)
        cache = connection.getResultSet("SELECT Latitude,Longitude FROM Coordinates")

        #Laster opp nyeste versjon av database til lokal "database"
        localdbConnection = SQLLite("Resources/WideAwakeCoordinates.db")
        localdbConnection.establishConnection()
        #localdbConnection.updateLocalDatabase(cache)
        localdbConnection.closeConnection()

        database(connection)

    except:
        print("Kunne ikke koble til database")

        #Kobler til lokal database
        offlineConnection = SQLLite("Resources/WideAwakeCoordinates.db")
        offlineConnection.establishConnection()

        database(offlineConnection)

        #Lukker kobling til sqlite-databasen
        offlineConnection.closeConnection()


if __name__ == "__main__":
    main()
