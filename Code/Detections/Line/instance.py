import cv2
import numpy as np
import random
import os
import math
from detections.Line.mask_rcnn import MaskRCNN
from detections.Line.config import Config
import colorsys
import time
from datetime import datetime
import imantics
from imantics import Polygons, Mask
import tensorflow as tf
from pathlib import Path
import matplotlib.pyplot as plt


class configuration(Config):
    NAME = "configuration"


coco_config = configuration(BACKBONE="resnet101", NUM_CLASSES=81, class_names=["BG"], IMAGES_PER_GPU=1,
                            DETECTION_MIN_CONFIDENCE=0.7, IMAGE_MAX_DIM=1024, IMAGE_MIN_DIM=800,
                            IMAGE_RESIZE_MODE="square", GPU_COUNT=1)


class custom_segmentation:
    def __init__(self):
        self.model_dir = os.getcwd()

    def inferConfig(self, name=None, network_backbone="resnet101", num_classes=1, class_names=["BG"], batch_size=1,
                    detection_threshold=0.7,
                    image_max_dim=512, image_min_dim=512, image_resize_mode="square", gpu_count=1):
        self.config = Config(BACKBONE=network_backbone, NUM_CLASSES=1 + num_classes, class_names=class_names,
                             IMAGES_PER_GPU=batch_size, IMAGE_MAX_DIM=image_max_dim, IMAGE_MIN_DIM=image_min_dim,
                             DETECTION_MIN_CONFIDENCE=detection_threshold,
                             IMAGE_RESIZE_MODE=image_resize_mode, GPU_COUNT=gpu_count)

    def load_model(self, model_path):
        # load the weights for COCO
        self.model = MaskRCNN(mode="inference", model_dir=self.model_dir, config=self.config)
        self.model.load_weights(model_path, by_name=True)

    def segmentImage(self, image, show_bboxes=False, extract_segmented_objects=False,
                     save_extracted_objects=False, mask_points_values=False, output_image_name=None,
                     text_thickness=1, text_size=1, box_thickness=2, verbose=None):

        #image = cv2.imread(image_path)

        new_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Run detection
        if verbose is not None:
            print("Processing image...")
        results = self.model.detect([new_img])

        r = results[0]

        output, detections = display_box_instances(image, r['rois'], r['masks'], r['class_ids'],
                                                   self.config.class_names,
                                                   r['scores'],
                                                   text_thickness=text_thickness, text_size=text_size,
                                                   box_thickness=box_thickness)
        ####Alert system
        for detection in detections:
            if detection[-1] != 'dot':
                boxes = detection[:4]
                # print(boxes)
                y1, x1, y2, x2 = boxes
                if x1 > x2:
                    status = warning(x1)
                else:
                    status = warning(x2)
                if status:
                    output = cv2.putText(output, "Do not overtake...", (1000, 250), cv2.FONT_HERSHEY_SIMPLEX, 6,
                                         (0, 0, 255), 8)

        output = cv2.resize(output, (1280, 720))
        return output


################VISUALIZATION CODE ##################


def random_colors(N, bright=True):
    """
    Generate random colors.
    To get visually distinct colors, generate them in HSV space then
    convert to RGB.
    """
    brightness = 1.0 if bright else 0.7
    hsv = [(i / N, 1, brightness) for i in range(N)]
    colors = list(map(lambda c: colorsys.hsv_to_rgb(*c), hsv))
    random.shuffle(colors)
    return colors


def apply_mask(image, mask, color, alpha=0.5):
    """Apply the given mask to the image.
    """

    for c in range(3):
        image[:, :, c] = np.where(mask == 1, image[:, :, c] * (1 - alpha) + alpha * color[c] * 255, image[:, :, c])

    return image


def display_box_instances(image, boxes, masks, class_ids, class_name, scores, text_size, box_thickness, text_thickness):
    detection = []
    assert boxes.shape[0] == masks.shape[-1] == class_ids.shape[0]

    for i in range(boxes.shape[0]):
        if not np.any(boxes[i]):
            continue

        y1, x1, y2, x2 = boxes[i]
        label = class_name[class_ids[i]]

        # append the x,y values along with the label

        xy = list(boxes[i])
        xy.append(label)
        detection.append(xy)

        for i in range(len(class_ids)):
            mask = masks[:, :, i]
            label = class_name[class_ids[i]]
            if label == 'dot':
                color = (0.0, 0.0, 1.0)
            elif label == 'straight':
                color = (1.0, 0.0, 0.0)
            elif label == 'cross':
                color = (0.0, 1.0, 1.0)
            else:
                color = (0.0, 0.0, 0.0)
            image = apply_mask(image, mask, color)

        #image = cv2.putText(image, caption, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, text_size, txt_color, text_thickness)
    return image, detection


def warning(x):
    warn = False
    if 2000 < x < 2200:
        warn = True
    return warn


def colorBackgroundText(img, text, font, fontScale, textPos, textThickness=1, textColor=(0, 255, 0), bgColor=(0, 0, 0),
                        pad_x=3, pad_y=3):
    """
    Draws text with background, with  control transparency
    @param img:(mat) which you want to draw text
    @param text: (string) text you want draw
    @param font: fonts face, like FONT_HERSHEY_COMPLEX, FONT_HERSHEY_PLAIN etc.
    @param fontScale: (double) the size of text, how big it should be.
    @param textPos: tuple(x,y) position where you want to draw text
    @param textThickness:(int) fonts weight, how bold it should be
    @param textPos: tuple(x,y) position where you want to draw text
    @param textThickness:(int) fonts weight, how bold it should be.
    @param textColor: tuple(BGR), values -->0 to 255 each
    @param bgColor: tuple(BGR), values -->0 to 255 each
    @param pad_x: int(pixels)  padding of in x direction
    @param pad_y: int(pixels) 1 to 1.0 (), controls transparency of  text background
    @return: img(mat) with draw with background
    """
    (t_w, t_h), _ = cv2.getTextSize(text, font, fontScale, textThickness)  # getting the text size
    x, y = textPos
    cv2.rectangle(img, (x - pad_x, y + pad_y), (x + t_w + pad_x, y - t_h - pad_y), bgColor, -1)  # draw rectangle
    cv2.putText(img, text, textPos, font, fontScale, textColor, textThickness)  # draw in text

    return img
