import json
import requests
from datetime import date, datetime, timedelta
import mysql.connector
from constantes import *


url = "https://world.openfoodfacts.org/cgi/search.pl?search_tag=categories&search_terms=aliments-et-boissons-a-base-de-vegetaux&json=1"

research_url = url
r = requests.get(url=research_url)
response = r.json()
list_of_categories = []

product_name = []
nutritionscore_ofproduct = []
url_of_product = []
store_name = []

for a in range(20):

    try:

        product_name.append(response["products"][a]["product_name"])
        nutritionscore_ofproduct.append(response["products"][a]["nutriscore_score"])
        url_of_product.append(response["products"][a]["url"])



    except KeyError:

        # product_name.append(response["products"][a]["product_name"])

        print("no nutriscore, or no store")
        nutritionscore_ofproduct.append(0)



print(product_name)
print(nutritionscore_ofproduct)
print(url_of_product)
print(store_name)

