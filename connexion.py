"""File used to log the user to the database in order to interact with it"""
import mysql.connector
from mysql.connector import errorcode


class Connect:
    """Related to files that need authentication to enter the database"""
    # def __init__(self):
    #     cursor = self.cursor
    def connecttodb(self):
        """Check authentication in order to use the database pure_beurre"""
        try:
            conn = mysql.connector.connect(
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

        conn.commit()
