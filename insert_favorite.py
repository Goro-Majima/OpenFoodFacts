import mysql.connector
import requests as req
import json
from display_db import *
from database_init import *
from connexion import *

try:
  conn = mysql.connector.connect(host = "localhost", user = "student", password = "mot_de_passe", database = "pure_beurre")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

cursor = conn.cursor()

class DisplaySub:
  def SubstituteList(self):
    watchsub = ("""SELECT idproduct, product_name, nutriscore, store, ingredients, url FROM Product \
    INNER JOIN Substitute ON Substitute.product_id = Product.idproduct WHERE product_id = idproduct """)
    cursor.execute(watchsub)
    WATCHSUB = cursor.fetchall()
    info = ["Référence: ", "Produit: ", "Nutrigrade: ", "Où l'acheter: ","Ingredients: ", "URL: "]
    counterRow2 = 0
    for watchsubRow in WATCHSUB:
      for row in watchsubRow:
        print(info[counterRow2], row)
        counterRow2 = counterRow2 + 1
      print("--------------------------------------------------------------------------")
      