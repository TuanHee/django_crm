import mysql.connector

connector = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)

# prepare a cursor object
cursor = connector.cursor()

#Create a database
cursor.execute("CREATE DATABASE dcrm")

print("All Done!")