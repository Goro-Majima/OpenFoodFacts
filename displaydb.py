'''Regroup functions that display all datas from the local base according, also insert substitutes'''
import random
from connexion import *

class Userintro:
    ''' Start the interaction with users.'''
    def introduction(self):
        ''' display the welcome text'''
        print("---------------------------------------------------------------------")
        print("BIENVENUE SUR LE PORTAIL DU BIEN ETRE \n")

    def choices(self):
        '''display input choice'''
        print("1 - Quel aliment souhaitez-vous remplacer ?")
        print("2 - Retrouver mes aliments substitués.\n")


class Displaydb:
    '''Display category, product tables to the user'''
    def __init__(self):
        self.substitutedetails = []
        self.productdetailsrow = []

    def showcategory(self):
        '''show category list to user'''
        print("")
        print("Quelle catégorie d'aliments ? ")
        for i in range(1, 21):
            categlist = """SELECT idCategory, name_category FROM Category WHERE idCategory = (%s)"""
            CURSOR.execute(categlist, (i,))
            catlist = CURSOR.fetchall()
            for detailcat in catlist:
                print(detailcat[0], "-", detailcat[1])

    def showproducts(self, categ):
        '''show all products from the category user choose'''
        print("Liste des produits de la catégorie: \n")
        productlist = (
            """SELECT idproduct, product_name FROM Product WHERE Category_id = (%s)"""
        )
        CURSOR.execute(productlist, (categ,))
        productlistrequest = CURSOR.fetchall()
        indexproduct = 0
        for i in productlistrequest:
            print(
                productlistrequest[indexproduct][0],
                "-",
                productlistrequest[indexproduct][1],
            )
            indexproduct = indexproduct + 1

    def showproductdetails(self, whichproduct):
        '''show all details of chosen product'''
        productdetails = """SELECT idproduct, product_name, nutriscore, store, ingredients, url FROM Product WHERE idproduct = (%s)"""
        CURSOR.execute(productdetails, (whichproduct,))
        productdetailsrow = CURSOR.fetchall()
        info = [
            "Référence: ",
            "Produit: ",
            "Nutrigrade: ",
            "Où l'acheter: ",
            "Ingredients: ",
            "URL: ",
        ]
        counterrow = 0
        for productrow in productdetailsrow:
            for row in productrow:
                print(info[counterrow], row)
                counterrow = counterrow + 1
        self.productdetailsrow = productdetailsrow
        print(self.productdetailsrow[0][0])
        return self.productdetailsrow

    def showalternative(self, categ):
        ''' Recommend a better nutrigrade product from the same category'''
        substitutep = """SELECT idProduct, product_name, nutriscore, store,ingredients, url FROM Product WHERE Category_id = (%s) AND nutriscore = 'A' or 'a'"""
        CURSOR.execute(substitutep, (categ,))
        substitutedetails = CURSOR.fetchall()
        if substitutedetails == []:
            substitutep = """SELECT idProduct, product_name, nutriscore, store, ingredients, url FROM Product WHERE Category_id = (%s) AND nutriscore = 'B' OR 'b'"""
            CURSOR.execute(substitutep, (categ,))
            substitutedetails = CURSOR.fetchall()
            if substitutedetails == []:
                substitutep = """SELECT idProduct, product_name, nutriscore, store, ingredients, url FROM Product WHERE Category_id = (%s) AND nutriscore = 'C' OR 'c'"""
                CURSOR.execute(substitutep, (categ,))
                substitutedetails = CURSOR.fetchall()
                if substitutedetails == []:
                    substitutep = """SELECT idProduct, product_name, nutriscore, store, ingredients, url FROM Product WHERE Category_id = (%s) AND nutriscore = 'D' OR 'd'"""
                    CURSOR.execute(substitutep, (categ,))
                    substitutedetails = CURSOR.fetchall()
        randomalternative = random.randint(0, len(substitutedetails) - 1)
        self.substitutedetails = substitutedetails[randomalternative]
        info = [
            "Référence: ",
            "Produit: ",
            "Nutrigrade: ",
            "Où l'acheter: ",
            "Ingredients: ",
            "URL: ",
        ]
        counter = 0
        #Check if same nutrigrade between product and random substitute ==> no substitute returned
        if self.productdetailsrow[0][2] == substitutedetails[randomalternative][2]:
            print("Pas de substitut proposé car nutrigrade équivalent.")
            self.substitutedetails = []
        else:
            for productrow in substitutedetails[randomalternative]:
                print(info[counter], productrow)
                counter = counter + 1
        return self.substitutedetails

    def addalternative(self):
        '''add the recommended product to a list of substitute into the table substitute'''
        if self.substitutedetails == []:
            print("\nImpossible d'ajouter aux favoris\n")
        else:
            print("insertion....")
            insertit = """INSERT INTO Substitute(product_id, previous_id) VALUES (%s, %s)"""
            CURSOR.execute(insertit, (self.substitutedetails[0], self.productdetailsrow[0][0]))
            CONN.commit()
