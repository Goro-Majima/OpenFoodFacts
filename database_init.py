"""file used to fill the table category and product at initialization """
import json
import mysql.connector
import requests as req
from display_db import *
from connexion import *


CONNECT = Connect()
CONNECT.connecttodb()

CATEGORYNAME = [
    "Pizzas",
    "Conserves",
    "Fromages",
    "Boissons",
    "Snacks sucrés",
    "Viandes",
    "Charcuteries",
    "Epicerie",
    "Desserts",
    "Surgelés",
    "Sauces",
    "Biscuits",
    "Chocolats",
    "Gâteaux",
    "Confitures",
    "Apéritif",
    "Condiments",
    "Yaourts",
    "Pains",
    "Huiles",
]


class DatabaseP:
    """ Fill the tables category and product"""

    def fill_table_category(self):
        """fill category table"""
        for name in CATEGORYNAME:
            categoryload = """INSERT INTO Category(name_category) VALUES(%s)"""
            CURSOR.execute(categoryload, (name,))
            # Make sure data is committed to the database
            CONN.commit()

    def fill_table_product(self):
        """Getting the data from the json url, the loop is going through \
          each page of each category. 50 product per category(20)"""
        idcat = 1
        for categp in CATEGORYNAME:
            count = 0
            for i in range(1, 20):
                url = (
                    "https://fr.openfoodfacts.org/category/"
                    + categp
                    + "/"
                    + str(i)
                    + ".json"
                )
                extract = req.get(url)
                response_data = extract.json()
                for products in response_data["products"]:
                    if count < 50:
                        if "product_name" in products:
                            if "stores" in products:
                                if "ingredients_text_debug" in products:
                                    if "nutrition_grade_fr" in products:
                                        if "url" in products:
                                            productload = """INSERT INTO Product(product_name, nutriscore, \
                                            store, ingredients, url, category_id) VALUES ( %s,%s,%s,%s,%s,%s) """
                                            CURSOR.execute(
                                                productload,
                                                (
                                                    products["product_name"],
                                                    products["nutrition_grade_fr"],
                                                    products["stores"],
                                                    products["ingredients_text_debug"],
                                                    products["url"],
                                                    idcat,
                                                ),
                                            )
                                            CONN.commit()
                                            count = count + 1
                                            print(count)
            idcat = idcat + 1
            print(idcat)
