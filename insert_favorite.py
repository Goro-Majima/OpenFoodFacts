'''Insert Product in table substitute as favorite'''
import mysql.connector
from display_db import *
from database_init import *
from connexion import *

try:
    CONN = mysql.connector.connect(host="localhost", user="student", \
    password="mot_de_passe", database="pure_beurre")
except mysql.connector.Error as erratum:
    if erratum.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif erratum.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(erratum)

CURSOR = CONN.cursor()

class Displaysub:
    '''Class related to the table Substitute and its content'''
    def substitutelist(self):
        '''Query and show previous products chosen by the user'''
        watchsub = ("""SELECT idproduct, product_name, nutriscore, store, ingredients, url \
        FROM Product INNER JOIN Substitute ON Substitute.product_id = Product.idproduct \
        WHERE product_id = idproduct """)
        CURSOR.execute(watchsub)
        watchsub = CURSOR.fetchall()
        info = ["Référence: ", "Produit: ", "Nutrigrade: ", "Où l'acheter: "\
          , "Ingredients: ", "URL: "]
        counterrow2 = 0
        for watchsubrow in watchsub:
            print("\nSubstitut: \n")
            for row in watchsubrow:
                print(info[counterrow2], row)
                counterrow2 = counterrow2 + 1
            print("--------------------------------------------------------------------------")
            counterrow2 = 0
        
        watchprev = ("""SELECT idproduct, product_name, nutriscore \
        FROM Product INNER JOIN Substitute ON Substitute.previous_id = Product.idproduct \
        WHERE previous_id = idproduct """)
        CURSOR.execute(watchprev)
        watchprev = CURSOR.fetchall()
        info = ["Référence: ", "Produit: ", "Nutrigrade: "]
        counterrow3 = 0
        for watchprevrow in watchprev:
            print("\nRemplacé: \n")
            for row in watchprevrow:
                print(info[counterrow3], row)
                counterrow3 = counterrow3 + 1
            print("--------------------------------------------------------------------------")
            counterrow3 = 0

    
       