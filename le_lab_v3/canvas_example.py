from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("canvas_example.kv")


class CanvasExample1(Widget):
    pass


class CanvasExample2(Widget):
    pass


class CanvasExample3(Widget):
    pass


class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0, 1)
            Line(points=(dp(100), dp(300), dp(400), dp(500)), width=dp(2))
            Line(circle=(dp(400), dp(400), dp(80)), width=dp(2))
            Line(rectangle=(dp(600), dp(400), dp(150), dp(100)), width=dp(2))
            self.rect = Rectangle(pos=(220, 0), size=(dp(200), dp(100)))

    def on_button_press(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        movement_speed = dp(20)
        diff = self.width - (x + w)
        if diff < movement_speed:
            movement_speed = diff
        x += movement_speed
        self.rect.pos = (x, y)

    def on_button_reset(self):
        self.rect.pos = (220, 0)


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            self.ball = Ellipse(pos=(dp(100), (dp(100))), size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1 / 60)

    def on_size(self, *args):
        self.ball.pos = self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2

    def update(self, dt):
        x, y = self.ball.pos
        diff_y = self.height - (y + self.ball_size)
        diff_x = self.width - (x + self.ball_size)

        if (y + self.ball_size) > self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy

        if (x + self.ball_size) > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx

        if y < 0:
            y = 0
            self.vy = abs(self.vy)

        if x < 0:
            x = 0
            self.vx = abs(self.vx)

        x += self.vx
        y += self.vy
        self.ball.pos = (x, y)


class CanvasExample6(Widget):
    pass


class CanvasExample7(BoxLayout):
    pass


class CanvasTab(TabbedPanel):
    pass
