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
#Establish connection to the database with config-user information
def getConnection():
    global cnx
    cnx = mysql.connector.connect(**config)
    global cursor
    cursor = cnx.cursor()


#close the connection to the databae
def closeConnetion():
    cnx.close()

#Try and connect to database, otherwise print error message.
def connectToDB():
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


#try and push data to the schema tabel
def pushToDB(lat, long):
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

#query a select-statment from the database
def pullFromDB():
    try:
        cursor.execute(query)
        toString()
        print("Successfully pulled from database")
        return True
    except Exception:
        return False

#format the output from the query
def toString():
    for (latitude, longitude) in cursor:
        print () #print a space between each tuple
        print("Latitude: " + str(latitude))
        print("Longitude: " + str(longitude))


#Run testScript, Try to connect, push and pull data. then prensent data or errors to user.
def main():
    if(connectToDB()):
        print("Will now try and push to database")

        #Creates testData to be uploaded
        lat,long = str(29.113456),str(16.997549)

        pushToDB(lat, long)

        print("Will now try and pull from database")
        pullFromDB()
        print("\nConnection will now terminate")
        closeConnetion()
    else:
        print("could not connect to the database")

main()
