# OpenFoodFacts
The goal is to create an interactive program connected to the database Open Food Facts. It can gather food products, compare them and recommand a healthier substitute to the user. The app will be created for french consumers only.

The database will be displayed on the commande prompt and user can choose the action he wants by typing a number.

## Specifications
The user is on terminal. The following choices are displayed:

1- Which product would you like to switch ?
2- Get my substituted products.

###User choose 1: 
- Display of 20 categories.
- The program ask you to select a category. If input not an integer or out of range, display of error message.
- User select a category.
- Display of 50 products of the category.
- The program ask you to select a product. If input not an integer or out of range, display of error message.
- User select a product.
- Display of the products details such as id, name, nutrigrade, store, ingredients and url.
- Display of the substitute below the chosen one with same details.
- No substitute if same or not better nutrigrade.
- User is able to save it or not in his favorites.
- Possibility to be back to the menu list or leave.

##User choose 2:
- If nothing in favorite user base, message instead of db.
- Display of favorite/"bad" product with their respective details.
- Ordered by time (Last on list is recorded last)
- Possibility to be back to the menu list or leave.

## Functions and modules

Product search in the database Open Food Facts.
User interact with the program through the terminal.
If user's input is other than a number, the program repeats the question.
The search is based on database Mysql.

Main program: purebeurre.py (start the app from this file)

Classes files:  connexion.py     ===> class Connect. File used to log the user to the database in order to interact with it.
                database_init.py ===> class Database. extract data from an url in json format and fill them into table.
                display_db.py    ===> classes Userintro, Displaydb. Regroup functions that display all datas from the local base according, also insert substitutes.
                insert_favorite  ===> class Displaysub. Insert an alternative product in table substitute as favorite.

venv file: Virtual environment needed for each project in order to keep the already installed versions packages in your system stable.

requirements.txt: file needed to manage required packages for the project.

bdd off.mwb: Schema of the db created, represented with related tables, its fields, primary and foreign keys.

scriptstables.sql: SQL Script related to the database created.

##How to use it ?

##Package management:
- Download mysql server
- install a text editor such as sublime text 3 or Visual studio code
- install python 3.7 on your text editor 
- Create a virtual environment and requirements.txt from the command line
- Install package mysql connector - python
- Install package requests

- Clone the repository or copy the url 
- Set the database from the command line:
- set path(try "set PATH=%PATH%;C:\"Program Files"\MySQL\"MySQL Server 8.0"\bin")
- Create the database by using scriptstables.sql through its path. 
- Use the id and password you set when you installed mysql
- Create a new user with user= "student" and password = 'mot_de_passe'. If you want to use other word, also change in all files.
- Grant all privilege to this user for this db. 

- open with the text editor and execute purebeurre.py






