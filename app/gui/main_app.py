from kivy.app import App
from .my_layout import MyLayout


class MainApp(App):

    def build(self):
        return MyLayout()



