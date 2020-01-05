import json
import requests
from datetime import date, datetime, timedelta
import mysql.connector
from constantes import  *
mydb =  mysql.connector.connect(host = "localhost", database = "OpenFood",
                                   user = "newuser", password = "monmdp")

mycursor = mydb.cursor()




mycursor.execute("SHOW DATABASES")


myresult = mycursor.fetchall()
database_name = []

for x in myresult:
    database_name.append(x)


if "OpenFood" in str(myresult):
    print("yes")




#print(database_name)




#sql = "INSERT INTO products (category_id , product_name, nutrion_score) VALUES (%s, %s, %s)"
#val = ('5',response["products"][a]['product_name_fr'], response["products"][a]["nutriscore_score"])

#mycursor.execute(sql, val)
#mydb.commit()

#print(mycursor.rowcount, "record inserted.")



