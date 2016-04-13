from car import Car
import unittest
from sqlLiteHandler import SQLLite
import datetime


def test():

    #connection = DBConnection()
    #connection.connectToDB()

    localdbConnection = SQLLite("Resources/WideAwakeCoordinates.db")
    localdbConnection.establishConnection()

    car = Car()

    while(car.next()):
        if(car.ABS):
            try:
                #Should eventually change query to something else
                date = datetime.datetime.now()
                print(type(car.long[1]))
                #inserts a testuserID, testcarID, weather_condition, coordinates as a timestamp and the current date and time. This is a temporary query and may be subject to change
                queryToDB = "(INSERT INTO Coordinates(Latitude, longitude, timestamp) VALUES ( + n\
                %s, %s, %s )) "
                (car.lat[0] ,car.long[0] , date.strftime( "%m/%d/%y/%H/%M/%S"))
                localdbConnection.executeInsertStatement(queryToDB)
                print("Complete query")
            except Exception as e:
                print(str(e))
                raise e
test()
