###
# VOS PREMIERS PAS EN POO (PROGRAMMATION ORIENTÉE OBJET)
###
# - Différence programmation impérative / objet
# - Le plus simple possible
# - Exercices, mises en situation

# Personne  (entité -> class)
#    Données : nom, age
#    Actions :  (méthodes)
#       - SePresenter()
#       - DemanderNom() / input
#  [Personne "Jean"]     [Personne "Paul"]


# --- DEFINITION ---
class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        if nom == "":
            nom = input("Quel est votre nom ?")
        self.nom = nom  # crée une variable d'instance : nom
        if age == 0:
            age = int(input("Quel est votre age ?"))
        self.age = age

    def SePresenter(self):
        if self.age == 0:
            return print(f"Je m'appelle {self.nom}")
        print(f"Bonjour, je m'appelle {self.nom}, j'ai {self.age} ans")
        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")

    def EstMajeur(self):
        return self.age >= 18


# --- UTILISATION ---
personne1 = Personne("Jean", 12)  # Je cree une personne
personne2 = Personne("Paul", 25)  # Je cree une personne
personne3 = Personne()
# Personne.SePresenter(personne1)
personne1.SePresenter()
personne2.SePresenter()  # méthode d'instance
personne3.SePresenter()

"""def afficher_informations_personne(nom, age):
    print(f"La personne s'appelle {nom}, son age est {age} ans")

def demanger_nom_personne():
    nom = input("Quel est votre nom ?")
    return nom

nom1 = "Jean"
age1 = 30

nom2 = "Paul"
age2 = 25

afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)

nom3 = demanger_nom_personne()
age3 = 18
afficher_informations_personne(nom3, age3)"""
