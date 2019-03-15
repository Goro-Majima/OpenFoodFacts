"""File used to log the user to the database in order to interact with it"""
import mysql.connector
from mysql.connector import errorcode

try:
    CONN = mysql.connector.connect(
                host="localhost",
                user="student",
                password="mot_de_passe",
                database="pure_beurre",
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
CURSOR = CONN.cursor()
CONN.commit()
