import cv2 as cv


class VideoHandler:

    def __init__(self, video_source):
        self.capture = cv.VideoCapture(video_source)

    def get_frame(self):
        ret_val, frame = self.capture.read()
        return ret_val, frame


def get_cameras():
    available_cams = []
    i = 0
    while True:
        if cv.VideoCapture(i).read()[0] is not False:
            available_cams.append(i)
            i += 1
        else:
            break
    return available_cams
