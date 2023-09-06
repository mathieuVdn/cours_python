# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
noms = []
nombre_de_personne = 0

noms.append(input("nom de la personne 1 : "))
noms.append(input("nom de la personne 2 : "))
noms.append(input("nom de la personne 3 : "))

listes = []

for nom in noms:
    listes.append(Personne(nom))

for personnes in l:
    p.SePresenter()