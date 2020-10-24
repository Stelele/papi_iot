from flask import Flask, render_template, Response, request
from papi_face_recognition import PapiFaceRecognition
from papi_email import PAPIEmail
import time
import os
import threading
import face_recognition

app = Flask(__name__)
email = PAPIEmail()
email.getCredentials('./client_secret_email.json')

@app.route('/', methods=['GET', 'POST'])
def move():
    result = ""
    if request.method == 'POST':
        
        return render_template('index.html', res_str=result)
                        
    return render_template('index.html')

def gen(camera):
    oldPhotoName = None
    sendTo = 'mgwgif001@myuct.ac.za'

    while True:
        frame, image, unknownPhotoName = camera.getFrame()

        if unknownPhotoName != None and unknownPhotoName != oldPhotoName:
            if oldPhotoName != None:
                check = threading.Thread(target=check_face_send,args=(unknownPhotoName,oldPhotoName,sendTo,))
                check.start()
            else:
                email.send_message('me',sendTo,'Unknown User Spotted','Suspicious user was noticed at your premises', unknownPhotoName)

            oldPhotoName = unknownPhotoName

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(PapiFaceRecognition()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/show_video')
def show_video():
    if request.method == 'POST':
        return render_template('video_feed.html')

    return render_template('video_feed.html')

@app.route('/register_user')
def register_user():
    return render_template('index.html')

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        return render_template('new_user.html')

    return render_template('new_user.html')

@app.route('/remove_user', methods=['GET', 'POST'])
def remove_user():
    if request.method == 'POST':
        return render_template('remove_user.html')

    return render_template('remove_user.html')


def check_face_send(newpictureName,oldPicture, sendTo):
    newImage = face_recognition.load_image_file(newpictureName)
    oldImage = face_recognition.load_image_file(oldPicture)

    newEncording = face_recognition.face_encodings(newImage)[0]
    oldEncording = face_recognition.face_encodings(oldImage)[0]

    results = face_recognition.compare_faces([newEncording], oldEncording, 0.4)

    if not (True in results):
        global email
        email.send_message('me',sendTo,'Unknown User Spotted','Suspicious user was noticed at your premises', newpictureName)

if __name__ == '__main__':
    from waitress import serve
    serve (app, host="0.0.0.0", port=8080)  