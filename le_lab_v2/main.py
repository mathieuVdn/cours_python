from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class WidgetsExample(GridLayout):
    mon_text = StringProperty("0")
    active_count = BooleanProperty(False)
    count = NumericProperty(0)
    slider_value = StringProperty("0")
    text_input_value = StringProperty("")

    def on_button_click(self):
        if self.active_count:
            self.count += 1
            self.mon_text = str(self.count)

    def reset_count(self):
        if self.active_count:
            self.count = 0
            self.mon_text = str(self.count)

    def on_toggle_button_state(self, widget):
        print(f"toggle {widget.state}")
        if widget.state == "normal":
            print("off")
            widget.text = "Off"
            self.active_count = False
        else:
            widget.text = "On"
            self.active_count = True

    def on_switch_active(self, widget):
        print(f"switch {widget.active}")

    def on_slider_value(self, widget):
        # self.slider_value = (str(int(widget.value)))
        pass

    def on_text_validate(self, widget):
        self.text_input_value = widget.text

class LeLabV2App(App):
    pass


LeLabV2App().run()
