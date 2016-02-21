"""
This is a barebones slideshow application using OpenCV as an experiment and excuse
to learn something about OpenCV.
The image_path, windowHeight, windowWidth are hard-coded and need to be set manually.
"""

import numpy as np
import cv2
import os

image_path = '/home/johnreed/Desktop/opencvpics'
wait_time    = 8000   #milliseconds
windowWidth  = 1366
windowHeight = 768

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.moveWindow('image', 0,0)
cv2.resizeWindow('image', windowWidth,windowHeight)

def get_image_files():
    """
    Recursive directory lookup of image_path for *.jpg and *.png files
    :return: a list of full-path image files
    """
    image_files = []
    for dirpath, dirs, files in os.walk(image_path):
        for filename in files:
            if filename.endswith((".jpg", ".png")):
                image_files.append(os.path.join(dirpath, filename))
    return image_files

def runSlideShow():
    """
    Main loop.  Open each image for wait_time mount of time until a key is pressed
    :return: None
    """
    while(True):
        for image in images:
            cv2.imshow('image', cv2.imread(image))
            if cv2.waitKey(wait_time) > 0:
                cv2.destroyWindow('image')
                return None


if __name__ == '__main__':
    images = get_image_files()
    runSlideShow()
