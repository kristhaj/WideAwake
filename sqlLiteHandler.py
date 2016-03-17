import sqlite3

#self.connection.commit()
#commits the current transaction. If you don't call this method,
#anything you did since the last call to commit() is not visible from other database connections.


class SQLLite:
    '''

    '''
    def __init__(self,path):
        '''
        '''
        self.path = path
        self.connection = None
        self.cursor = None

    def establishConnection(self):
        '''
        '''
        try:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
        except:
            print('E')

    def executeInsertStatement(self,query):
        '''
        '''
        self.cursor.execute(query)
        self.connection.commit()

    def executeQueryStatement(self):
        '''
        '''
        query = "SELECT * FROM WideAwakeTrip"
        self.cursor.execute(query)
        return self.createResultSet()

    def createResultSet(self):
        '''
         This function creates the result set. Iterates through the cursor (tuple for tuple)
         adds the tuples to a list. returns the list
         :param:
         :return: resultSet, list containg tuples from query.
        '''
        resultSet = []
        for row in self.cursor:
            resultSet.append(row)
        return resultSet

    def closeConnection(self):
        '''
        '''
        self.connection.commit()
        self.connection.close()

    def createInsertStatment(self,lat,long):
        return "insert into WideAwakeTrip values ("+str(lat)+","+str(long)+")"

def main():
    #change path to coorect path of database on Pi.
    path = "Resources/WideAwakeCoordinates.db"
    conn = SQLLite(path)
    conn.establishConnection()
    lat = 10.11005
    long = 11.10005
    conn.executeInsertStatement(conn.createInsertStatment(lat,long))
    rs = conn.executeQueryStatement()
    print(rs)
    conn.closeConnection()

main()
