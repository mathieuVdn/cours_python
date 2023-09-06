# LES COLLECTIONS : LISTE / TUPLES


# --------------------------------------------------------------------------------------------------------------
# -----------------------------------# Append / Extend / += / Insert -------------------------------------------
# --------------------------------------------------------------------------------------------------------------


# noms = ["Jean", "Sophie", "Martin"]
#
# noms_supplémentaires = ["Christophe", "Zoe"]
#
# # LE APPEND
#
# # noms.append(noms_supplémentaires)
# # Rajoute un tableau a l' intérieur du tableau d' origine noms ['Jean', 'Sophie', 'Martin', ['Christophe', 'Zoe']]
#
# # LA BOUCLE
#
# # for e in noms_supplémentaires:
# #     noms.append(e)
#
# # ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe']
# # Cela fonctionne mais c'est pas optimale il y a plus simple
#
# # EXTENDS
#
# # noms.extend(noms_supplémentaires)
# # ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe']
#
# # extends fonctionne comme une +=
# # noms = noms_supplémentaires + noms
# noms += noms_supplémentaires
# # INSERT
#
# print(noms)

# --------------------------------------------------------------------------------------------------------------
# -------------------------------------------------SLICE -------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------


# noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe']

# print(noms[1:3]) -> ['Sophie', 'Martin']
#

# Slice n' est pas obligé d' avoir un index [:]
# Pour autant quand on fait un slice sans index il nous renvoie la liste complète

# print(noms[:]) -> ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe']

# A quoi ca sert ??

# noms_slice = noms[:]
# noms[0] = "toto"

# print(noms) -> ['toto', 'Sophie', 'Martin', 'Christophe', 'Zoe']
# print(noms_slice) -> ['toto', 'Sophie', 'Martin', 'Christophe', 'Zoe']

# Finalement le slice sans valeur va permettre de créer une copie en mémoire du tableau
# On crée une nouvelle liste que ce soit avec un index ou non


# --------------------------------------------------------------------------------------------------------------
# -------------------------------------------------TRI -------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------


# noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe']
# #
# # noms.sort()  # in place on a pas recréer une liste on a altérer l' état de liste
# #
# # noms_tries = sorted(noms)  # On crée une nouvelle liste
#
# # on peut personnalisé le tri (par défaut A->Z, 0->infini)
#
# noms.sort(key=lambda x: len(x))
#
# print(noms)


# --------------------------------------------------------------------------------------------------------------
# ------------------------------------------MIN / MAX / IN / SUM -----------------------------------------------
# --------------------------------------------------------------------------------------------------------------


# noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe']
#
# ages = [21, 20, 30, 25, 22]
#
# # Pour des int
# # print(min(ages))  # -> 20
# # print(max(ages))  # -> 30
#
#
# # Pour des str
#
# print(min(noms))  # -> Christophe (c' est le plus bas en ordre alphabétique (C))
# print(max(noms))  # -> Zoe (c' est le plus haut en ordre alphabétique (Z))
#
# # IN
#
# # Pour les str
# # if "Martin" in noms:
# #     print("Présent")
# # else:
# #     print("Absent")
# #   -> Présent
#
# # Pour les int
#
# if 30 in ages:
#     print("Présent")
# else:
#     print("Absent")
# # -> Présent


# --------------------------------------------------------------------------------------------------------------
# ----------------------------------SWAPPER DEUX ELEMENT D' UNE LISTE ------------------------------------------
# --------------------------------------------------------------------------------------------------------------


# noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe']
#
# # Exemple je remplace les valeur
#
# # noms[0] = noms[4]
# # noms[4] = noms[0]
# #
# # print(noms)  # ->['Zoe', 'Sophie', 'Martin', 'Christophe', 'Zoe']
#
# # Cela efface jean pour le remplacer par Zoé donc dans la seconde opération noms[0]=Zoé et pas Jean
#
# # Stockez dans une variable intermédiaire
#
# # t = noms[0]
# #
# # noms[0] = noms[4]
# # noms[4] = t
# #
# # print(noms)  # -> ['Zoe', 'Sophie', 'Martin', 'Christophe', 'Jean']
#
#
# # Plus simple (Python est trop fort) on appelle ca la manière atomique (on fait tout en une seule ligne)
#
# noms[0], noms[4] = noms[4], noms[0]
#
# print(noms)  # ->['Zoe', 'Sophie', 'Martin', 'Christophe', 'Jean']

# --------------------------------------------------------------------------------------------------------------
# -------------------------------------------------JOIN ET SPLIT -----------------------------------------------
# --------------------------------------------------------------------------------------------------------------


# noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe']
#
# # Join ca veut dire rejoindre -> on va venir collé des éléments d' une collection
# #  Il va falloir lui donner une opérateur pour coller les éléments entres eux
# # Par exemple -> "-"
#
# noms_join_tiret = "-".join(noms)
# print(noms_join_tiret)  # -> Jean-Sophie-Martin-Christophe-Zoe
#
# # On pourrait mettre n' importe quel symbole ou chaine de caractère comme séparation comme par exemple ", "
#
# nom_join_virgule = ", ".join(noms)
# print(nom_join_virgule)  # -> "Jean, Sophie, Martin, Christophe, Zoe"
#
# # On a transformé une liste en chaine de caractère
#
# # Split veut dire séparer -> on va venir séparé des éléments d' une collection
# # il va prendre un point de repère dans une liste pour les enlever par exemple le ", "
#
# noms_str = "Jean, Sophie, Martin, Christophe, Zoe"
#
# noms_str_split = noms_str.split(", ")
#
# print(noms_str_split)
#
# # a l' inverse de join, on a transformer une chaine de caractère en liste


