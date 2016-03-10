import unittest
import dbConnectionTest
import gpsHandler

class MyTestCase(unittest.TestCase):

    def test_parameter(self):
        con = dbConnectionTest
        con.connectToDB()
        handler = gpsHandler
        state = handler.setConnection(con)
        self.assertTrue(state)



if __name__ == '__main__':
    unittest.main()
