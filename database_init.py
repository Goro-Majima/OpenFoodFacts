import mysql.connector
import requests as req
import json
from constants import *
from classes import *

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


category_name = ["Pizzas","Conserves","Fromages","Boissons", "Snacks sucrés", "Viandes", \
    "Charcuteries", "Epicerie", "Desserts", "Surgelés", "Sauces", "Biscuits", "Chocolats",\
        "Gâteaux", "Confitures", "Apéritif", "Condiments", "Yaourts", "Pains", "Huiles"]
#category_name = ["pizzas"]
class DatabaseP:
  # Fill the tables category and product

  def fill_table_category(self):
    for name in category_name:
      categoryload = ("""INSERT INTO Category(name_category) VALUES(%s)""")
      cursor.execute(categoryload,(name,))
      conn.commit()

  def fill_table_product(self):
    idcat = 1    
    for categP in category_name:
      count = 0
      for i in range(1,20):
        url = 'https://fr.openfoodfacts.org/category/' + categP +'/' + str(i) + '.json'
        r = req.get(url)
        response_data = r.json()
        for products in response_data['products']:
          if count < 100:  
            if 'product_name' in products:
              if 'stores' in products:
                if 'nutrition_grade_fr' in products:
                  if 'url' in products:    
                    productload = """INSERT INTO Product(product_name, nutriscore, store, url, category_id) \
                        VALUES ( %s,%s,%s,%s,%s) """ 
                    #print(products['product_name'], "store: ", products['stores'],"'", products['nutrition_grade_fr'],"'", products['url'] )
                    cursor.execute(productload,(products['product_name'],products['nutrition_grade_fr'],products['stores'],products['url'], idcat))
                    conn.commit()
                    count = count + 1 
                    print(count)
      idcat = idcat + 1
      print(idcat)                 