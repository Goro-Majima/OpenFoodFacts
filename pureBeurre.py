# -*- coding: utf-8 -*-
'''Starting program that calls insert and display functions from other file '''
import json
import mysql.connector
import requests as req
from display_db import *
from database_init import *
from connexion import *
from insert_favorite import *

CONNECT = Connect()
CONNECT.connecttodb()

NEWDATABASE = DatabaseP()
""" Already filled"""
# newdatabase.fill_table_category()
# newdatabase.fill_table_product()

MENUSCREEN = 1
while MENUSCREEN:
    USER = Userintro()
    USER.introduction()
    USER.choices()
    CHOICE = 0

    while CHOICE not in (1, 2):
        try:
            CHOICE = int(input("Veuillez choisir entre requête 1 ou 2:\n"))
        except ValueError:
            print("Mauvaise commande, choisir 1 ou 2")

    if CHOICE == 1:
        # User wants to see the category list
        DISPLAY = Displaydb()
        DISPLAY.showcategory()

        print("")
        CATEG = -1
        while CATEG < 0 or CATEG > 20:
            # User choose which category
            try:
                CATEG = int(input("Sélectionnez la catégorie entre 1 et 20:  \n"))
            except ValueError:
                print("Mauvaise commande, choisir entre 1 et 20\n\n")

        DISPLAY.showproducts(CATEG)

        # Put an error message if input different than product list
        # loop with verification from database
        WHICHPRODUCT = 0
        while WHICHPRODUCT < (CATEG * 50) - 49 or WHICHPRODUCT > CATEG * 50:
            try:
                WHICHPRODUCT = int(
                    input("\nSélectionnez l'aliment à remplacer dans sa catégorie:  \n")
                )
                print("")
            except ValueError:
                print("Mauvaise commande, choisir aliment\n\n")
            
        print("-----------------------------------------------------------")
        print("Votre sélection: \n")
        DISPLAY.showproductdetails(WHICHPRODUCT)

        print("\n-----------------------------------------------------------")
        print("Produit alternatif: \n")

        DISPLAY.showalternative(CATEG)

        FAVORITE = input("\nSouhaitez-vous ajouter cet aliment à vos favoris ? O/N \n")
        while FAVORITE not in ('N', 'O'):
            print("Mauvaise commande, tnapez O pour OUI, N pour NON\n")
            FAVORITE = input(
                "Souhaitez-vous ajouter cet aliment à vos favoris ? O/N \n"
            )
        if FAVORITE == "N":
            BACKTOMENU = input("\nRevenir à l'accueil ?\n")
            while BACKTOMENU not in ('N', 'O'):
                print("Mauvaise commande, tnapez O pour OUI, N pour NON\n")
                BACKTOMENU = input("Revenir à l'accueil ? O ou N\n")
            if BACKTOMENU == "N":
                print("")
                print("Merci d'avoir utilisé la plateforme ! A la prochaine !")
                MENUSCREEN = 0
            else:
                print("-------------------------------------------------------------\n")
        elif FAVORITE == "O":
            print("insertion....")
            DISPLAY.addalternative()

    elif CHOICE == 2:
        REQSUB = """SELECT * FROM Substitute"""
        CURSOR.execute(REQSUB)
        REQSUB = CURSOR.fetchall()
        if REQSUB == []:
            print("\nIl n'y a aucun produit alternatif. \n")
            print("-----------------------------------------------")
            BACKTOMENU2 = input("Revenir à l'accueil ?\n")
            while BACKTOMENU2 not in ('O', 'N'):
                print("Mauvaise commande, tnapez O pour OUI, N pour NON\n")
                BACKTOMENU2 = input("Revenir à l'accueil ? O ou N\n")
            if BACKTOMENU2 == "N":
                print("")
                print("Merci d'avoir utilisé la plateforme ! A la prochaine !")
                MENUSCREEN = 0
            else:
                print("-------------------------------------------------------------\n")
        else:
            DISPLAYSUB = Displaysub()
            DISPLAYSUB.substitutelist()

CONN.commit()
CONN.close()
