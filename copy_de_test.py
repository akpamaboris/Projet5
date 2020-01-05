finished_software = False
display_favorite = False
my_accepted_answear_a = [1, 2]

while not finished_software :

    try :

        print("What do you choose ?")
        reponse_initialisation = input("    ")

    except ValueError:
        print("Valeur non authorisée ")
        continue



    if int(reponse_initialisation) == 1 :
        print("It's working")

    elif int(reponse_initialisation == 2):
        display_favorite == False
        print("2 is working")




def inputLoop(message) :
    try:

        print("What do you choose ?")
        reponse_initialisation = int(input(message))

    except ValueError:
        print("Valeur non authorisée ")

    else :
        return reponse_initialisation
