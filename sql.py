import sqlite3
import datetime as datetime

def connectDB(fileName):
    return sqlite3.connect(fileName)

def closeDB(varConnection):
    varConnection.close()

def createTable(varConnection, tableName):
    varQuery = f"CREATE TABLE IF NOT EXISTS {tableName} (dataKey INTEGER PRIMARY KEY, date TEXT NOT NULL, orderCount INTEGER DEFAULT 0);"
    varConnection.execute(varQuery)

def insertData(varConnection, tableName, varDate, orderCount):
    varQuery = f"INSERT INTO {tableName} (date, orderCount) VALUES ('{varDate}', {orderCount});"
    cur = varConnection.cursor()
    cur.execute(varQuery) 

def retrunData(varConnection, tableName, varDate):
    varQuery = f"Select * from {tableName} WHERE date = '{varDate}';"
    cur = varConnection.cursor()
    cur.execute(varQuery) 
    rows = cur.fetchall()
    return rows