#Project Udemy

#Mini jeu

import sys
import random

essais = 4
rand = random.randint(0, 100)

print("*** Le jeu du nombre mystère ***")
print("Tu dois deviner un nombre entre 0 et 100")
print("Il te reste 5 essais")
nombre = input("Devine le nombre : ")

while essais != 0:
    if not nombre.isdigit():
        print("Merci d'entrer un nombre valide.")
        nombre = input("Devine le nombre : ")
        continue
    elif rand > int(nombre):
        print(f"Le nombre mystère est plus grand que {nombre}")
        print(f"Il te reste {essais} essais")
        nombre = input("Devine le nombre : ")
    elif rand < int(nombre):
        print(f"Le nombre mystère est plus petit que {nombre}")
        print(f"Il te reste {essais} essais")
        nombre = input("Devine le nombre : ")
    elif rand == int(nombre):
        print(f"Bravo ! Le nombre mystère était bien {nombre} !")
        print(f"Tu as trouvé le nombre en {essais+1} essai(s)")
        sys.exit()
    essais -= 1
else:
    print(f"Dommage ! Le nombre mystère était {rand}")
    print("Fin du jeu.")
    sys.exit()
    
