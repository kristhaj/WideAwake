import sqlite3

#self.connection.commit()
#commits the current transaction. If you don't call this method,
#anything you did since the last call to commit() is not visible from other database connections.


class SQLLite:
    '''
    This class handles the WideAwake local database. Sets, executes, and closes connection with the SQLlite db.
    '''
    def __init__(self,path):
        '''
        Sets the class static variables
        '''
        self.path = path
        self.connection = None
        self.cursor = None

    def establishConnection(self):
        '''
        Establishes the connection with the SQLLite database, and creates a cursor object to execute statements.
        :return: True if successful, False else.
        '''
        try:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
            return True
        except:
            return False

    def executeInsertStatement(self,query):
        '''
        Executes the insert statment. Inserts new coordinates into database.
        :param query: the insert statement to be executed
        :return: True if execute successful, False if not.
        '''
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False

    def executeQueryStatement(self):
        '''
        Executes the query statement and returns resultset.
        :return: resultSet as List if successfull, else False.
        '''
        query = "SELECT * FROM WideAwakeTrip"
        try:
            self.cursor.execute(query)
            return self.createResultSet()
        except:
            return False

    def createResultSet(self):
        '''
        This function creates the result set. Iterates through the cursor (tuple for tuple)
        adds the tuples to a list. returns the list
        :return: ResultSet as a list containg tuples from database.
        '''
        resultSet = []
        for row in self.cursor:
            resultSet.append(row)
        return resultSet

    def closeConnection(self):
        '''
        Commits latest changes, and closes connection.
        :return: True if successfully closed commited and closed connection. False else
        '''
        try:
            self.connection.commit()
            self.connection.close()
            return True
        except:
            return False

    def createInsertStatment(self,lat,long):
        '''
        Creates a insert statment with the given coordinates.
        :param lat: Car latitude to push to local database.
        :param long: Car longitude to push to local database
        :return: SQLlite insert-statment.
        '''
        return "insert into WideAwakeTrip values ("+str(lat)+","+str(long)+")"

def main():
    #change path to coorect path of database on Pi.
    path = "Resources/WideAwakeCoordinates.db"
    conn = SQLLite(path)
    conn.establishConnection()
    lat = 10.11006
    long = 11.10006
    conn.executeInsertStatement(conn.createInsertStatment(lat,long))
    rs = conn.executeQueryStatement()
    print(rs)
    conn.closeConnection()

#main()
