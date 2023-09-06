from kivy.app import App

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from navigation_screen_manager import NavigationScreenManager
from canvas_example import *


class MyScreenManager(NavigationScreenManager):
    pass


class LeLabV3App(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager


LeLabV3App().run()
