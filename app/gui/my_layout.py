from kivy.uix.button import Button
from app.videoAnalysis.video_handler import video_capture, get_cameras
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyLayout(FloatLayout):

    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

        self.file_btn = Button(text="From file", pos=(200, 250), size_hint=(.15, .10))
        self.file_btn.bind(on_press=self.file_btn_handler)
        self.camera_btn = Button(text="From live camera", pos=(300, 350), size_hint=(.25, .18))
        self.camera_btn.bind(on_press=self.camera_btn_callback)

        self.spinner = Spinner(text="Choose camera",
                               values=(f'Camera {cam_id}' for cam_id in get_cameras()),
                               size_hint=(0.3, 0.2),
                               pos_hint={'x': .1, 'y': .8})

        self.add_widget(self.camera_btn)
        self.add_widget(self.file_btn)
        self.add_widget(self.spinner)

    def camera_btn_callback(self, instance):
        chosen_camera_id = self.spinner.text.split()[-1]
        if chosen_camera_id.isnumeric():
            chosen_camera_id = int(chosen_camera_id)
        else:
            chosen_camera_id = 0
        print(chosen_camera_id)
        video_capture(chosen_camera_id)

    def file_btn_handler(self, instance):
        video_capture(".\proba.mp4")
