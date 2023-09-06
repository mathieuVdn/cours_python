class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def Afficher(self):
        veggie_or_not_veggie = " - VEGETARIENNE" if self.vegetarienne else ""
        print(f"PIZZA {self.nom} : {round(self.prix, 2):.2f}€{veggie_or_not_veggie} \n{', '.join(self.ingredients)}")
        print()


class PizzaPersonalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    nb = 0

    def __init__(self):
        PizzaPersonalisee.nb += 1
        self.nb = PizzaPersonalisee.nb
        super().__init__(f'Personalisee {PizzaPersonalisee.nb}', 0, [])
        self.demander_ingredient_utilisateur()
        self.prix = self.calculer_le_prix()

    def demander_ingredient_utilisateur(self):
        while True:
            ingredient = input(f"Ajouter un ingrédient pour la pizza n°{self.nb} (ou ENTER pour terminer)")
            if ingredient == "":
                break
            self.ingredients.append(ingredient)
            print(
                f"Vous avez {len(self.ingredients)} ingrédient(s) dans la pizza {self.nb} : {' - '.join(self.ingredients)}")

    def calculer_le_prix(self):
        return PizzaPersonalisee.PRIX_DE_BASE + (len(self.ingredients) * PizzaPersonalisee.PRIX_PAR_INGREDIENT)


pizzas = [Pizza("4 fromages", 8.5, ("brie", "comté", "emmental", "parmesan"), True),
          Pizza("Margherita", 9.0, ("mozzarella", "tomates", "basilic"), True),
          Pizza("Pepperoni", 10.5, ("mozzarella", "pepperoni", "sauce tomate")),
          Pizza("Végétarienne", 8.0, ("mozzarella", "poivrons", "oignons", "champignons", "tomates"), True),
          Pizza("Hawaïenne", 11.0, ("mozzarella", "jambon", "ananas", "sauce tomate")),
          Pizza("Prosciutto", 12.0, ("mozzarella", "jambon cru", "roquette", "parmesan")),
          PizzaPersonalisee(),
          PizzaPersonalisee(),
          ]


def tri(e):
    return e.nom


# pizzas.sort(key=tri)

for pizza in pizzas:
    # if pizza.vegetarienne:
    #     pizza.Afficher()
    # if not pizza.vegetarienne:
    #     pizza.Afficher()
    # if "tomates" in pizza.ingredients:
    #     pizza.Afficher()
    # if pizza.prix < 10:
    #     pizza.Afficher(
    pizza.Afficher()
