#! /usr/bin/env python3
# coding: utf-8


import mysql.connector

"""This class contains all the importation  of products that are essential to the application"""


class import_product_category:
    """This class imports the products"""


    def __init__(self):

        self.mydb = mysql.connector.connect(host="localhost",
                                            user="newuser", password="monmdp", database = "OpenFood")

        self.mycursor = self.mydb.cursor()


    def insert_products(self):
        add_product_id = "INSERT INTO category (category_name) VALUES ('Aliments et boissons à base de végétaux')," \
                         "('Aliments d''origine végétale'), ('Snacks'), ('Boissons'), ('Snacks sucrés')"

        data_product = ('Aliments et boissons à base de végétaux', 'Aliments d''origine végétale', 'Snacks', 'Boissons',
                        'Snacks sucrés')

        self.mycursor.execute(add_product_id)
        self.mydb.commit()





