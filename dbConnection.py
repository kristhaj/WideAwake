"""
WideAwake documentation for sprint 1.
"""
import mysql.connector
from mysql.connector import errorcode
import dbConfig

class DBConnection:
    '''
    This class sets the database connection and handles all SQL statements and querys to the database.
    '''

    # SQL-statment to execute on database (retrive tuples)
    # coordinates = tabelName
    query = ("SELECT Latitude, Longitude, Timestamp FROM Coordinates")

    def __init__(self):
        '''
        This sets all the class variables static and initializes
        :return: Nothing
        '''
        self.cnx = None
        self.cursor = None

        #Connection configurations
        self.config = {
            'user': dbConfig.getUsr(),
            'password': dbConfig.getPwd(),
            'host': dbConfig.getHost(),
            'database': dbConfig.getDB()
        }

    def getConnection(self):
        """
        This creates the database connection, cnx, and the database cursor, cursor, initialising  both globaly
        The database credentials are stored in a separate file not stored on github so the database is secure.

        :cnx: mysql.connector
        :cursor: mysql.connector.cursor
        :return: nothing directly, but sets the two global variables cnx and cursor
        """

        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()


    def closeConnection(self):
        """
        Closes the database connection
        """
        self.cnx.close()

    def connectToDB(self):
        """
        Connects the scripts to the database using getConnection().
        Returns true if successful, or false if unsuccessful.
        Also prints the errors if there are any.

        :return: boolean
        """
        try:
            #Try to connect to database with config
            self.getConnection()
            #if connection successful
            print("Connection established to database")
            return True
        #if connection attempt failed, do:
        except mysql.connector.Error as err:
            if(err.errno == errorcode.ER_ACCESS_DENIED_ERROR):
                print("Something is wrong with your user name or password")
            elif(err.errno == errorcode.ER_BAD_DB_ERROR):
                print("Database does not exist")
            else:
                print(err)
            return False


    def pushToDB(self,lat, long):
        """
        Pushes gps data to the database.
        Returns true if it is successful, or false if it is unsuccessful.
        Also prints the errors if there are any.

        :param lat: number
        :param long: number
        :return: boolean
        """
        #create test query, coordinates = tabelName
        add_testCoordinates = ("INSERT INTO Coordinates (Latitude, Longitude, Timestamp) VALUES ("+lat+", "+long+", NOW())")
        cursor = self.cnx.cursor()
        #Insert new tuple to database
        try:
            cursor.execute(add_testCoordinates)
            self.cnx.commit()
            cursor.close()
            #print("Successfylly pushed to database")
            return True
    #This exception is raised when the relational integrity of the data is affected. For example, a duplicate key was inserted or a foreign key constraint would fail.
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))
            return False

        #make sure data is commited to database

    def pullFromDB(self):
        """
        Pulls gps coordinates from the database.
        Returns true if it is successful, or false if it is unsuccessful.

        :return: boolean
        """
        try:
            self.cursor.execute(self.query)
            #self.toString()
            #print("Successfully pulled from database")
            return True
        except Exception:
            return False

    def getResultSet(self,query):
        '''
        Pulls gps coordinates from the database Returns the resultset as a list containg coordinates as tuples (lat,long)
        :resultSet: list with tuples (lat,long) from database.
        :param query: SQL query to execute.
        :return: resultSet as list with tuples or False.
        '''
        try:
            self.cursor.execute(query)
            #self.toString()
            resultSet = self.toList()
            #print("Successfully pulled from database")
            return resultSet
        except Exception:
            return False


    def toList(self):
        '''
        Creates and Appends all tuples in database to a list and then returns this list.
        :return: List with tuples from database.
        '''
        result = []
        for (latitude, longitude, timestamp) in self.cursor:
            result.append((latitude,longitude, timestamp))

        return result


    def toString(self):
        """
        Formats and prints the tuples the cursor is pointing at.

        :return: None
        """
        for (latitude, longitude, timestamp) in self.cursor:
            print () #print a space between each tuple
            print("Latitude: " + str(latitude))
            print("Longitude: " + str(longitude))
            print("Timetamp " + str(timestamp))


def main():
    """
    Runs the testscript wich tries to connect, push and pull data. Then presents the data or errors to the user.
    Uses connectToDB, pushToDB, pullFromDB, closeConnection, printing what step the script is on before executing it.

    :return: None
    """
    connection = DBConnection()

    if(connection.connectToDB()):
        print("Will now try and push to database")

        #Creates testData to be uploaded
        lat,long = str(40.768967),str(-73.993202)
        connection.pushToDB(lat, long)

        print("Will now try and pull from database")
        connection.pullFromDB()
        print("\nConnection will now terminate")
        connection.closeConnection()
    else:
        print("could not connect to the database")

#main()