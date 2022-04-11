import cv2
from detections.Drowsiness import drowsiness


########Drowsiness detection#######
def detect_drowsy(img):
    out = drowsiness.pipeline(frame=img)
    return out


def image_detection():
    img = cv2.imread('images/eye_close.png')
    out = detect_drowsy(img)
    cv2.imshow("Frame", out)
    cv2.waitKey(0)


def video_detection():
    video = cv2.VideoCapture(0)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        out = detect_drowsy(frame)
        out = cv2.resize(out, (1280, 720))
        cv2.imshow("Frame", out)
        cv2.waitKey(1)


video_detection()
