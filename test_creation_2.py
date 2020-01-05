import json
import requests
from datetime import date, datetime, timedelta
import mysql.connector
from constantes import *




DICO = {1 :"aliments-et-boissons-a-base-de-vegetaux" , 2 : "aliments-d-origine-vegetale", 3 : "Snacks", 4 :"Boissons", 5:"snacks-sucres"}





mydb = mysql.connector.connect(host="localhost", database="OpenFood",
                                       user="newuser", password="monmdp")

mycursor = mydb.cursor()
research_url = "https://world.openfoodfacts.org/cgi/search.pl?search_tag=categories&search_terms=" + DICO[2]+"&json=1"
print(research_url)

r = requests.get(url=research_url)
response = r.json()
list_of_categories = []

product_name = []
nutritionscore_ofproduct = []

for a in range(20):


    try:

        product_name.append(response["products"][a]["product_name"])
        nutritionscore_ofproduct.append(response["products"][a]["nutriscore_score"])

    except KeyError:



        print("no nutriscore")
        nutritionscore_ofproduct.append(0)


print(product_name)
print(nutritionscore_ofproduct)
