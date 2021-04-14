from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from app.videoAnalysis.video_handler import video_capture, get_cameras
from kivy.uix.spinner import Spinner


class MainApp(App):

    def build(self):
        screen = Screen()

        file_btn = Button(text="From file", pos=(200, 250), size_hint=(.15, .10))
        file_btn.bind(on_press=file_btn_handler)
        camera_btn = Button(text="From live camera", pos=(300, 350), size_hint=(.25, .18))
        camera_btn.bind(on_press=camera_btn_handler)

        screen.add_widget(camera_btn)
        screen.add_widget(file_btn)
        screen.add_widget(cams_spinner())

        return screen


def camera_btn_handler(self):
    video_capture()


def file_btn_handler(self):
    video_capture()


def cams_spinner():
    spinner = Spinner(text="Choose camera",
                      values=(f'Camera {cam_id}' for cam_id in get_cameras()))

    spinner.size_hint = (0.3, 0.2)
    spinner.pos_hint = {'x': .1, 'y': .8}
    return spinner
