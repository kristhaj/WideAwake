'''
inneholde en cach / lokal database versjon med siste online versjon av databasen.

'''
from sqlLiteHandler import SQLLite
from gpsHandler import GPSHandler
from Interface import LEDcontrols

class OfflineMode:

    def __init__(self):
        self.interFace = LEDcontrols.LEDcontrols()
        self.handler = GPSHandler()
        self.sqlite = SQLLite()
        self.clat = 0
        self.clong = 0


    def notifyDriverOffline(self):
        self.interFace.setUpLeds(self.interFace.leds)
        self.interFace.safe(False)

    def compareCoordinates(self,carLat,carLong,carSpeed):
        rs = self.sqlite.executeQueryStatement()
        gpsState = self.handler.compareCoordinates(carLat,carLong)
        if(gpsState[0] == 'A' or gpsState[0] == 'C' and self.clat != carLat or self.clong != carLong ):
            self.clat = carLat
            self.clong = carLong
            self.handler.validateCoordinates(carLat,carLong,gpsState[1],carSpeed)






