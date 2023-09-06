# PARTIE 1
# personne = {"nom": "Anastasia", "age": 39, "taille": 1.65}
# print(personne)
#
# print(personne["nom"])
# print(personne["age"])
#
# personne["nom"] = "Claire"
#
# print(personne)
#
# personne["poste"] = "Développeur"
#
# print(personne)
#
#
# achat = ("Chocolat", "beurre", "fromage")
# personne["achats"] = achat
#
# print(personne)
#
# for i in personne:
#     print(f"clef: {i} - valeur: {personne[i]}")

# PARTIE 2

# personnes = [
#     ("Mélanie", 25, 1.60),
#     ("Paul", 29, 1.80),
#     ("Jacques", 35, 1.75),
#     ("Martine", 16, 1.65),
# ]
#
#
# def obtenir_informations(nom, liste):
#     for i in liste:
#         if i[0] == nom:
#             return i
#     return None
#
#
# infos = obtenir_informations("Jacques", personnes)

# print(infos)

personnes_dic = {
    "Mélanie": (29, 1.6),
    "Paul": (25, 1.80),
    "Jacques": (35, 1.75),
    "Martine": (16, 1.65)
}

infos = personnes_dic["Jacques"]
# dans le cas ou la clé n'éxiste pas
# infos = personnes_dic["Claire"]
# Le programme renvoie une erreur
# on peut utiliser un try except
infos = personnes_dic.get("Claire")
# il renverra None et donc on peut creer des conditions
if not infos:
    print("ERREUR: La clef n'existe pas ")
else:
    print(infos)

# L'utilisation du dictionnaire dans ce cas n'est pas probante
# dans le sens ou nous avons que très peux d'éléments dans nos collections
# Dans le cas ou l'on aurait des dizaines de milliers d'entrée dans notre collection,
# L'utilisation du dictionnaire permet d'éviter de boucler
# et d'obtenir des infos directement sans boucler
