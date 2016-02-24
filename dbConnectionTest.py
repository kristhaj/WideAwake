import mysql.connector
from mysql.connector import errorcode

#Connection configurations
config = {'user': 'username',
          'password':'password',
          'host':'ip-adr',
          'database':'coordinates',
          }


def connectToDB():
    try:
        cnx = mysql.connector.connect(**config)
        print("Connection established to database")
    except mysql.connector.Error as err:
        if(err.errno == errorcode.ER_ACCESS_DENIED_ERROR):
            print("Something is wrong with your user name or password")
        elif(err.errno == errorcode.ER_BAD_DB_ERROR):
            print("Database does not exist")
        else:
            print(err)




def main():
    connectToDB()

