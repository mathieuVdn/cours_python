# LISTES - ALGO : VALEUR LA PLUS PETITE

distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]
nom_chauffeur = ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]

distance_min = distance_chauffeur_km[0]

index_min = 0
for index, distance in enumerate(distance_chauffeur_km) :
    if distance < distance_min:
        distance_min = distance
        index_min = index

nom_chauffeur_min = nom_chauffeur[index_min]
print("La distance minimale est", distance_min, "km")
print("L'index minimale est", type(index_min))
print("Le chauffeur est", nom_chauffeur_min)

