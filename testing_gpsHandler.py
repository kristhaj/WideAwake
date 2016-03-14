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
        testState = False
        con = DBConnection()
        con.connectToDB()
        handler = GPSHandler()
        handler.setConnection(con)
        parser = JsonParser()
        parser.removeWantedAttribute("vehicle_speed")
        parser.addWantedAttribute("vehicle_speed",False)
        #list containing dictionaries
        list = parser.getResources("Resources/downtown-crosstown.json")
        #Go through the dataset - dictionary/line for line.
        for i in range(len(list)):

            time1 = list[i]["timestamp"]
            #if end of script is next, it means that we have read the last (lat,long) tuples in dataset.
            if("end_of_script" in list[i+1]):
                print("end_of_script")
                break
            else:
                #latitude always comes before longitude, in dataset.
                if(list[i]["name"]) == "latitude":
                    #print(list[i]["value"])
                    self.carLat = list[i]["value"]
                    #print("lat" + str(self.carLat))
                if(list[i+1]["name"]) == "longitude":
                    self.carLong = list[i+1]["value"]
                    #print("long" + str(self.carLong))

                #print("lat :" + str(self.carLat) + "    long : " + str(self.carLong))
                state = handler.compareCoordinates(self.carLat,self.carLong)
                print(state)
                if(state[0] == "A"):
                    print("que A")
                    testState = True
                elif(state[0] == "C"):
                    print("que C")
                    testState = True

                #time to sleep between next command --> virtual real time.
                time2 = list[i+1]["timestamp"]
                d = ((time2-time1)/1000000)
                #if(d >= 0):
                    #time.sleep(d)
        if(testState == False):
            self.fail()

if __name__ == '__main__':
    unittest.main()