# --------------------------------------------------------------------------------------------------------------
# ------------------------------------------ INDEX / FIND / COUNT ----------------------------------------------
# --------------------------------------------------------------------------------------------------------------
#
# noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe', "Martin"]

# INDEX

# find_index = noms.index("Martin")
# print(find_index)  # -> 2 dans la liste Martin est bien a l' index 2

# ATTENTION
# Si l' élément recherché ne se trouve pas dans la liste dans ce cas on aura une erreur
# On va mettre en place un système de recherche dans la liste pour se protéger de ce genre d' erreur

# element_recherche = "dsqf"
# if element_recherche in noms:
#     print(noms.index(element_recherche))
# else:
#     print("L' élément n' est pas dans la liste")

# Si l'élement est présent plusieurs fois dans la liste dans ce cas il nous retournera le premier trouvé


# COUNT

# element_recherche = "Martin"
#
# nb_occurence = noms.count(element_recherche)
# print(f"Nombre d'occurences: {nb_occurence}")
# if nb_occurence > 0:
#     index_occurence = 0
#     for i in range(nb_occurence):
#         index_occurence = noms.index(element_recherche, index_occurence)
#         print(f"{element_recherche} touvé à l'index {index_occurence}")
#         index_occurence += 1
# else:
#     print("L' élément n' est pas dans la liste")

# FIND

# Find fonctionne uniquement sur les chaînes de caractères et non sur les collections(liste, tuple, dictionnaires


# a = 'Jean-Martin-Toto'
# i = a.find("Martin")

# print(i)  # -> 5 Martin commence bien a l' index 5
# a = 'Jean-Martin-Toto'
# i = a.find("martin")
# print(i)  # -> -1 c'est la valeur renvoyé si la recherche n' est pas présente dans la chaine de caractère

# --------------------------------------------------------------------------------------------------------------
# ---------------------------------------- LES COMPREHENSION DE LISTE ------------------------------------------
# --------------------------------------------------------------------------------------------------------------

# noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe', "Martin"]

# # Si l'on souhaite faire une liste qui reprend la liste noms mais avec les chaines de caractère mais un
# # int qui compte le nombre de caractère
# longueur_noms = []
# for nom in noms:
#     longueur_noms.append(len(nom))
# print(longueur_noms)  # -> [4, 6, 6, 10, 3, 6]
#
# # avec la compréhension de liste on peut faire cette opération en une seul ligne
#
# longueur_noms = [len(nom) for nom in noms]
# print(longueur_noms)  # -> [4, 6, 6, 10, 3, 6]


# C est un exemple de la comprehension de liste mais on peut y ajouter des conditions avant ou après

# longueur_noms = [len(nom) for nom in noms if len(nom) < 10]
# print(longueur_noms)  # -> [4, 6, 6, 3, 6]

# noms_avec_des_e = [nom for nom in noms if "e" in nom]
# print(noms_avec_des_e)  # -> ['Jean', 'Sophie', 'Christophe', 'Zoe']

# longueur_noms = [len(nom) if len(nom) < 10 else 0 for nom in noms]
# print(longueur_noms)  # -> [4, 6, 6, 0, 3, 6]

# Lorsque la condition est placer avant la compréhension de liste elle va a toujours mettre une valeur mais on peut
# conditionner la valeur d' entrer dans la liste

# a = [i for i in range(20) if (i // 2) * 2 != i]
#
# print(a)

# (i // 2) * 2 == i] -> permet de retrouver les chiffres pairs

# b = [(i, True if (i // 2) * 2 == i else False) for i in range(20)]
# print(b)


# --------------------------------------------------------------------------------------------------------------
# ------------------------------------------------ ANY ET ALL --------------------------------------------------
# --------------------------------------------------------------------------------------------------------------


# noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe', "Martin"]

a = [True, False, False, True]
# print(any(a))  # -> True

# Any renvoie True car il va rechercher dans une liste si AU MOINS un élément est True alors il renvoie TRUE
# Si tous les éléments sont False il renverra False

b = [True, False, False, True]
# print(all(b))  # -> False

# A l' inverse all renvoie True uniquement si TOUS les éléments sont true
# Donc si un élément de la liste est false dans ce cas il renverra False

# Cela peut servir avec notre liste de noms pour detecter si un des noms contient une quelconque lettre

# Version de base avec une boucle

# found = False
# for nom in noms:
#     if "z" in nom.lower():
#         found = True
#         break
#
# if found:
#     print("Trouvé")
# else:
#     print("Non trouvé")

# noms_avec_un_z_existe = any([True if "z" in nom.lower() else False for nom in noms])
#
# if noms_avec_un_z_existe:
#     print("Trouvé")
# else:
#     print("Non trouvé")


# --------------------------------------------------------------------------------------------------------------
# ------------------------------------------------ ANY ET ALL --------------------------------------------------
# --------------------------------------------------------------------------------------------------------------

noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe']


def element_dans_la_liste(e, l):
    insensible_casse = [nom.lower() for nom in l]
    return e.lower() in insensible_casse


if element_dans_la_liste("jeaN", noms):
    print("Jean est la")
else:
    print("Jean n'est pas la")
