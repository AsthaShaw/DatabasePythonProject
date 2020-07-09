# 1) DB server connection variables
from database_OOP import database_OOP
import os

server = os.environ.get('db_server')
database = os.environ.get('db_database')
username = os.environ.get('db_username')
password = os.environ.get('db_password')


## OOP part
user_input=int(input("Please enter the number for the operation you want us to execute::"
                     "\n 1. Fetch one row \n 2. Fetch many rows \n 3. Fetch All rows \n"))
data_oop=database_OOP(server, database, username, password)
oop_connection=data_oop.establish_connection()
data_oop.execute_sql('SELECT * FROM Products', oop_connection, user_input)
#data_oop.execute_sql("'SELECT ProductId, ProductName FROM Products w'", now, user_id).rowcount

#Assignment:-Calculate the average unit price of all the products