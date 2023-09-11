import mysql.connector 

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '0531',

)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE studentdb")

print("ALL GOOD!")