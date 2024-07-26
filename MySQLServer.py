import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Mr@11731103',
)

mycursor = mydb.cursor()
try:
    mycursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store')
    print("Database 'alx_book_store' created successfully!")
except Exception as e:
    print("Ane error occured: {e}")

mycursor.close()
mydb.close()
