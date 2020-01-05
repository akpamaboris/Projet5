import mysql.connector
from constantes import *
from class_initialise import *
from class_create_db import *
from class_verify_database import *
from class_create_table import *
from class_insert_product_category import *
from main6 import *
import json
import mysql.connector
from mysql.connector import  Error
from mysql.connector import errorcode
from mysql.connector import MySQLConnection, Error
import requests
from constantes import *
from main6 import *
from class_initialisation_debut import *


finished_software = False
display_favorite = False
debut_programme = Initialisation_debut()
my_accepted_answear_a = [1, 2]

while not finished_software :

    try :



        debut_programme.initialisation()
        reponse_initialisation = input("    ")
        int_reponse_init = int(reponse_initialisation)
        if int_reponse_init not in (1, 2):
            raise ValueError



    except ValueError :
        print("not a number")
        continue


    if int_reponse_init == 1 :
        try :
            print("Est ce que tu veux réinitialiser la base de donnée ?")
            print("Tape 1 pour réinitialiser , tape 2 pour continuer")
            reponse_initialisation_de_base = input("   ")
            int_reponse_initialisation_de_base = int(reponse_initialisation_de_base)

            if int_reponse_initialisation_de_base not in (1, 2):
                raise ValueError
        except ValueError:
            reponse_initialisation_de_base = 0
            print("Valeur non authorisée")


        if int_reponse_initialisation_de_base == 1 :
            # I initialise the database
            Initialisation = Initialise_db()
            Initialisation.initialise_database()

            # Create the database
            Create_the_database = Create_database()
            Create_the_database.create_database()

            # Create the tables

            Create_the_tables = Create_tables()
            Create_the_tables.create_tables()

            # Insert the categorys in category

            insert_the_categorys = import_product_category()

            insert_the_categorys.insert_products()

            url_aliments_boissons_vege = create_url(1)
            url_aliments_vegetaux = create_url(2)
            url_snacks = create_url(3)
            url_boissons = create_url(4)
            url_snacks_sucres = create_url(5)

            insert_alim_boisson_vege = InsertProduct(ID_ALIM_ET_BOISSONS_VEGE, url_aliments_boissons_vege)
            insert_alim_boisson_vege.insertion()

            insert_alim_origine_vege = InsertProduct(ID_ALIM_ORIGINE_VEGE, url_aliments_vegetaux)
            insert_alim_origine_vege.insertion()

            insert_snacks = InsertProduct(ID_SNACKS, url_snacks)
            insert_snacks.insertion()

            insert_boissons = InsertProduct(ID_BOISSONS, url_boissons)
            insert_boissons.insertion()

            insert_Snacks_Sucres = InsertProduct(ID_SNACKS_SUCRES, url_snacks_sucres)
            insert_Snacks_Sucres.insertion()


        elif int_reponse_initialisation_de_base ==2:


            print("Tapez le numéro associé à la requête de votre choix")
            print("1 - Quel est la catégorie de l'aliment que vous souhaitez  remplacer ?" + "\n")
            print("1 :", DICO[1], "\n", "2 :", DICO[2], "\n", "3 :", DICO[3], "\n", "4 :", DICO[4], "\n", "5 :",
                  DICO[5])
            response_user = input('enter value')  # I take the answear of the user

            # creation of the loop

            is_running = True

            mes_rep_accepte = (1, 2, 3, 4, 5)

            if int(response_user) in mes_rep_accepte:
                dict = select_category_product(response_user)

            print("Quel est l'ID de l'aliment que vous souhaitez remplacer")
            response_user_b = input('enter value')  # I take the answear of the user
            print("pour l'aliment avec l'id " + response_user_b + "  " + "les alternatives sont les suivantes ")

            print("the nutrition score of the aliment you selected is ", dict[int(response_user_b)][1])
            print("the name of the aliment you selected is ", dict[int(response_user_b)][0])

            print(int(response_user))

            mydb = mysql.connector.connect(host="localhost", database="OpenFood",
                                           user="newuser", password="monmdp")

            mycursor = mydb.cursor()

            final_answear = int(response_user_b)
            mycursor.execute(
                "SELECT product_name, product_id , nutrition_score FROM products  " "WHERE nutrition_score >= {} AND category_id = {}".format(
                    dict[int(response_user_b)][1], int(response_user)))

            myresult = mycursor.fetchall()

            selected_aliment_list = []
            selected_aliment_id_list = []
            selected_aliment_nutrition_score = []
            for x in myresult:
                print("name is .. ", x[0], " ", "aliment Id is .. ", x[1], " ", " nutrition score is .. ", " ", x[2])
                selected_aliment_list.append(x[0])
                selected_aliment_id_list.append(x[1])
                selected_aliment_nutrition_score.append(x[2])

            selected_dict_list = {i: [j, k] for i, j, k in zip(selected_aliment_id_list, selected_aliment_list,
                                                               selected_aliment_nutrition_score)}

            # print(selected_dict_list)
            print("Quel est l'id de l'élément que vous souhaitez remplacer")
            response_user_c = input("enter id ")
            final_answear_c = int(response_user_c)

            my_favorite = []

            for key, value in selected_dict_list.items():
                print(key, value)

                if key == final_answear_c:
                    my_favorite.append(key)
                    my_favorite.append(selected_dict_list[key])
                    # print("the key that equal it is...", key , value[0])

            print(my_favorite)

            print(my_favorite[0])
            print(my_favorite[1][0])
            print(my_favorite[1][1])

            mydb = mysql.connector.connect(host="localhost",
                                           user="newuser", password="monmdp", database="OpenFood")

            mycursor = mydb.cursor()

            add_favorite = "INSERT INTO favorites (category_id , product_name , product_id) VALUES ('{}','{}','{}')".format(
                int(response_user), my_favorite[1][0], my_favorite[1][1])

            mycursor.execute(add_favorite)
            mydb.commit()

            print("your favorite  is now registered for the category ", DICO[int(response_user)])

            mydb = mysql.connector.connect(host="localhost", database="OpenFood",
                                           user="newuser", password="monmdp")

            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM favorites  " "WHERE category_id = {}".format(int(response_user)))

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)











    elif int_reponse_init == 2 :
        display_favorite = False

        while not display_favorite :
            mydb = mysql.connector.connect(host="localhost", database="OpenFood",
                                       user="newuser", password="monmdp")
            mycursor = mydb.cursor()

            mycursor.execute("SELECT category_id, product_name FROM favorites  ")

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)
            display_favorite = True
            break




