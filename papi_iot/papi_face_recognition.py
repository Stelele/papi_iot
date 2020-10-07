from PIL import Image, ImageDraw    # for image manipulation
import face_recognition
import os
import cv2

class PapiFaceRecognition:
    # Class attributes here
    known_faces = []
    known_names = []

    def __init__ (self, known_faces_dir, unknown_faces_dir, tolerance=0.6, frame_thickness=3, font_thickness=2, model='cnn'):
        """
            Initial state of the object by assigning the values of the object’s properties
        """
        self.known_faces_dir = known_faces_dir
        self.unknown_faces_dir = unknown_faces_dir
        self.tolerance = tolerance
        self.frame_thickness = frame_thickness
        self.font_thickness = font_thickness
        self.model = model

    def nameToColor (self, name):
        color = [(ord(c.lower()) - 97) * 8 for c in name[:3]]
        return color

    def addAllowedUser (self, filename):
        '''
            Add the users that the residence-room owner wants to the online
            database.

            args:
                image_face (Image): a record of facial images

            return:
                None
        '''

        print(f'Filename {filename}')
        image = face_recognition.load_image_file(f'{filename}')
        encoding = face_recognition.face_encodings(image)[0]
        return encoding

    def addBannedUser (self, filename):
        '''
            Add the users that are banned from residence-room by the owner to the
            online database.

            args:
                image_face (Image): a record of facial images

            return:
                None
        '''

        print(f'Filename {filename}')
        image = face_recognition.load_image_file(f'{filename}')
        locations = face_recognition.face_locations(image, model=self.model)
        encodings = face_recognition.face_encodings(image, locations)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        return image, locations, encodings

    def removeUser (self):
        '''
            remove the users from the online database.

            args:
                None

            return:
                None
        '''

        # Add code here

        pass

    def identifyFromPhoto (self):
        '''
            Find all the faces that appear in a picture. Recognize who appears
            in each photo

            args:

            return:

        '''

        for name in os.listdir(self.known_faces_dir):
            for filename in os.listdir(f'{self.known_faces_dir}/{name}'):
                encoding = addAllowedUser (filename)
                known_faces.append(encoding)
                known_names.append(name)

        print('Processing unknown faces...')
        for filename in os.listdir(self.unknown_faces_dir):
            print(f'Filename {filename}', end='')
            image, locations, encodings = addBannedUser (filename)

            print(f', found {len(encodings)} face(s)')
            for face_encoding, face_location in zip(encodings, locations):
                results = face_recognition.compare_faces(known_faces, face_encoding, self.tolerance)
                match = None
                if True in results:
                    match = known_names[results.index(True)]
                    print(f' - {match} from {results}')
                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])
                    color = nameToColor(match)
                    cv2.rectangle(image, top_left, bottom_right, color, self.frame_thickness)
                    top_left = (face_location[3], face_location[2])
                    bottom_right = (face_location[1], face_location[2] + 22)
                    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                    cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (200, 200, 200), self.font_thickness)
            cv2.imshow(filename, image)
            cv2.waitKey(0)
            cv2.destroyWindow(filename)



    def identifyFromVideo (self):
        '''
            Do real-time face recognition

            args:

            return:

        '''

        # Add code here

        pass

    def recordTimeOfEncounter (self):
        '''
            Do real-time face recognition

            args:
                None

            return:
                hours (integer): hour of the day in real time
                mins (integer): minutes in real time
                secs (integer): seconds in real time
        '''

        # Add code here

        pass

    def gettingMatchingStatistics (self):
        '''
            Output the measure parameters of the matching algorithm

            args:
                None

            return:
                accuracy (float): the percentile match of the recognised face
                loss (float):  loss is a number indicating how bad the model's prediction was on a single face
        '''

        # Add code here

        pass

if __name__ == "__main__":
    test = PapiFaceRecognition()
