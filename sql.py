import sqlite3

class DBconnector:

    def __init__(self, fileName):
        self.con = sqlite3.connect(fileName)

    def closeDB(self):
        self.con.close()

    def createTable(self, tableName):
        varQuery = f"CREATE TABLE IF NOT EXISTS {tableName} (ID INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT NOT NULL, orderCount INTEGER DEFAULT 0);"
        self.con.execute(varQuery)

    def insertData(self, tableName, varDate, orderCount):
        varQuery = f"INSERT INTO {tableName} (date, orderCount) VALUES ('{varDate}', {orderCount});"
        cur = self.con.cursor()
        cur.execute(varQuery) 
        self.con.commit()
        return cur.fetchall()

    def returnData(self, tableName, varDate):
        varQuery = f"Select * from {tableName} where date = '{varDate}';"
        cur = self.con.cursor()
        cur.execute(varQuery) 
        return cur.fetchall()

    def AddHoc(self, sqlCode):
        cur = self.con.cursor()
        cur.execute(sqlCode)
        return cur.fetchall()