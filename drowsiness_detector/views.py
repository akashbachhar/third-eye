from django.shortcuts import render
from drowsiness_detector.camera import VideoCamera
from django.http import StreamingHttpResponse


def home(self):
    return render(self, 'drowsiness_detector/home.html')


def live_page(self):
    return render(self, 'drowsiness_detector/live.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def live_view(self):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
