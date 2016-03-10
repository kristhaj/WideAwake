import unittest
import dbConnectionTest
from gpsHandler import GPSHandler

class MyTestCase(unittest.TestCase):

    def test_parameter(self):
        con = dbConnectionTest
        con.connectToDB()
        handler = GPSHandler()
        state = handler.setConnection(con)
        self.assertTrue(state)



if __name__ == '__main__':
    unittest.main()
