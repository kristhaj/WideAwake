import unittest
from dbConnection import DBConnection



class MyTestCase(unittest.TestCase):

    def test_connection(self):
        con1 = DBConnection()
        self.assertTrue(con1.connectToDB()) #true if connection is established
        con1.closeConnection()

    def test_pushNoDuplicate(self):
        con2 = DBConnection()
        con2.connectToDB()
        self.assertTrue(con2.pushToDB(str(32.123466),str(33.123456))) #make sure these are uniqe (not in db).
        con2.closeConnection()

    def test_pushDuplicate(self):
        con3 = DBConnection()
        con3.connectToDB()
        self.assertFalse(con3.pushToDB(str(63.424156),str(10.393827))) #testing for duplicate coordinates to elgseterbrua. Should return false, because they are in the
        con3.closeConnection()

    def test_PullFromDB(self):
        con4 = DBConnection()
        con4.connectToDB()
        self.assertTrue(con4.pullFromDB())
        con4.closeConnection()


if __name__ == '__main__':
    unittest.main()

