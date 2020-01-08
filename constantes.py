#! /usr/bin/env python3
# coding: utf-8

#Dictionary


"""This class contains all the constantes of the application"""

DICO ={1 :"aliments-et-boissons-a-base-de-vegetaux" , 2 : "aliments-d-origine-vegetale",
        3 : "Snacks", 4 :"Boissons", 5:"snacks-sucres"}


#URL
URL = "https://world.openfoodfacts.org/cgi/search.pl?search_tag=categories&search_terms="

#Json
JSON = "&json=1"

#ID

ID_ALIM_ET_BOISSONS_VEGE= 1
ID_ALIM_ORIGINE_VEGE = 2
ID_SNACKS = 3
ID_BOISSONS = 4
ID_SNACKS_SUCRES = 5



#SQL TABLES

TABLES = {}

TABLES ['category'] = (
    "CREATE TABLE category( category_id int unsigned AUTO_INCREMENT ,"
    "category_name varchar(40), PRIMARY KEY(category_id))ENGINE = InnoDB;")



TABLES ['products'] = (
    "CREATE TABLE products("
    "category_id INTEGER UNSIGNED NOT NULL, product_name VARCHAR(90) NOT NULL,"
    "nutrition_score INTEGER NOT NULL, product_id INTEGER UNSIGNED AUTO_INCREMENT,"
    "url VARCHAR(200) NOT NULL, store VARCHAR(200),"
    "PRIMARY KEY (product_id, product_name), UNIQUE (product_id, product_name), "
    "FOREIGN KEY (category_id) REFERENCES category (category_id)"
    ")ENGINE = InnoDB;")



TABLES ['favorites '] = ("CREATE TABLE favorites (category_id INTEGER UNSIGNED NOT NULL,"
                         "product_name VARCHAR(90) NOT NULL, product_id INTEGER UNSIGNED "
                         "AUTO_INCREMENT,"
                         "url VARCHAR(200) NOT NULL, store VARCHAR(200),"
                         " PRIMARY KEY (product_id, product_name) , "
                         "UNIQUE (product_id, product_name), "
                         "FOREIGN KEY (category_id) REFERENCES category (category_id)"
                         ") ENGINE = InnoDB;")