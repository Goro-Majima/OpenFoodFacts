# -*- coding: utf-8 -*-

import mysql.connector
import requests as req
import json
from constants import *
from classes import *
from database_init import *
from mysql.connector import errorcode
#from connexion import *


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
  # User wants to see the category list
  display = DisplayDB()
  display.ShowCategory() 

  print("")  
  categ = -1
  while categ < 0 or categ > 20:
    # User choose which category
    categ = int(input("Sélectionnez la catégorie:  \n"))
  
  print("")
  
  display.ShowProducts(categ)

  print("")
  # Put an error message if input different than product list 
  # loop with verification from database 
  whichproduct = int(input("Sélectionnez l'aliment à remplacer:  \n"))
  print("")
  print("Votre sélection: ")
  display.ShowProductdetails(whichproduct)

  print("")
  print("-----------------------------------------------------------")
  print("Produit alternatif: ")
  print("")

  display.ShowAlternative(categ)
  print("")

  favorite = input("Souhaitez-vous ajouter cet aliment à vos favoris ? O/N ")
  if favorite == 'O':
    insertit = ("""INSERT INTO Substitute...""")
    #alter table susbstitute modify auto_increment

  

elif choice == 2:
  sql2 = ("""SELECT * FROM Substitute""")
  cursor.execute(sql2)
  res2 = cursor.fetchall()
  if res2 == []:
    print("Il n'y a aucun produit alternatif. \n")

newdatabase = DatabaseP()
""" Already filled"""
#newdatabase.fill_table_category()
#newdatabase.fill_table_product()

conn.commit()
conn.close()
