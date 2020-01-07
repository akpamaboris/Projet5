#! /usr/bin/env python3
# coding: utf-8

import requests
import mysql.connector
from constantes import *







class InsertProduct:
    #variables





    def __init__(self,id,url):
        self.id = id
        self.url = url





    def insertion (self):
        mydb = mysql.connector.connect(host="localhost", database="OpenFood",
                                       user="newuser", password="monmdp")

        mycursor = mydb.cursor()
        research_url = self.url
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
                if store_name.append(response["products"][a]["stores"]) == True:
                    store_name.append(response["products"][a]["stores"])
                else:
                    store_name.append("No Store")

            except KeyError:

                #product_name.append(response["products"][a]["product_name"])

                print("no nutriscore")
                nutritionscore_ofproduct.append("0")







        for a in range(20):

            try:
                sql = "INSERT INTO products (category_id , product_name, nutrition_score, url , store ) VALUES (%s, %s, %s ,%s ,%s)"
                val = (self.id, product_name[a], nutritionscore_ofproduct[a], url_of_product[a] ,store_name[a])

                mycursor.execute(sql, val)
                mydb.commit()

                print(mycursor.rowcount, "record inserted.")

            except IndexError :
                store_of_product= 'null'

    def create_url(id):

        final_url = URL + DICO[id] + JSON
        return final_url

    def select_category_product(id):
        mydb = mysql.connector.connect(host="localhost", database="OpenFood",
                                       user="newuser", password="monmdp")

        mycursor = mydb.cursor()

        request_user = int(id)
        mycursor.execute(
            "SELECT product_name, product_id , nutrition_score, url , store FROM products  " "WHERE category_id = {}".format(
                int(id)))

        myresult = mycursor.fetchall()
        aliment_list = []
        aliment_id_list = []
        aliment_nutrition_score = []
        aliment_url = []
        aliment_store = []

        for x in myresult:
            print("Alim => " + x[0] + " ID => " + str(x[1]) + " SCORE => " + str(x[2]) + " URL  => " + str(
                x[3]) + " STORE =>" + str(x[4]))
            aliment_list.append(x[0])
            aliment_id_list.append(x[1])
            aliment_nutrition_score.append(x[2])
            aliment_url.append(x[3])
            aliment_store.append(x[4])

        dict_list = {i: [j, k, l, m] for i, j, k, l, m in
                     zip(aliment_id_list, aliment_list, aliment_nutrition_score, aliment_url, aliment_store)}

        return dict_list


    def insert_favorites (reponse_user , my_favorite):
        mydb = mysql.connector.connect(host="localhost",
                                       user="newuser", password="monmdp", database="OpenFood")

        mycursor = mydb.cursor()

        add_favorite = "INSERT INTO favorites (category_id , product_name , product_id , url) VALUES ('{}','{}','{}', '{}')".format(
            int(reponse_user), my_favorite[1][0], my_favorite[1][1], my_favorite[1][2])

        mycursor.execute(add_favorite)
        mydb.commit()

        print("ton favoris est bien enregistré ", "\n")



    def select_favorites (self):

        mydb = mysql.connector.connect(host="localhost", database="OpenFood",
                                       user="newuser", password="monmdp")
        mycursor = mydb.cursor()

        mycursor.execute("SELECT category_id, product_name FROM favorites  ")

        myresult = mycursor.fetchall()

        for x in myresult:

            if mycursor.rowcount > 0 :
                print(x)

            else :
                print("Pas encore de favoris, ajoutez en")






















