import unittest
import dbConnection
from gpsHandler import GPSHandler
from jsonParser import JsonParser

class MyTestCase(unittest.TestCase):

    def test_parameter(self):
        con = dbConnection()
        con.connectToDB()
        handler = GPSHandler()
        state = handler.setConnection(con)
        self.assertTrue(state)

    def test_carPos_against_dbCoordinates(self):
        con = dbConnection()
        con.connectToDB()
        handler = GPSHandler()
        parser = JsonParser()
        dictionary = parser.getWantedAttributes()
        print(dictionary)


if __name__ == '__main__':
    unittest.main()
