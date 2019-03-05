import mysql.connector
import requests as req
import json
from display_db import *
from database_init import *
from connexion import *

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

class Substitution:
  def insertdb(self,element):
    # insertit = ("""INSERT INTO Substitute(product_id) VALUES (%s)""")
    # cursor.execute(insertit, (substituteDetails[randomAlternative],))
    # conn.commit()
    print(substituteDetails[randomAlternative][0])

