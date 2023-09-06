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
# nom : str
# age : int
# 1 - Si age == 0 
#   => Bonjour, je m'appelle Toto
#   => On affiche pas mineur
# 2 - Si nom == ""
#   => Demander nom à l'utilisateur
#   => DemanderNom(...) -> input("") -> nom
class Personne:
    espece_etre_vivant = "Humain"
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        if nom == "":
            self.DemanderNom()
        print("Constructeur personne " + self.nom)

    def SePresenter(self):

        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        info_personne = "Bonjour, je m'appelle " + self.nom
        if self.age != 0:
            info_personne += ", j'ai " + str(self.age) + " ans"

        print(info_personne)

        if self.age != 0:
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")

    def EstMajeur(self):
        return self.age >= 18

    def DemanderNom(self):
        self.nom = input("Nom de la personne : ")

    def AfficherInfosEtreVivant(self):
        print("infos être vivant" +self.espece_etre_vivant)


# --- UTILISATION ---
# personne1 = Personne("Jean", 30)   # Je cree une personne
# personne2 = Personne("Paul", 15)   # Je cree une personne

liste_personnes = [Personne("Jean", 30),
                   Personne("Paul", 15),
                   Personne("Zoé", 20)]


for personne in liste_personnes:
    personne.SePresenter()



