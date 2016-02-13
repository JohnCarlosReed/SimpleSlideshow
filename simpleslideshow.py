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
    image_files = []
    for dirpath, dirs, files in os.walk(image_path):
        for filename in files:
            if filename.endswith((".jpg", ".png")):
                image_files.append(os.path.join(dirpath, filename))
    return image_files

def runSlideShow():
    while(True):
        for image in images:
            cv2.imshow('image', cv2.imread(image))
            if cv2.waitKey(wait_time) > 0:
                cv2.destroyWindow('image')
                return


if __name__ == '__main__':
    images = get_image_files()
    runSlideShow()
