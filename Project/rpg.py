#Project Udemy

#Mini jeu

import sys
import random

player_health = 50
ennemy_health = 50
potion = 3
phrase = "Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "

while player_health > 0 or ennemy_health > 0: 
    menu = input(phrase)
    if int(menu) == 1: #attaquer
        attack = random.randint(5, 10) #joueur attaque
        ennemy_health = ennemy_health - attack
        print(f"Vous avez infligé {attack} points de dégats à l'ennemi ⚔️")
        if ennemy_health <= 0: #ennemi mort
            print("Vous avez gagné !")
            print("Fin du jeu.")
            sys.exit()
        attack_ennemy = random.randint(5, 15) #ennemi attaque
        player_health = player_health - attack_ennemy
        print(f"L'ennemi vous a infligé {attack_ennemy} points de dégats ⚔️")
        if player_health <= 0: #joueur mort
            print("Vous avez perdu ...")
            print("Fin du jeu.")
            sys.exit()
        print(f"Il vous reste {player_health} point{'s' if player_health > 1 else ''} de vie")
        print(f"Il reste {ennemy_health} point{'s' if ennemy_health > 1 else ''} à l'ennemi")
        print("--------------------------------------------------")
    elif int(menu) == 2: #utiliser potion
        if potion > 0:
            potion_health = random.randint(15, 50) #joueur se soigne
            potion -= 1
            player_health = player_health + potion_health
            print(f"Vous récupérez {potion_health} points de vie ❤️ ({potion} restante{'s' if potion > 1 else ''})")
            attack_ennemy = random.randint(5, 15) #ennemi attaque
            player_health = player_health - attack_ennemy
            print(f"L'ennemi vous a infligé {attack_ennemy} points de dégats ⚔️")
            if player_health <= 0: #joueur mort
                print("Vous avez perdu ...")
                print("Fin du jeu.")
                sys.exit()
            print(f"Il vous reste {player_health} point{'s' if player_health > 1 else ''} de vie")
            print(f"Il reste {ennemy_health} point{'s' if ennemy_health > 1 else ''} à l'ennemi")
            print("--------------------------------------------------")
            print("Vous passez votre tour ...")
            attack_ennemy = random.randint(5, 15) #ennemi attaque
            player_health = player_health - attack_ennemy
            print(f"L'ennemi vous a infligé {attack_ennemy} points de dégats ⚔️")
            if player_health <= 0: #joueur mort
                print("Vous avez perdu ...")
                print("Fin du jeu.")
                sys.exit()
            print(f"Il vous reste {player_health} point{'s' if player_health > 1 else ''} de vie")
            print(f"Il reste {ennemy_health} point{'s' if ennemy_health > 1 else ''} à l'ennemi")
            print("--------------------------------------------------")
        elif potion == 0:
            print("Vous n'avez plus de potions ...")
    else:
        menu = input(phrase)
        continue








