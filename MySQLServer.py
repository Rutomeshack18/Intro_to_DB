import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
)

mycursor = mydb.cursor()
try:
    mycursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store')
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print("An error occured: {e}")

mycursor.close()
mydb.close()