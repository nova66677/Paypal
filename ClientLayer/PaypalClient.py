from Encryption import hash_password

def print_headers() :
    print("<------------------------->")
    print("          Bienvenue        ")
    print("\n\n\n")

user_id = input("Saisissez votre UID : ")
password = input("Saisissez votre mot de passe : ")


def print_choix():
    """
    Cette fonction affiche toutes les actions réalisables par l'Utilisateur
    Elle renvoie le nombre d'actions possibles
    """
    actions = ["\t1) Consulter mes soldes", "\t2) Effectuer un virement", "\t3) Consulter l'historique"]
    print("Que souhaitez vous faire ?")
    for action in actions : 
        print(action)
    return len(actions)

def getUserChoice():
    """Cette fonction affiche les choix possibles et valide l'input Utilisateur"""
    tailleChoix = print_choix()
    choix = input("Que souhaitez vous faire ?")
    while choix not in [str(i) for i in range(1, tailleChoix+1)]:
        print("Wrong input...")
        choix, tailleChoix = getUserChoice()
    return choix, tailleChoix
    

while 1:
    choix, tailleChoix = getUserChoice()
    if choix == "1":
        print("Consulting account..")
        #consulteComptes()
    elif choix == "2":
        print("Wire preparation....")
        #effectuerVirement()
    else:
        print("Getting history...")
        #consulterHistorique()
    
    
