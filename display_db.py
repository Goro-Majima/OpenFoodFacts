'''Regroup functions that display all datas from the local base according, also insert substitutes'''
import random
import mysql.connector

try:
    CONN = mysql.connector.connect(
        host="localhost",
        user="student",
        password="mot_de_passe",
        database="pure_beurre",
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

CURSOR = CONN.cursor()


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
        if self.productdetailsrow[0][2] == substitutedetails[randomalternative][2]:
            print("Pas de substitut proposé car nutrigrade équivalent")
        else:
            for productrow in substitutedetails[randomalternative]:
                print(info[counter], productrow)
                counter = counter + 1
            print(substitutedetails[randomalternative][0])
        
        return self.substitutedetails

    def addalternative(self):
        '''add the recommended product to a list of substitute into the table substitute'''
        print(self.substitutedetails[0])
        insertit = """INSERT INTO Substitute(product_id, previous_id) VALUES (%s, %s)"""
        CURSOR.execute(insertit, (self.substitutedetails[0], self.productdetailsrow[0][0]))
        CONN.commit()
