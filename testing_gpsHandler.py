import unittest
from dbConnection import DBConnection
from gpsHandler import GPSHandler
from jsonParser import JsonParser
import time


class MyTestCase(unittest.TestCase):
    carLat = None
    carLong= None

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

        parser = JsonParser()
        #list containing dictionaries
        list = parser.getResources("Resources/downtown-crosstown.json")
        #Go through the dataset - dictionary/line for line.
        for i in range(len(list)):
            carLat = None
            carLong = None
            time1 = list[i]["timestamp"]
            #if end of script is next, it means that we have read the last (lat,long) tuples in dataset.
            if("end_of_script" in list[i+1]):
                break

            else:
                name = list[i]["name"]
                #latitude always comes before longitude, in dataset.
                if(list[i]["name"]) == "latitude":
                    carLat = list[i]["value"]
                if(list[i+1]["name"]) == "longitude":
                    carLong = list[i+1]["value"]


                state = handler.compareCoordinates(carLat,carLong)
                if(state == 'A'):
                    self.assertEquals(handler.compareCoordinates(carLat,carLong),'A',(40.768967,-73.993202),None)
                elif(state == 'C'):
                    self.assertEquals(handler.compareCoordinates(carLat,carLong),'C',(40.768967,-73.993202),None)


                #time to sleep between next command --> virtual real time.
                time2 = list[i+1]["timestamp"]
                print(time2-time1)
                d = ((time2-time1)/1000000)
                print(d)
                if(d >= 0):
                    time.sleep((time2-time1)/1000000)

            self.fail()


if __name__ == '__main__':
    unittest.main()
