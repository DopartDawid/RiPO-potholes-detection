from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from app.videoAnalysis.video_handler import video_capture, get_cameras
from kivy.uix.spinner import Spinner


class CamScreen(Screen):
    def __init__(self, **kwargs):
        super(CamScreen, self).__init__(**kwargs)
        self.file_btn = Button(text="Template", pos=(200, 250), size_hint=(.15, .10))
        self.file_btn.bind(on_press=self.file_btn_handler)
        self.camera_btn = Button(text="sample text", pos=(300, 350), size_hint=(.25, .18))
        self.camera_btn.bind(on_press=self.camera_btn_callback)

        self.spinner = Spinner(text="camera",
                               values=(f'Camera {cam_id}' for cam_id in get_cameras()),
                               size_hint=(0.3, 0.2),
                               pos_hint={'x': .1, 'y': .8})

        self.add_widget(self.camera_btn)
        self.add_widget(self.file_btn)
        self.add_widget(self.spinner)

    def camera_btn_callback(self, instance):
        self.changer()

    def file_btn_handler(self, instance):
        self.changer()

    def changer(self, *args):
        self.manager.current = 'screen1'