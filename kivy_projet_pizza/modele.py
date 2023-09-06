class Pizza:
    name = ""
    ingredients = ""
    price = 0.0
    veggie = False

    def __init__(self, name, ingredients, price, veggie):
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.veggie = veggie

    def get_data(self):
        return {"name": self.name, "ingredients": self.ingredients, "price": self.price, "veggie": self.veggie}
