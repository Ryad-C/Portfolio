#Mini jeu effectué en exercice avec Udemy

import sys

liste = []
p = ['1', '2', '3', '4', '5']

while True:
    i = input("1: Ajouter un élément à la liste de courses \n2: Retirer un élément de la liste de courses \n3: Afficher les éléments de la liste de courses \n4: Vider la liste de course \n5: Quitter le programme \nVotre choix : ")
    if i == '1':
        a = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        liste.append(a)
        print(f"L'élément {a} a bien été ajouté à la liste.")
    elif i == '2':
        r = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if r in liste:
            liste.remove(r)
            print(f"l'élément {r} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {r} n'est pas dans la liste.")
    elif i == '3':
        if not liste:
            print("Votre liste ne contient aucun élément.")
        else:
            print(f"Voici le contenu de votre liste :")
            for l, element in enumerate(liste):
                print(l+1, element)
    elif i == '4':
        liste.clear()
        print("La liste a été vidée de son contenu.")
    elif i == '5':
        print("À bientôt !")
        sys.exit()
    else:
        print("Veuillez choisir une option valide...")
    













'''
test = ['a', 'b', 'c', 'd']
for i, element in enumerate(test):
    print(i+1, element)
'''




'''
1: Ajouter un élément à la liste de courses
2: Retirer un élément de la liste de courses
3: Afficher les éléments de la liste de courses
4: Vider la liste de course
5: Quitter le programme'



'''