

import mysql.connector


class Create_database :


    #Initialiser

    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",
                                            user="newuser", password="monmdp")

        self.mycursor =  self.mydb.cursor()


    def create_database(self):


        try :


            sql = "CREATE DATABASE OpenFood;"

            self.mycursor.execute(sql)

            print("Database Created ")


        except mysql.connector.Error as error:
            print("Failed to create the database : {}".format(error))


        self.mydb.close()







