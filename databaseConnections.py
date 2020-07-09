import pyodbc
import os
#What-We are trying to establish a connection and read data from the database in the python console

#pyodbc just a python library helps you connect to database

#why-helping us to showcase data in the console which in real time we would display on the frontend


#Goal
# 1. 35 mins -->Establishing a database connection
#0)install pyodbc
#write import pyodbc or install pyodbc
#go to pycharm

# 1) DB server connection variables
from database_OOP import database_OOP

server = os.environ.get('db_server')
database = os.environ.get('db_database')
username = os.environ.get('db_username')
password = os.environ.get('db_password')

## OOP part
# data_oop=database_OOP(server, database, username, password)
# oop_connection=data_oop.establish_connection()
# data_oop.execute_sql('SELECT * FROM Products',oop_connection)


# Can put this in a static method
# 2) Establishing the connection-Specifying the ODBC driver, server name, database, etc. directly
#cnxnString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# connectionString='DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
#
# try:
#     with pyodbc.connect(connectionString, timeout=5) as connection:
#         print("Connection did not time out")
# except:
#      print("Connection Timed Out")
# else:

#acquire a cursor from a connection-execute the codethrough
# the cursor-cursor.fetch-iterate through the results by using the row objects that are returned by the cursor.fetch command
        # 3) Create a cursor from the connection
cursor = connection.cursor()

# investigating
print(connection)
print(cursor)



query_result = cursor.execute('SELECT * FROM Products')

print("Printing query_result object:",query_result)

# count = cursor.execute('SELECT * FROM Products').rowcount
# print("Count",count)

# .fetchone() --> output next 1 pyodbc.Row -- remember cursor maintains state
# if you want to get back to the start, you need a new cursor or to run the execute command again.
#fetchone row-fetchone(), if fetch many rows that is fetchmany(), if fetch all rows that is fetchall()
rows=query_result.fetchone()
#fetch maintains its state
print(type(rows)) #pyodbc.row object
print(rows[1])#second column of rows-columns start from 0th index
print(rows.ProductName)

rows=query_result.fetchone()
print(type(rows)) #pyodbc.row object
print(rows[1])#second column of rows-columns start from 0th index
print(rows.ProductName)


#fetchall() returns a list of row objects
#print(cursor.description)
#print(query_result.fetchone())

# fetchmany when you know how many
print("-------------FETCHMANY--------------------")
rows=query_result.fetchmany(30)
for row in rows:
    print(row.ProductID)

print("-------------FETCHALL--------------------")
rows=query_result.fetchall()

for row in rows:
    print("ProductName::"+row.ProductName, "Costs :",row.UnitPrice)

for row in rows:
    print(row[0])

# if len(rows)==0:
#     print("No rows returned")
# else:
#     print(str(len(rows)) + ' rows returned')
#     print(", ".join(column[0] for column in rows[0].cursor_description))
#     for row in rows:
#         print(",".join(str(value) for value in row))
#
