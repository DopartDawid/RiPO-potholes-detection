import cv2 as cv


def video_capture(video_input=0):
    cv.namedWindow('Pottholes detection')

    # video_input = 0
    cap = cv.VideoCapture(video_input)
    while True:
        ret_val, frame = cap.read()
        if cv.waitKey(1) & 0xFF == ord('q') or ret_val is False:
            break
        cv.imshow('Pottholes detection', frame)

    cap.release()
    cv.destroyAllWindows()


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
