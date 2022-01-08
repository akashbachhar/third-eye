import cv2
import numpy as np
import dlib
from imutils import face_utils
import simpleaudio as sa

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

wave_obj = sa.WaveObject.from_wave_file("alarm.wav")


class VideoCamera(object):
    def __init__(self):
        self.sleep = 0
        self.drowsy = 0
        self.active = 0
        self.status = " "
        self.color = (0, 0, 0)

        self.dist = 0
        self.up = 0
        self.down = 0
        self.ratio = 0

        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def distance(self, ptA, ptB):
        self.dist = np.linalg.norm(ptA - ptB)
        return self.dist

    def blinked(self, a, b, c, d, e, f):
        self.up = self.distance(b, d) + self.distance(c, e)
        self.down = self.distance(a, f)
        self.ratio = self.up / (2.0 * self.down)

        if self.ratio > 0.25:
            return 2
        elif 0.21 < self.ratio <= 0.25:
            return 1
        else:
            return 0

    def get_frame(self):
        ret, frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)

        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            landmarks = predictor(gray, face)
            landmarks = face_utils.shape_to_np(landmarks)

            left_blink = self.blinked(landmarks[36], landmarks[37],
                                      landmarks[38], landmarks[41], landmarks[40], landmarks[39])
            right_blink = self.blinked(landmarks[42], landmarks[43],
                                       landmarks[44], landmarks[47], landmarks[46], landmarks[45])

            if left_blink == 0 or right_blink == 0:
                self.sleep += 1
                self.drowsy = 0
                self.active = 0
                if self.sleep > 6:
                    self.status = "Sleeping Alarm !!!"
                    self.color = (255, 0, 0)

            elif left_blink == 1 or right_blink == 1:
                self.sleep = 0
                self.active = 0
                self.drowsy += 1
                if self.drowsy > 6:
                    self.status = "Drowsing !"
                    self.color = (0, 0, 255)

            else:
                self.drowsy = 0
                self.sleep = 0
                self.active += 1
                if self.active > 6:
                    self.status = "You're Active :)"
                    self.color = (0, 255, 0)

            cv2.putText(frame, self.status, (100, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, self.color, 3)

            for n in range(0, 68):
                (x, y) = landmarks[n]
                cv2.circle(frame, (x, y), 1, (255, 255, 255), -1)
            if self.sleep > 6 or self.drowsy > 6:
                wave_obj.play()
        suc, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
