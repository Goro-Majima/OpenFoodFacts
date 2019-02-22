# -*- coding: utf-8 -*-

import mysql.connector
import requests as req
import json
from constants import *
from classes import *
from mysql.connector import errorcode

# r= req.get('https://fr.openfoodfacts.org/category/pizzas.json')


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

user = UserIntro()
user.Introduction()
user.Choices()
choice = int(input("Veuillez choisir entre ces deux requêtes:"))
while choice != 1 and choice != 2:
  user.Choices()
  choice = int(input("TAPEZ 1 OU 2:"))
if choice == 1:
  print("Veuillez patienter...")
  print("Quelle catégorie d'aliments ?  choix: ")
  sql0 = """SELECT * FROM Category"""
  cursor.execute(sql0)
  res = cursor.fetchall()
  print(res)
  print("")

  categ = -1
  while categ < 0 or categ >= 20:
    categ = int(input("Choix de la categorie entre 1 et 10:  \n"))
  
  print("")
  print('Liste des produits de la catégorie: \n')
  sql1 = ("""SELECT * FROM Product WHERE Category_idCategory = (%s)""")
  cursor.execute(sql1, (categ,))
  res1 = cursor.fetchall()
  print(res1)
  print("")

  
  whichproduct = int(input("Choisissez l'id du produit à remplacer:  \n"))

  #retrieve and recommend a similar product with a better nutrition grade


elif choice == 2:
  sql2 = ("""SELECT * FROM Substitute""")
  cursor.execute(sql2)
  res2 = cursor.fetchall()
  if res2 == []:
    print("Il n'y a aucun produit alternatif. \n")

r = req.get('https://fr.openfoodfacts.org/category/pizzas.json')

conn.commit()
conn.close()
