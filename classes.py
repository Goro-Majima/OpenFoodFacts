import mysql.connector
import requests as req
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
        print("BIENVENUE SUR LE PORTAIL DU BIEN ETRE \n")

    def Choices(self):
        print("1 - Quel aliment souhaitez-vous remplacer ?")
        print("2 - Retrouver mes aliments substitués.\n")
        
class DisplayDB:

    def ShowCategory(self):
      print("Veuillez patienter...")
      print("Quelle catégorie d'aliments ? ")
      for i in range(1,21):
        sql0 = """SELECT * FROM Category WHERE idCategory = (%s)"""
        cursor.execute(sql0,(i,))
        res = cursor.fetchall()
        print(res)
    
    # def ShowProducts(self):
    #   print('Liste des produits de la catégorie: \n')
    #   sql1 = ("""SELECT * FROM Product WHERE Category_idCategory = (%s)""")
    #   cursor.execute(sql1, (categ,))
    #   res1 = cursor.fetchall()
    #   print(res1)