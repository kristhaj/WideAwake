import Interface.LEDcontrols
import dbConnectionTest

def main():
    dbConnection = dbConnectionTest
    dbConnection.connectToDB()
    dbConnection.pullFromDB()
    dbConnection.closeConnection()

main()
