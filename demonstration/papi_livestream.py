print("Starting Server")
from operator import index
print("Setting Flask")
from flask import Flask, render_template, Response, request
print("Getting Face Recognition")
from papi_iot.papi_face_recognition import PapiFaceRecognition
print("Setting Storage")
from papi_iot.papi_storage_offline import OfflineStorage
from papi_email import PAPIEmail
from shutil import copy
import os

print("Setting variables")
app = Flask(__name__)
email = PAPIEmail()

print("Got Email Credentails")
offlineStorage = OfflineStorage()
offlineStorage.setOfflinePhotoStorageLocation()
print("Set offlne Storage")
@app.route('/', methods=['GET', 'POST'])
def move():
    result = ""
    if request.method == 'POST':
        
        return render_template('index.html', res_str=result)
                        
    return render_template('index.html')

def gen(camera):
    oldPhotoName = None
    sendTo = 'mgwgif001@myuct.ac.za'
    video_index = 0
    while True:
        frame, image, unknownPhotoName = camera.getFrame()

        if unknownPhotoName != None:
            unknownPath = unknownPhotoName.split('/')
            unknownPath[-1] = 'old_frame.jpg'
            temp = '/'.join(unknownPath)
            if oldPhotoName != None and os.path.exists(temp):
                check_face_send(unknownPhotoName,temp,sendTo,video_index)
                video_index += 1
            else:
                email.send_message('me',sendTo,'Unknown User Spotted','Suspicious user was noticed at your premises', unknownPhotoName)

            if(video_index % 5 == 0):       
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
    email.getCredentials('client_secret_email.json')
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


def check_face_send(newpictureName,oldPicture, sendTo,video_index, skipFor=5):
    if(video_index % skipFor == 0): 
        print("comparing old and new")
        
        checkMatch = PapiFaceRecognition.checkSamePerson(newpictureName, oldPicture)
        if not checkMatch:
            print("Sending email")
            email.send_message('me',sendTo,'Unknown User Spotted','Suspicious user was noticed at your premises', newpictureName)

if __name__ == '__main__':
    from waitress import serve
    serve (app, host="0.0.0.0", port=8080)   
    
