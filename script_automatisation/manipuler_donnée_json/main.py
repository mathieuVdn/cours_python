# JSON
# Manipuler des données structurées
import json

# Personne
# nom : str
# age : int
# amis : [str]

# Paul
# 25
# Sophie, Marie, Jean

# Pierre
# 18
# Eric, Marc


personnes = {"nom": "Paul",
             "age": 25,
             "amis": ["Sophie", "Marie", "Jean"]}

#

# Sérialiser DATA - transformer TXT en json dumps

# f = open("fichier_json.txt", 'w')
# personnes_json = json.dumps(personnes)
#
# f.write(personnes_json)
#
# f.close()

# Désérialiser TXT -> JSON loads
f = open("fichier_json.txt", 'r')
donnees_json = f.read()
personne = json.loads(donnees_json)
f.close()
