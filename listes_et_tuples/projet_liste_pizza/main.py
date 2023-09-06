# projet liste de pizza -- Niveau Débutant

pizzas = ["4 fromages", "végétarienne", "margarita", "calzone"]
vide = ()


# def tri_personalise(e):
#     return len(e)


def print_pizza(collections, n_premiers_elements=-1):
    # collections.sort(key=tri_personalise, reverse=True)
    c = collections
    if not n_premiers_elements == -1:
        c = collections[:n_premiers_elements]
    if len(c) <= 0:
        print("AUCUNE PIZZA")
        return
    print(f"---- LISTE DES PIZZAS ({len(c)} ) ----")
    for collection in c:
        print(f" Pizza {collection}")
    print()
    print(f"Première pizza : {c[0]}")
    print(f"Dernière pizza : {c[len(c) - 1]}")
    # OU
    # print(f"Dernière pizza : {collections[-1]}")


# Ajout pizza
def ajout_pizza(collections):
    user_pizza = input("Nom de la pizza a ajouter : ")
    if not pizza_existe(user_pizza, collections):
        collections.append(user_pizza)
    else:
        print('ERREUR : La pizza existe déjà')


def pizza_existe(user_pizza, collections):
    for collection in collections:
        if collection == user_pizza:
            return True
    return False


ajout_pizza(pizzas)
print_pizza(pizzas, 2)
