# DatabasePythonProject

## pyodbc introduction

All if the information contained here and the information used can be found on the pyodbc git wiki [here](https://github.com/mkleehammer/pyodbc/wiki).

### What is pyodbc?

as per the git wiki pyodbc is an open source Python module that makes accessing ODBC databases simple. An ODBC driver uses the Open Database Connectivity (ODBC)
interface by Microsoft that allows applications to access data in database management systems (DBMS) using SQL as a standard for accessing the data.

essentially pyodbc is an implementation of a driver that allows you to connect to pretty much any database.


### Cursor

A cursor itself is a control structure that allows us to control and manage rows of data from a response. In the pyodbc instance is used to manage our queries directly with the db.
