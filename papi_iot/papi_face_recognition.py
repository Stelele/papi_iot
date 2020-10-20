import face_recognition
import os
import cv2
import pickle
import time
import numpy as np

class PapiFaceRecognition:
    # Class attributes here
    KNOWN_FACES_DIR = './home/pi/photos/knownFaces'
    UNKNOWN_FACES_DIR = './home/pi/photos/unknownFaces'

    TOLERANCE = 0.6
    FRAME_THICKNESS = 3
    FONT_THICKNESS = 2
    MODEL = 'cnn'

    VIDEO = cv2.VideoCapture(0) # Could put in a video file or path to video file/stream from camera

    def __init__ (self):
        """
            Initial state of the object by assigning the values of the object’s properties
        """
        #self.DIRECTORIES = OfflineStorage()
        self.KNOWN_FACES_DIR = './home/pi/photos/knownFaces' #DIRECTORIES.getOfflinePhotoStorageLocation('known_faces')
        self.UNKNOWN_FACES_DIR = './home/pi/photos/unknownFaces' #DIRECTORIES.getOfflinePhotoStorageLocation('unknown_faces')
        self.TOLERANCE = 0.6
        self.FRAME_THICKNESS = 3
        self.FONT_THICKNESS = 2
        self.MODEL = 'cnn'
        self.VIDEO = cv2.VideoCapture(0)

    def nameToColor (self, name):
        # Take 3 first letters, tolower()
        # lowercased character ord() value rage is 97 to 122, substract 97, multiply by 8
        color = [(ord(c.lower()) - 97) * 8 for c in name[:3]]
        return color
    
    def faceRecognitionFromPhoto (self):
        print('Loading known faces...')
        known_faces = []
        known_names = []

        # We oranize known faces as subfolders of KNOWN_FACES_DIR
        # Each subfolder's name becomes our label (name)
        # Next we load every file of faces of known person
        for file in os.listdir(self.KNOWN_FACES_DIR):
            # print(file)
            # Load an image
            known_names.append(file.replace(".jpg", ""))
            file = os.path.join(self.KNOWN_FACES_DIR + "/", file)
            image = face_recognition.load_image_file(file)

            # Get 128-dimension face encoding
            # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
            encoding = face_recognition.face_encodings(image)[0]
            # Append encodings
            known_faces.append(encoding)
            


        print('Processing unknown faces...')
        # Now let's loop over a folder of faces we want to label
        for filename in os.listdir(self.UNKNOWN_FACES_DIR):

            # Load image
            print(f'Filename {filename}', end='')
            image = face_recognition.load_image_file(f'{self.UNKNOWN_FACES_DIR}/{filename}')

            # This time we first grab face locations - we'll need them to draw boxes
            locations = face_recognition.face_locations(image, model=self.MODEL)

            # Now since we know loctions, we can pass them to face_encodings as second argument
            # Without that it will search for faces once again slowing down whole process
            encodings = face_recognition.face_encodings(image, locations)

            # We passed our image through face_locations and face_encodings, so we can modify it
            # First we need to convert it from RGB to BGR as we are going to work with cv2
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # But this time we assume that there might be more faces in an image - we can find faces of dirrerent people
            print(f', found {len(encodings)} face(s)')
            for face_encoding, face_location in zip(encodings, locations):

                # We use compare_faces (but might use face_distance as well)
                # Returns array of True/False values in order of passed known_faces
                results = face_recognition.compare_faces(known_faces, face_encoding, self.TOLERANCE)

                # Since order is being preserved, we check if any face was found then grab index
                # then label (name) of first matching known face withing a tolerance
                match = None
                if True in results:  # If at least one is true, get a name of first of found labels
                    match = known_names[results.index(True)]
                    print(f' - {match} from {results}')

                    # Each location contains positions in order: top, right, bottom, left
                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])

                    # Get color by name using our fancy function
                    color = self.nameToColor(match)

                    # Paint frame
                    cv2.rectangle(image, top_left, bottom_right, color, self.FRAME_THICKNESS)

                    # Now we need smaller, filled grame below for a name
                    # This time we use bottom in both corners - to start from bottom and move 50 pixels down
                    top_left = (face_location[3], face_location[2])
                    bottom_right = (face_location[1], face_location[2] + 22)

                    # Paint frame
                    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)

                    # Wite a name
                    cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), self.FONT_THICKNESS)

            # Show image
            cv2.imshow(filename, image)
            cv2.waitKey(0)
            cv2.destroyWindow(filename)


    def faceRecognitionFromVdeo (self):
        print('Loading known faces...')
        # Store objects in array
        # Name of person string
        known_person = []
        # Image object 
        known_image = [] 
        # Encoding object
        known_face_encodings = [] 

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        #Loop to add images in friends folder
        for file in os.listdir(self.KNOWN_FACES_DIR):
            try:
                #Extracting person name from the image filename eg: david.jpg
                known_person.append(file.replace(".jpg", ""))
                file=os.path.join(self.KNOWN_FACES_DIR + "/", file)
                known_image = face_recognition.load_image_file(file)
                #print(face_recognition.face_encodings(known_image)[0])
                known_face_encodings.append(face_recognition.face_encodings(known_image)[0])
                #print(known_face_encodings)

            except Exception as e:
                pass
            
        #print(len(known_face_encodings))
        #print(known_person)

        while True:
            # Grab a single frame of video
            ret, frame = self.VIDEO.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                global name_gui;
                #face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"
                    
                    #print(face_encoding)
                    #print(matches)

                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_person[best_match_index]

                    #print(name)
                    #print(face_locations)
                    face_names.append(name)
            
                    name_gui = name

            process_this_frame = not process_this_frame


            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 255, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name_gui, (left + 10, bottom - 10), font, 1.0, (0, 0, 0), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        self.VIDEO.release()
        cv2.destroyAllWindows()

# if __name__ == "__main__":
    #unit = PapiFaceRecognition()

    # unit.faceRecognitionFromPhoto()
    # unit.faceRecognitionFromVdeo()


    
