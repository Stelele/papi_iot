from flask import Flask, render_template, Response, request
from papi_face_recognition import PapiFaceRecognition
import time
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def move():
    result = ""
    if request.method == 'POST':
        
        return render_template('index.html', res_str=result)
                        
    return render_template('index.html')

def gen(camera):
    while True:
        frame, image = camera.getFrame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(PapiFaceRecognition()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    from waitress import serve
    serve (app, host="0.0.0.0", port=8080)  