# on import les modules
# on définit les variables vies user et bot
# on souhaite la bienvenue à l'utilisateur
# On créait une boucle while true: pour tous englober le code
# On commence le combat avec un choix pour l'utilisateur, il peut soit attaquer, soit se redonner des pv
# On random l'attaque du bot
# on fait un point sur les pv des 2 avec les f-string
# on met un if pv_user ou _bot == 0: on end la partie avec une petit message si user gagne un dit gg si il perd, on pleure

import time
import random
import sys
vies_user = 10
vies_bot = 10
print("Bienvenue sur ce jeu de combat. Le but de ce jeu est d'être le dernier survivant de ces combats effroyables. \nLors de votre tour, vous avez le choix entre : \n- 'attaquer' : Permet d'attaquer votre adversaire\n- 'défendre' : Permet de récupérer des pv via une potion")
while True:
    choix = input("Souhaitez-vous attaquer ou défendre : ")
    if choix == "défendre":
        addpv = random.randint(-2, 3)
        vies_user += addpv
        if addpv < 0:
            print(f"Quel dommage, vous avez pris une potion de poison. Vous perdez {abs(addpv)} pv")
            time.sleep(2)
        else:
            print(f"Vous regagnez {addpv} pv")
            time.sleep(2)
            addpvbot = random.randint(1, 4)
            print(f"Votre adversaire aussi en profite pour récupérer des pv. Il vient d'en regagner {abs(addpvbot)}")
            vies_bot += addpvbot
            time.sleep(2)
    
    # elif choix == "cheat-code":
        # attaque = random.randint(5, 20)
        # vies_bot -= attaque
        # print(f"Bravo, vous avez infligé {attaque} dégâts à votre adversaire")
        # time.sleep(2)
    elif choix == "attaquer":
        attaque = random.randint(1, 3)
        vies_bot -= attaque
        print(f"Félicitations, vous avez infligé {attaque} dégât(s) à votre adversaire")
        time.sleep(2)
        if attaque > 1:
            removepv = random.randint(2, 5)
            vies_user -= removepv
            print(f"Ahhhh, votre adversaire vous inflige un coût critique. Vous perdez {abs(removepv)} pv")
            time.sleep(2)
    else:
        print("Choix invalide. Veuillez choisir 'attaquer' ou 'défendre'.")
        time.sleep(2)
    if vies_user <= 0:
        print("Vous avez perdu. Votre adversaire a gagné.")
        sys.exit()
    elif vies_bot <= 0:
        print("Félicitations ! Vous avez vaincu votre adversaire.")
        sys.exit()
    print(f"Vos points de vie : {vies_user} | Points de vie de l'adversaire : {vies_bot}")
