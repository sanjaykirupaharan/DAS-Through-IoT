import cv2 as cv
import mediapipe as mp
import time
import detections.Drowsiness.utils as utils
import math
import numpy as np
import playsound
import os
from twilio.rest import Client

# variables
frame_counter = 0
CEF_COUNTER = 0

# constants
CLOSED_EYES_FRAME = 70
FONTS = cv.FONT_HERSHEY_COMPLEX

# Left eyes indices
LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]

# right eyes indices
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]

map_face_mesh = mp.solutions.face_mesh


# landmark detection function
def landmarksDetection(img, results, draw=False):
    img_height, img_width = img.shape[:2]

    mesh_coord = [(int(point.x * img_width), int(point.y * img_height)) for point in
                  results.multi_face_landmarks[0].landmark]
    if draw:
        [cv.circle(img, p, 2, (0, 255, 0), -1) for p in mesh_coord]

    # returning the list of tuples for each landmarks
    return mesh_coord


# Euclaidean distance
def euclaideanDistance(point, point1):
    x, y = point
    x1, y1 = point1
    distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    return distance


# Blinking Ratio
def blinkRatio(img, landmarks, right_indices, left_indices):
    # Right eyes
    # horizontal line
    rh_right = landmarks[right_indices[0]]
    rh_left = landmarks[right_indices[8]]
    # vertical line
    rv_top = landmarks[right_indices[12]]
    rv_bottom = landmarks[right_indices[4]]

    # LEFT_EYE
    # horizontal line
    lh_right = landmarks[left_indices[0]]
    lh_left = landmarks[left_indices[8]]

    # vertical line
    lv_top = landmarks[left_indices[12]]
    lv_bottom = landmarks[left_indices[4]]

    rhDistance = euclaideanDistance(rh_right, rh_left)
    rvDistance = euclaideanDistance(rv_top, rv_bottom)

    lvDistance = euclaideanDistance(lv_top, lv_bottom)
    lhDistance = euclaideanDistance(lh_right, lh_left)

    reRatio = rhDistance / rvDistance
    leRatio = lhDistance / lvDistance

    ratio = (reRatio + leRatio) / 2
    return ratio


def sound_alarm(path):
    # play an alarm sound
    playsound.playsound(path)


def message():
    # Through Twilio send a message and make a call
    account_sid = "AC13105bbd4e802e2b2022dadb2e342a3f"  # Put your Twilio account SID here
    auth_token = "ba7d3f9a392eed50c84d91e2ea243931"  # Put your auth token here

    client = Client(account_sid, auth_token)

    # Send a message
    message = client.api.account.messages.create(
        to="+94765266417",  # Put your cellphone number here
        from_="+17755229292",  # Put your Twilio number here
        body="Driver is Sleeping....")
    print("[INFO] sending message...")


def pipeline(frame):
    global CEF_COUNTER
    with map_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:

        #  resizing frame
        frame = cv.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv.INTER_CUBIC)
        frame_height, frame_width = frame.shape[:2]
        rgb_frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        results = face_mesh.process(rgb_frame)
        if results.multi_face_landmarks:
            mesh_coords = landmarksDetection(frame, results, False)
            ratio = blinkRatio(frame, mesh_coords, RIGHT_EYE, LEFT_EYE)

            utils.colorBackgroundText(frame, f'Ratio : {round(ratio, 2)}', FONTS, 0.7, (30, 100), 2, utils.PINK,
                                      utils.YELLOW)

            if ratio > 3.5:
                CEF_COUNTER += 1

                if CEF_COUNTER <= 25:
                    utils.colorBackgroundText(frame, f'1', FONTS, 5, (430, 200), 6, utils.WHITE, utils.RED, pad_x=4,
                                              pad_y=6, )
                elif CEF_COUNTER <= 50:
                    utils.colorBackgroundText(frame, f'2', FONTS, 5, (430, 200), 6, utils.WHITE, utils.RED, pad_x=4,
                                              pad_y=6, )
                elif CEF_COUNTER <= CLOSED_EYES_FRAME:
                    utils.colorBackgroundText(frame, f'3', FONTS, 5, (430, 200), 6, utils.WHITE, utils.RED, pad_x=4,
                                              pad_y=6, )
                if CEF_COUNTER > CLOSED_EYES_FRAME:
                    utils.colorBackgroundText(frame, f'Drowsiness Alert...', FONTS, 1.7, (250, 150),
                                              2, utils.YELLOW, pad_x=4, pad_y=6, )
                    sound_alarm('warning.mp3')
                    message()

            else:
                CEF_COUNTER = 0

            cv.polylines(frame, [np.array([mesh_coords[p] for p in LEFT_EYE], dtype=np.int32)], True, utils.GREEN, 1,
                         cv.LINE_AA)
            cv.polylines(frame, [np.array([mesh_coords[p] for p in RIGHT_EYE], dtype=np.int32)], True, utils.GREEN, 1,
                         cv.LINE_AA)

    return frame

"""
video = cv.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break

    out = pipeline(frame)
    out = cv.resize(out, (1280, 720))
    cv.imshow("Frame", out)
    cv.waitKey(1)
"""
