
import mysql.connector



mydb = mysql.connector.connect(

host="localhost",user="newuser", password="monmdp", database = "Openfood"

)




mycursor = mydb.cursor()







mycursor.execute("CREATE TABLE products( category_id INTEGER UNSIGNED NOT NULL, product_name VARCHAR(90) NOT NULL,"
                 "nutrition_score INTEGER NOT NULL,product_id INTEGER UNSIGNED AUTO_INCREMENT,PRIMARY KEY (product_id),"
                 "FOREIGN KEY (category_id) REFERENCES category (category_id))ENGINE = InnoDB;")




