#! /usr/bin/env python3
# coding: utf-8



import mysql.connector




class Verify_database():

    def __init__(self):

        self.mydb =  mysql.connector.connect(host = "localhost",
                                   user = "newuser", password = "monmdp")


        self.mycursor = self.mydb.cursor()



    def verify_the_database(self):


        self.mycursor.execute("SHOW DATABASES")
        myresult = self.mycursor.fetchall()
        database_name = []

        for x in myresult:
            print(x)
            database_name.append(x)














#if "OpenFood" in str(myresult):
#    print("yes")




#print(database_name)




#sql = "INSERT INTO products (category_id , product_name, nutrion_score) VALUES (%s, %s, %s)"
#val = ('5',response["products"][a]['product_name_fr'], response["products"][a]["nutriscore_score"])

#mycursor.execute(sql, val)
#mydb.commit()

#print(mycursor.rowcount, "record inserted.")



