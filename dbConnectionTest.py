"""
WideAwake documentation for sprint 1.
"""
import mysql.connector
from mysql.connector import errorcode

import dbConfig

usr = dbConfig.getUsr()
pwd = dbConfig.getPwd()
host = dbConfig.getHost()
db = dbConfig.getDB()

#Connection configurations
config = {'user': usr,
          'password': pwd,
          'host': host,
          'database': db,
          }

def getConnection():
    """
    This creates the database connection, cnx, and the database cursor, cursor, initialising  both globaly
    The database credentials are stored in a separate file not stored on github so the database is secure.

    :cnx: mysql.connector
    :cursor: mysql.connector.cursor
    :return: nothing directly, but sets the two global variables cnx and cursor
    """
    global cnx
    cnx = mysql.connector.connect(**config)
    global cursor
    cursor = cnx.cursor()


def closeConnection():
    """
    Closes the database connection
    """
    cnx.close()

def connectToDB():
    """
    Connects the scripts to the database using getConnection().
    Returns true if successful, or false if unsuccessful.
    Also prints the errors if there are any.

    :return: boolean
    """
    try:
        #Try to connect to database with config
        getConnection()
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


def pushToDB(lat, long):
    """
    Pushes gps data to the database.
    Returns true if it is successful, or false if it is unsuccessful.
    Also prints the errors if there are any.

    :param lat: number
    :param long: number
    :return: boolean
    """
    #create test query, coordinates = tabelName
    add_testCoordinates = ("INSERT INTO Coordinates (Latitude, Longitude) VALUES ("+lat+", "+long+")")
    cursor = cnx.cursor()
    #Insert new tuple to database
    try:
        cursor.execute(add_testCoordinates)
        cnx.commit()
        cursor.close()
        print("Successfylly pushed to database")
        return True
#This exception is raised when the relational integrity of the data is affected. For example, a duplicate key was inserted or a foreign key constraint would fail.
    except mysql.connector.IntegrityError as err:
        print("Error: {}".format(err))
        return False

    #make sure data is commited to database


#SQL-statment to execute on database (retrive tuples)
#coordinates = tabelName
query = ("SELECT Latitude, Longitude FROM Coordinates")

def pullFromDB():
    """
    Pulls gps coordinates from the database.
    Returns true if it is successful, or false if it is unsuccessful.

    :return: boolean
    """
    try:
        cursor.execute(query)
        toString()
        print("Successfully pulled from database")
        return True
    except Exception:
        return False

def toString():
    """
    Formats and prints the tuples the cursor is pointing at.

    :return: None
    """
    for (latitude, longitude) in cursor:
        print () #print a space between each tuple
        print("Latitude: " + str(latitude))
        print("Longitude: " + str(longitude))


def main():
    """
    Runs the testscript wich tries to connect, push and pull data. Then presents the data or errors to the user.
    Uses connectToDB, pushToDB, pullFromDB, closeConnection, printing what step the script is on before executing it.

    :return: None
    """
    if(connectToDB()):
        print("Will now try and push to database")

        #Creates testData to be uploaded
        lat,long = str(29.113456),str(16.997549)

        pushToDB(lat, long)

        print("Will now try and pull from database")
        pullFromDB()
        print("\nConnection will now terminate")
        closeConnection()
    else:
        print("could not connect to the database")

#main()
