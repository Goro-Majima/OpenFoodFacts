import mysql.connector
import requests as req
import random
from constants import *

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
        print("---------------------------------------------------------------------")
        print("BIENVENUE SUR LE PORTAIL DU BIEN ETRE \n")

    def Choices(self):
        print("1 - Quel aliment souhaitez-vous remplacer ?")
        print("2 - Retrouver mes aliments substitués.\n")
        
class DisplayDB:
    def __init__(self):
      self.substituteDetails = [1]
    def ShowCategory(self):
      print("")
      print("Quelle catégorie d'aliments ? ")
      for i in range(1,21):
        categList = """SELECT idCategory, name_category FROM Category WHERE idCategory = (%s)"""
        cursor.execute(categList,(i,))
        catList = cursor.fetchall()
        for detailCat in catList:
          print(detailCat[0], "-", detailCat[1])
    
    def ShowProducts(self,categ):
      print('Liste des produits de la catégorie: \n')
      productList = ("""SELECT idproduct, product_name FROM Product WHERE Category_id = (%s)""")
      cursor.execute(productList, (categ,))
      productListrequest = cursor.fetchall()
      indexproduct = 0
      for i in productListrequest:
        print(productListrequest[indexproduct][0], "-", productListrequest[indexproduct][1])
        indexproduct = indexproduct + 1

    def ShowProductdetails(self, whichproduct):
      productDetails = ("""SELECT idproduct, product_name, nutriscore, store, ingredients, url FROM Product WHERE idproduct = (%s)""")
      cursor.execute(productDetails, (whichproduct,))
      productDetailsRow = cursor.fetchall()
      info = ["Référence: ", "Produit: ", "Nutrigrade: ", "Où l'acheter: ","Ingredients: ", "URL: "]
      counterRow = 0
      for productRow in productDetailsRow:
        for row in productRow:
          print(info[counterRow], row)
          counterRow = counterRow + 1
      
    def ShowAlternative(self, categ):
      
      substituteP = ("""SELECT idProduct, product_name, nutriscore, store,ingredients, url FROM Product WHERE Category_id = (%s) AND nutriscore = 'A' or 'a'""")
      cursor.execute(substituteP, (categ, ))
      substituteDetails = cursor.fetchall()
      if substituteDetails == []:
        substituteP = ("""SELECT idProduct, product_name, nutriscore, store, ingredients, url FROM Product WHERE Category_id = (%s) AND nutriscore = 'B' OR 'b'""")
        cursor.execute(substituteP, (categ, ))
        substituteDetails = cursor.fetchall()
        if substituteDetails == []:
          substituteP = ("""SELECT idProduct, product_name, nutriscore, store, ingredients, url FROM Product WHERE Category_id = (%s) AND nutriscore = 'C' OR 'c'""")
          cursor.execute(substituteP, (categ, ))
          substituteDetails = cursor.fetchall()
          if substituteDetails == []:
            substituteP = ("""SELECT idProduct, product_name, nutriscore, store, ingredients, url FROM Product WHERE Category_id = (%s) AND nutriscore = 'D' OR 'd'""")
            cursor.execute(substituteP, (categ, ))
            substituteDetails = cursor.fetchall()
      randomAlternative = random.randint(0, len(substituteDetails)-1)
      info = ["Référence: ", "Produit: ", "Nutrigrade: ", "Où l'acheter: ","Ingredients: ", "URL: "]
      counter = 0
      for productrow in substituteDetails[randomAlternative]:
        print(info[counter], productrow)
        counter = counter + 1
      print(substituteDetails[randomAlternative][0])
      self.substituteDetails = substituteDetails[randomAlternative]
      return self.substituteDetails

    def AddAlternative(self):
      print(self.substituteDetails[0])
      insertit = ("""INSERT INTO Substitute(product_id) VALUES (%s)""")
      cursor.execute(insertit, (self.substituteDetails[0], ))
      conn.commit()
      