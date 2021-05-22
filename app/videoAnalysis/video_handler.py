import cv2 as cv


class VideoHandler:
    def __init__(self, video_source):
        self.capture = cv.VideoCapture(video_source)
        self.pothole_cascade = cv.CascadeClassifier(
            "app/haarcascades/cascadeBigger20.xml")

    def get_frame(self):
        ret_val, frame = self.capture.read()
        return ret_val, frame

    def detect_object(self, frame):
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)

        potholes = self.pothole_cascade.detectMultiScale(frame_gray)
        for (x, y, w, h) in potholes:
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return frame


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
