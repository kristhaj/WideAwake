import unittest
import dbConnectionTest



class MyTestCase(unittest.TestCase):

    def test_connection(self):
        self.assertTrue(dbConnectionTest.connectToDB())



if __name__ == '__main__':
    unittest.main()

