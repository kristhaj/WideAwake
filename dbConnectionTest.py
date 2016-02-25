import mysql.connector
from mysql.connector import errorcode

#Connection configurations
config = {'user': 'saskaugv',
          'password':'skaugvoll',
          'host':'mysql.stud.ntnu.no',
          'database':'tshumbor_WideAwake',
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
    #if connection attempt failed, do:
    except mysql.connector.Error as err:
        if(err.errno == errorcode.ER_ACCESS_DENIED_ERROR):
            print("Something is wrong with your user name or password")
        elif(err.errno == errorcode.ER_BAD_DB_ERROR):
            print("Database does not exist")
        else:
            print(err)


#Creates testData to be uploaded
#coordinates = tabelName
add_testCoordinates = ("INSERT INTO Coordinates (latitude, longitude) VALUES (63.424156, 10.393827)")

#try and push data to the schema tabel
def pushToDB():
    cursor = cnx.cursor()
    #Insert new tuple to database
    cursor.execute(add_testCoordinates)
    #make sure data is commited to database
    cnx.commit()
    cursor.close()

#SQL-statment to execute on database (retrive tuples)
#coordinates = tabelName
query = ("SELECT latitude, longitude FROM Coordinates")

#query a select-statment from the database
def pullFromDB():
    cursor.execute(query)
    toString()

#format the output from the query
def toString():
    for (latitude, longitude) in cursor:
        print () #print a space between each tuple
        print("Long: " + str(longitude))
        print("Lat: " + str(latitude))



#Run testScript, Try to connect, push and pull data. then prensent data or errors to user.
def main():
    connectToDB()
    print("Will now try and push to database")
    pushToDB()
    print("It worked! lets try and retrive from the database")
    pullFromDB()
    print("Did it work?, if so the connection will now be closed")
    closeConnetion()

main()