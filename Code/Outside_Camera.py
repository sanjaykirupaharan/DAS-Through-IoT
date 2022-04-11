import os
import cv2
import time
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook
from detections.Line import instance
from detections.Sign import sign_detect
from detections.Object import object_detection


def write_excel(name, total_duration, fps, frame_count, total_timem, total_times):
    # current date and time
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y_%H:%M:%S")

    df = pd.DataFrame({'Date': [date_time],
                       'Name': [name],
                       'Duration': [total_duration],
                       'Frames': [fps],
                       'Total Frames': [frame_count],
                       'Time Video Elapsed': [total_timem],
                       'Time Image Elapsed': [total_times]})

    writer = pd.ExcelWriter('output/output_details.xlsx', engine='openpyxl')
    # try to open an existing workbook
    writer.book = load_workbook('output/output_details.xlsx')
    # copy existing sheets
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    # read existing file
    reader = pd.read_excel('output/output_details.xlsx')
    # write out the new sheet
    df.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)

    writer.close()


# Load Line detection model
segment_image = instance.custom_segmentation()
segment_image.inferConfig(network_backbone="resnet101", num_classes=3, class_names=["BG", "straight", "dot", "cross"])
segment_image.load_model("detections/Line/mask_rcnn_model-line.h5")


def image_detection():
    images = os.listdir('images/outside')
    for image in images:
        img = cv2.imread('images/outside/' + image)

        t = time.time()

        sign_detect.detect(img)
        object_detection.detect(img)
        output = segment_image.segmentImage(img)

        cv2.imwrite('output/outside/' + image, output)

        total_times = time.time() - t

        # Write
        write_excel(image, ' ', ' ', ' ', ' ', total_times)

    print("Process finished...")


def video_detection(name):
    i = 0

    video = cv2.VideoCapture('videos/' + name)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output/outside/{}_out.avi'.format(name.split('.')[0]), fourcc, 20, (1280, 720))

    fps = int(video.get(cv2.CAP_PROP_FPS))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    total_duration = frame_count / fps
    print(fps, frame_count, total_duration)

    start_t = time.time()

    while True:
        ret, frame = video.read()
        if not ret:
            break

        print('Processing {}/{}'.format(str(i), str(frame_count)))
        i += 1

        sign_detect.detect(frame)
        object_detection.detect(frame)
        output = segment_image.segmentImage(frame)

        # out.write(output)
        output = cv2.resize(output, (960, 640))
        cv2.imshow('Frame', output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    total_timem = (time.time() - start_t) / 60

    # Write
    write_excel(name, total_duration, fps, frame_count, total_timem, ' ')

    print("Process finished...")


# image_detection()
video_detection('GH040486.mp4')
cv2.destroyAllWindows()