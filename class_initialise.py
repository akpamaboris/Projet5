#! /usr/bin/env python3
# coding: utf-8


import mysql.connector
from mysql.connector import InterfaceError , Error
from _mysql_connector import *

class Initialise_db :


    #Initialiser

    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",
                                            user="newuser", password="monmdp")

        self.mycursor =  self.mydb.cursor()


    def initialise_database(self):



        try :


            sql = "DROP DATABASE OpenFood;"

            self.mycursor.execute(sql)

            print("The database has been deleted ")


        except mysql.connector.Error as error:
            print("Failed to delete the database : {}".format(error))



        self.mydb.close()







