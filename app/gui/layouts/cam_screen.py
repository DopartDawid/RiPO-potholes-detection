from kivy.uix.screenmanager import Screen
from app.videoAnalysis.video_handler import VideoHandler
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
import cv2 as cv


class CamScreen(Screen):
    def __init__(self, **kwargs):
        super(CamScreen, self).__init__(**kwargs)
        self.img = Image()

        self.quit_btn = Button(text=" X ", pos=(.9, .9), size_hint=(.1, .1))
        self.quit_btn.bind(on_press=self.changer)

        self.add_widget(self.img)
        self.add_widget(self.quit_btn)

        self.video = None
        self.event = None

    def on_enter(self, *args):
        self.video = VideoHandler(self.manager.video_source)
        self.event = Clock.schedule_interval(self.update, 1.0/self.video.capture.get(cv.CAP_PROP_FPS))

    def update(self, dt):
        ret_val, frame = self.video.get_frame()
        if ret_val is False or frame is None:
            self.changer()
            return
        buf1 = cv.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img.texture = texture1

    def changer(self, *args):
        self.video.capture.release()
        self.event.cancel()
        self.manager.current = 'screen1'



