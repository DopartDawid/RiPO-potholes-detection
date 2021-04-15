from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from app.videoAnalysis.video_handler import get_cameras
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.file_btn = Button(text="Choose file", pos=(200, 250), size_hint=(.15, .10))
        self.file_btn.bind(on_press=self.file_btn_handler)
        self.start_btn = Button(text="Start analyze", pos=(300, 350), size_hint=(.25, .18))
        self.start_btn.bind(on_press=self.start_btn_callback)

        self.spinner = Spinner(text="Choose camera",
                               values=(f'Camera {cam_id}' for cam_id in get_cameras()),
                               size_hint=(0.3, 0.2),
                               pos_hint={'x': .1, 'y': .8})

        self.add_widget(self.start_btn)
        self.add_widget(self.file_btn)
        self.add_widget(self.spinner)

        self.popup = None

    def start_btn_callback(self, instance):
        chosen_camera_id = self.spinner.text.split()[-1]
        if self.popup is None:
            chosen_file = None
        else:
            chosen_file = self.popup.chosen_file
        if chosen_file is None:
            if chosen_camera_id.isnumeric():
                source = int(chosen_camera_id)
            else:
                source = 1
        else:
            source = chosen_file
        if self.popup is not None:
            self.popup.chosen_file = None

        self.manager.video_source = source
        self.changer()

    def file_btn_handler(self, instance):
        # self.manager.video_source = ".\proba.mp4"
        self.popup = Popup(title="File chooser",
                           size_hint=(None, None),
                           size=(400, 400),
                           auto_dismiss=False)
        self.popup.chosen_file = None
        file_chooser = FileChooser(self.popup)
        self.popup.add_widget(file_chooser)
        self.popup.open()

    def changer(self, *args):
        self.manager.current = 'screen2'


class FileChooser(FileChooserListView):
    def __init__(self, popup, **kwargs):
        super(FileChooserListView, self).__init__(**kwargs)
        self.parent_popup = popup

    def on_submit(self, selected, touch=None):
        self.parent_popup.chosen_file = selected[0]
        self.parent_popup.dismiss()
