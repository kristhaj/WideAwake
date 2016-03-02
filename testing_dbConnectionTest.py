import unittest
import dbConnectionTest



class MyTestCase(unittest.TestCase):

    def test_connection(self):
        self.assertTrue(dbConnectionTest.connectToDB()) #true if connection is established

    def test_pushNoDuplicate(self):
        self.assertTrue(dbConnectionTest.pushToDB(str(10.123466),str(10.123456))) #make sure these are uniqe (not in db).

    def test_pushDuplicate(self):
        self.assertFalse(dbConnectionTest.pushToDB(str(63.424156),str(10.393827))) #testing for duplicate coordinates to elgseterbrua. Should return false, because they are in the

    def test_PullFromDB(self):
        self.assertTrue(dbConnectionTest.pullFromDB()) #true if managed to retrive from database


if __name__ == '__main__':
    unittest.main()

