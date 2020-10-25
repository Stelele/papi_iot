from operator import index
from flask import Flask, render_template, Response, request
from papi_face_recognition import PapiFaceRecognition
from papi_storage_offline import OfflineStorage
from papi_email import PAPIEmail
from shutil import copy
import time
import os
import multiprocessing
import face_recognition

app = Flask(__name__)
email = PAPIEmail()
email.getCredentials('./client_secret_email.json')
offlineStorage = OfflineStorage()
offlineStorage.setOfflinePhotoStorageLocation()

@app.route('/', methods=['GET', 'POST'])
def move():
    result = ""
    if request.method == 'POST':
        
        return render_template('index.html', res_str=result)
                        
    return render_template('index.html')

def gen(camera):
    oldPhotoName = None
    sendTo = 'mgwgif001@myuct.ac.za'
    index = 0
    while True:
        frame, image, unknownPhotoName = camera.getFrame()

        if unknownPhotoName != None:
            unknownPath = unknownPhotoName.split('/')
            unknownPath[-1] = 'old_frame.jpg'
            temp = '/'.join(unknownPath)
            
            if os.path.exists(temp):           
                check_face_send(unknownPhotoName,temp,sendTo,index)
                index += 1
            else:
                email.send_message('me',sendTo,'Unknown User Spotted','Suspicious user was noticed at your premises', unknownPhotoName)

            if(index % 10 == 0):       
                copy(unknownPhotoName, temp)
                oldPhotoName = temp

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
        f = request.files['file']
        name = f.filename
        f.save(name)
        offlineStorage.storeNewKnownUser(name)
        os.remove(name)
        return render_template('new_user.html', added=True)

    return render_template('new_user.html')

@app.route('/remove_user', methods=['GET', 'POST'])
def remove_user():
    if request.method == 'POST':
        removed = offlineStorage.removeKnownUser(request.form.get('remove_user'))
        notRemoved = not removed 
        return render_template('remove_user.html', removed=removed, notRemoved=notRemoved)

    return render_template('remove_user.html')


def check_face_send(newpictureName,oldPicture, sendTo,index):
    if(index % 10 == 0): 
        newImage = face_recognition.load_image_file(newpictureName)
        oldImage = face_recognition.load_image_file(oldPicture)

        newEncording = face_recognition.face_encodings(newImage)
        oldEncording = face_recognition.face_encodings(oldImage)

        if(len(newEncording)>0 and len(oldEncording)> 0):
            newEncording = newEncording[0]
            oldEncording = oldEncording[0]
            results = face_recognition.compare_faces([newEncording], oldEncording)

            if not (True in results):
                email.send_message('me',sendTo,'Unknown User Spotted','Suspicious user was noticed at your premises', newpictureName)

if __name__ == '__main__':
    from waitress import serve
    serve (app, host="0.0.0.0", port=8080)  