from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, WipeTransition
from .layouts.main_screen import MainScreen
from .layouts.cam_screen import CamScreen


class MainApp(App):

    def build(self):
        return LayoutManager()


class LayoutManager(FloatLayout):

    def __init__(self, **kwargs):
        super(LayoutManager, self).__init__(**kwargs)
        self.screen_manager = ScreenManager(transition=WipeTransition())
        self.add_widget(self.screen_manager)

        self.screen_manager.add_widget(MainScreen(name='screen1'))
        self.screen_manager.add_widget(CamScreen(name='screen2'))

        self.screen_manager.video_source = None
