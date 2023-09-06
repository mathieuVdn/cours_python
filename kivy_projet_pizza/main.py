from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior

from storage_manager import StorageManager
from http_client import HttpClient
from modele import Pizza


class PizzaWidget(BoxLayout):
    nom = StringProperty("")
    ingredients = StringProperty("")
    prix = NumericProperty(0.0)
    vegetarienne = BooleanProperty(False)


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.pizzas = [
        #     Pizza("Carnivore", "boeuf, epinards, ail, crème", 13.99, False),
        #     Pizza("4 fromages", "Emmental, Brie, Reblochon, Bleu", 11.00, True),
        #     Pizza("Poulet champignons", "poulet, champignons, tomate, oignons", 11.5, False),
        #     Pizza("Végétarienne", "tomates, oignons, olives, poireaux", 8.5, True)
        # ]

        HttpClient().get_pizza(self.on_server_data, self.on_error)

    def on_parent(self, widget, parent):
        pizza_dict = StorageManager().load_data("pizzas")
        if pizza_dict:
            self.recycleView.data = pizza_dict

    def on_server_data(self, pizzas_dict):
        self.recycleView.data = pizzas_dict
        StorageManager().save_data("pizzas", pizzas_dict)

    def on_error(self, error):
        self.error_str = error


class PizzaApp(App):
    pass


PizzaApp().run()
