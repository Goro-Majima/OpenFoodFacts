import mysql.connector
import requests as req
from constants import *
import random

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

class UserIntro:
    # Start the interaction with users.
    def Introduction(self):
        print("BIENVENUE SUR LE PORTAIL DU BIEN ETRE \n")

    def Choices(self):
        print("1 - Quel aliment souhaitez-vous remplacer ?")
        print("2 - Retrouver mes aliments substitués.\n")
        
class DisplayDB:

    def ShowCategory(self):
      print("")
      print("Quelle catégorie d'aliments ? ")
      for i in range(1,21):
        categList = """SELECT idCategory, name_category FROM Category WHERE idCategory = (%s)"""
        cursor.execute(categList,(i,))
        catList = cursor.fetchall()
        print(catList)
    
    def ShowProducts(self,categ):
      print('Liste des produits de la catégorie: \n')
      productList = ("""SELECT idproduct, product_name FROM Product WHERE Category_id = (%s)""")
      cursor.execute(productList, (categ,))
      productListrequest = cursor.fetchall()
      indexproduct = 0
      for i in productListrequest:
        print(productListrequest[indexproduct])
        indexproduct = indexproduct + 1

    def ShowProductdetails(self, whichproduct):
      productDetails = ("""SELECT product_name, nutriscore, store, url FROM Product WHERE idproduct = (%s)""")
      cursor.execute(productDetails, (whichproduct,))
      productDetailsRow = cursor.fetchall()
      print(productDetailsRow)
      
    def ShowAlternative(self, categ):
      substituteP = ("""SELECT product_name, nutriscore, store, url FROM Product WHERE Category_id = (%s) AND nutriscore = 'A' or 'a'""")
      cursor.execute(substituteP, (categ, ))
      substituteDetails = cursor.fetchall()
      if substituteDetails == []:
        substituteP = ("""SELECT product_name, nutriscore, store, url FROM Product WHERE Category_id = (%s) AND nutriscore = 'B' OR 'b'""")
        cursor.execute(substituteP, (categ, ))
        substituteDetails = cursor.fetchall()
      randomAlternative = random.randint(0, len(substituteDetails))
      print(substituteDetails[randomAlternative])
      
# class UpdateDB:
#   def insertAlternative():
    