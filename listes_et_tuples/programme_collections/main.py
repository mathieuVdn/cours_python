# Collections : Tableaux, listes, Tuples ...
# Permet de contenir et gérer plusieurs éléments

# Tuple (): immutable -> non modifiable
# Liste []: mutable -> modifiable : rajouter/ supprimer des éléments ou les modifier

# Pourquoi utiliser des tuples alors que la liste fait la même chose et est mutable ?

# Pour des questions de performances le tuples va utiliser moins de ressources et
# donc va trouver une utilité lors de optimisation du programme

# ----------------------- TUPLES ----------------------------

# personnes = ("Mathieu", "Anastasia", "Enora", "Paul",)

# print(personnes)
# print(personnes[1])
# print(len(personnes))
# print(personnes[-1])  # -1 pour le dernier élément de la liste
#
# #
# for i in range(0, len(personnes)):
#     print(f"{personnes[i]}")
#
#

# for i in personnes:
#     print(i)
#     print(len(i))
#     print(i[1])
#
# on peut voir dans ce cas qu'une chaine de caractère se comporte littéralement comme un tuples


# ----------------------- LISTES ----------------------------
#
# personnes = ["Mathieu", "Anastasia", "Enora", "Paul"]
#
# nouvelle_personne = "Nicolas"
#
# print(personnes)
#
# personnes.append(nouvelle_personne)
# del personnes[1]
#
# print(personnes)
#
#
# def afficher_une_personne():
#     print("")
#
#
# for i in personnes:
#     print(i)
#
#
# # Fonction permettant de se rendre compte de la différence entre une liste et une variable
# def modifier_valeur(a):
#     a[1] = 10
#
#
# # test = 5
#
# test = [1, 2, 3, 4, 5]
# print(test)
#
# modifier_valeur(test)
#
# print(test)
#
# # on peut voir que la valeur reste a ca valeur d'origine
# # Pourquoi ?
# # Parce que dans la fonction modifier_valeur on réaffecte une valeur en déclarant une nouvelle variable
# # mais elle est locale a la fonction
#
# # Par contre lorsque l'on met une liste en paramètre la valeurs dans la liste est modifié
# # la raison réside dans le fait que l'on envoie un conteneur a la fonction et non une valeur


#  ---------------------------FONCTIONS ET TUPLES --------------------
#
# def obtenir_informations():
#     return "Mélanie", 37, 1.6  # retourne un Tupples


# def afficher_informations(nom, age, taille):
#     print(f"Informations \n Nom : {nom} \n Age : {age} ans \n Taille : {taille} m")
#
#
# infos = obtenir_informations()
# # print("nom : " + infos[0])
# # print("age : " + str(infos[1]))
# # print("taille : " + str(infos[2]))
#
# # nom, age, taille = obtenir_informations()  # permet de destructuré pour init les variable dans l'ordre du tuple
# afficher_informations(*infos)  # unpack tuple


#  ---------------------SLICES --------------------

personnes = ("Mathieu", "Anastasia", "Enora", "Paul", "Nicolas", "Nathalie")

# slice [start:end:step]
for i in personnes[0:2]:
    print(i)  # affiche uniquement les deux premiers index de mon tuple

# permet de aussi de pouvoir donner a l'envers le tuple grace au step

for i in personnes[::-1]:
    print(i)
