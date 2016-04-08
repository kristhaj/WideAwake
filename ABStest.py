from car import Car
import unittest
from sqlLiteHandler import SQLLite
import datetime


def test():
    testuserID = '69'
    testcarID = '80085'
    testWeather = "DET REGNER :( "

    #connection = DBConnection()
    #connection.connectToDB()

    localdbConnection = SQLLite("Resources/WideAwakeCoordinates.db")
    localdbConnection.establishConnection()

    car = Car()

    while(car.next()):
        if(car.ABS):
            try:
                #Should eventually change query to something else
                query = ("SELECT max(rID) as rID FROM REPORT ")
                newID = localdbConnection.getResultSet(query)
                print(newID)
                date = datetime.datetime.now()
                newID = '7'
                coordinates = car.lat + car.long
                coordinates = (''.join(elems) for elems in coordinates)
                print (coordinates)
                #inserts a testuserID, testcarID, weather_condition, coordinates as a timestamp and the current date and time. This is a temporary query and may be subject to change
                queryToDB = "(INSERT INTO REPORT (rID, uID, cID, weather_condition, coordinate, report_time) VALUES ( + n\
                %s ,  %s, %s, %s, %s, %s )) "
                (newID, testuserID, testcarID , testWeather, coordinates , date.strftime( "%m/%d/%y/%H/%M/%S"))
                print("Hello: " + queryToDB)
                localdbConnection.executeInsertStatement(queryToDB)
                print("Complete query")
            except Exception as e:
                print(str(e))
                raise e
test()
