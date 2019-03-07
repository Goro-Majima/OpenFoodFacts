# -*- coding: utf-8 -*-

import mysql.connector
import requests as req
import json
from display_db import *
from database_init import *
from connexion import *
from insert_favorite import *

connect = Connect()
connect.connecttodb()

newdatabase = DatabaseP()
""" Already filled"""
# newdatabase.fill_table_category()
# newdatabase.fill_table_product()

MENUSCREEN = 1
while MENUSCREEN:
    user = UserIntro()
    user.Introduction()
    user.Choices()
    choice = 0

    while choice != 1 and choice != 2:
        try:
            choice = int(input("Veuillez choisir entre requête 1 ou 2:\n"))
        except ValueError:
            print("Mauvaise commande, choisir 1 ou 2")

    if choice == 1:
        # User wants to see the category list
        display = DisplayDB()
        display.ShowCategory()

        print("")
        categ = -1
        while categ < 0 or categ > 20:
            # User choose which category
            try:
                categ = int(input("Sélectionnez la catégorie entre 1 et 20:  \n"))
            except ValueError:
                print("Mauvaise commande, choisir entre 1 et 20")
        print("")

        display.ShowProducts(categ)

        print("")
        # Put an error message if input different than product list
        # loop with verification from database
        whichproduct = 0
        while whichproduct < (categ * 50) - 49 or whichproduct > categ * 50:
            try:
                whichproduct = int(
                    input("Sélectionnez l'aliment à remplacer dans sa catégorie:  \n")
                )
                print("")
            except ValueError:
                print("Mauvaise commande, choisir aliment")
                print("")
        print("")
        print("-----------------------------------------------------------")
        print("Votre sélection: ")
        print("")
        display.ShowProductdetails(whichproduct)

        print("")
        print("-----------------------------------------------------------")
        print("Produit alternatif: \n")

        display.ShowAlternative(categ)
        print("")

        favorite = input("Souhaitez-vous ajouter cet aliment à vos favoris ? O/N \n")
        while favorite != "N" and favorite != "O":
            print("Mauvaise commande, tnapez O pour OUI, N pour NON\n")
            favorite = input(
                "Souhaitez-vous ajouter cet aliment à vos favoris ? O/N \n"
            )
        if favorite == "N":
            backtomenu = input("Revenir à l'accueil ?\n")
            while backtomenu != "N" and backtomenu != "O":
                print("Mauvaise commande, tnapez O pour OUI, N pour NON\n")
                backtomenu = input("Revenir à l'accueil ? O ou N\n")
            if backtomenu == "N":
                print("")
                print("Merci d'avoir utilisé la plateforme ! A la prochaine !")
                MENUSCREEN = 0
            else:
                print("-------------------------------------------------------------\n")
        elif favorite == "O":
            print("inserting....")
            display.AddAlternative()

    elif choice == 2:
        sql2 = """SELECT * FROM Substitute"""
        cursor.execute(sql2)
        res2 = cursor.fetchall()
        if res2 == []:
            print("Il n'y a aucun produit alternatif. \n")
            print("-----------------------------------------------")
            backtomenu2 = input("Revenir à l'accueil ?\n")
            while backtomenu2 != "N" and backtomenu2 != "O":
                print("Mauvaise commande, tnapez O pour OUI, N pour NON\n")
                backtomenu2 = input("Revenir à l'accueil ? O ou N\n")
            if backtomenu2 == "N":
                print("")
                print("Merci d'avoir utilisé la plateforme ! A la prochaine !")
                MENUSCREEN = 0
            else:
                print("-------------------------------------------------------------\n")
        else:
            DISPLAYSUB = DisplaySub()
            DISPLAYSUB.substitutelist()

conn.commit()
conn.close()
