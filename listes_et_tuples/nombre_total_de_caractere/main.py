noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]
nb = 0

for nom in noms:
    nb += len(nom)

print(nb)

liste_nb_caractere = [len(nom) for nom in noms]

print(sum(liste_nb_caractere))

x = "".join(noms)
print(len(x))
