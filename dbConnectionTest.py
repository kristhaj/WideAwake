import mysql.connector
from mysql.connector import errorcode

#Connection configurations
config = {'user': 'saskaugv',
          'password':'skaugvoll',
          'host':'mysql.stud.ntnu.no',
          'database':'<databaseNavn>',
          }

def getConnection():
    global cnx
    cnx = mysql.connector.connect(**config)
    global cursor
    cursor = cnx.cursor()

def closeConnetion():
    cnx.close()


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
add_testCoordinates = ("INSERT INTO coordinates "  #coordinates = tabelName
                       "latitude, longitude "
                       "VALUES (63.424156, 10.393827)")

def pushToDB():
    cursor = cnx.cursor()
    #Insert new tuple to database
    cursor.execute(add_testCoordinates)
    #make sure data is commited to database
    cnx.commit()
    cursor.close()

def main():
    connectToDB()
    print("Will now try and push to database")
    pushToDB()
    print("Did it work?, if so now I will close the connection")
    closeConnetion()
