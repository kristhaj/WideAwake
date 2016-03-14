import unittest
from dbConnection import DBConnection
from gpsHandler import GPSHandler
from jsonParser import JsonParser
import time


class MyTestCase(unittest.TestCase):
    parser = JsonParser()
    #list containing dictionaries
    list = parser.getResources("Resources/downtown-crosstown.json")

    def test_parameter(self):
        con = DBConnection()
        con.connectToDB()
        handler = GPSHandler()
        state = handler.setConnection(con)
        self.assertTrue(state)

    def test_carPos_against_dbCoordinates(self):
        con = DBConnection()
        con.connectToDB()
        handler = GPSHandler()



        for i in range(len(list)):
            time1 = self.list[i]["timestamp"]
            if(self.list[i+1]["end_of_script"] == True):
                None
            else:
                name = self.list[i]["name"]
                if(name) == "latitude":
                    carLat = self.list[i]["latitude"]
                elif(name) == "longitude":
                    carLong = self.list[i]["longitude"]
                handler.compareCoordinates(carLat,carLong)

                #time to sleep between next command --> virtual real time.
                time2 = [self.list[i+1]["timestamp"]]
                time.sleep(time2-time1)






if __name__ == '__main__':
    unittest.main()
