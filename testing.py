import sql

connObj = sql.connectDB("ErikStats.db")

exchangeList = ["LSA", 'LSB', 'LSC','LSD', 'LSE']

for x in exchangeList:
    sql.createTable(connObj, x)

sql.closeDB(connObj)
print(connObj)