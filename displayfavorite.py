'''Insert an alternative product in table substitute as favorite'''
import mysql.connector
from displaydb import *
from databaseinit import *
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
        '''Query and show substituted and previous products chosen by the user'''
        watchsub = ("""SELECT idproduct, product_name, nutriscore, store, ingredients, url \
        FROM Product INNER JOIN Substitute ON Substitute.product_id = Product.idproduct \
        WHERE product_id = idproduct ORDER BY idsubstitute""")
        CURSOR.execute(watchsub)
        watchsub = CURSOR.fetchall()
        info = ["Référence: ", "Produit: ", "Nutrigrade: ", "Où l'acheter: "\
          , "Ingredients: ", "URL: "]
        counterrow2 = 0
        idkey = 0
        while idkey < len(watchsub):
            info = ["Référence: ", "Produit: ", "Nutrigrade: ", "Où l'acheter: "\
            , "Ingredients: ", "URL: "]
            print("\nProduit favori: \n")
            for row in watchsub[idkey]:
                print(info[counterrow2], row)
                counterrow2 = counterrow2 + 1
            counterrow2 = 0
            watchprev = ("""SELECT idproduct, product_name, nutriscore, store, ingredients, url \
            FROM Product INNER JOIN Substitute ON Substitute.previous_id = Product.idproduct \
            WHERE previous_id = idproduct ORDER BY idsubstitute""")
            CURSOR.execute(watchprev)
            watchprev = CURSOR.fetchall()
            counterrow3 = 0
            print("\nProduit remplacé: \n")
            for watchprevrow in watchprev[idkey]:
                print(info[counterrow3], watchprevrow)
                counterrow3 = counterrow3 + 1
            idkey = idkey + 1
            counterrow3 = 0
            print("--------------------------------------------------------------------------")
            #problème avec l'ordre des produits dans la table substitute, les remplacés ne correspondent pas aux favoris car classé par ordre numérique réparé avec ORDER BY
    