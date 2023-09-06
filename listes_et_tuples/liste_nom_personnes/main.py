# LISTES - EXERCICE : DEMANDER NOMS DE PERSONNES

noms = []
while True:
    nom = input("Quel est le nom de la personne ?")
    if nom == "":
        break
    noms.append(nom)
    print(noms)