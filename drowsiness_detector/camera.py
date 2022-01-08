import cv2 as cv
import numpy as np

class VideoCamera(object):
    def __init__(self):
        self.video = cv.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret, img = self.video.read()
        suc, jpeg = cv.imencode('.jpg', img)
        return jpeg.tobytes()
