<<<<<<< HEAD
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agriculture_dms"
=======
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agriculture_dms"
>>>>>>> a72cffaba9099136b3b23b3b7f422b5cd19dd79b
    )