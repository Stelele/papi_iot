from shutil import copy
from os import listdir
from os import makedirs
from matplotlib import image

class OfflineStorage:
    rootDir = 'home/pi'
    knownFaces = '/knownFaces'
    unknownFaces = '/unknownFaces'

    def __init__(self):
        """
            Initial state of the object by assigning the values of the object’s properties.
            Create knownFaces and unknownFaces folders.
        """
        self.setOfflinePhotoStorageLocation()
        self.setOfflineVideoStorageLocation()
        
    def setOfflinePhotoStorageLocation(self):
        makedirs(rootDir + '/photos' +  knownFaces)
        makedirs(rootDir + '/photos' +  unknownFaces)

    def getOfflinePhotoStorageLocation(self, category):
        if category == 'knownFaces':
            return './' + self.rootDir + '/photos' + self.knownFaces
        else: 
            return './' + self.rootDir + '/photos' + self.unknownFaces

    def setOfflineVideoStorageLocation(self):
        pass

    def storeOfflinePhotos(self, photo, destination):
        """
            Store photos from pi camera into the given folder

            args:
                photo (string): filename for image
                destination (string): location to store image
        """
        copy(photo, destination)

    def storeOfflineVideos(self):
        pass

    def getOfflinePhoto(self, destination):
        """
            Obtain photo based on destination given.

            args: 
                destination (string): filename for image
            
            return:
                image as pixel array
        """
        return image.imread(destination)

    def getOfflinePhotos(self):
        """
            Obtain all photos from both knownFaces and unknownFace folders

            return:
                knownFacesImageList (list): known faces image pixel array list
                unknownFacesImageList (list): unknown faces image pixel array list
        """
        knownFacesImageList = list()
        unknownFacesImageList = list()
        for filename in listdir('./' + rootDir + '/photos' +  knownFaces):
            imgData = image.imread('./' + rootDir + '/photos' +  knownFaces + '/' + filename)
            knownFacesImageList.append(imgData)

        for filename in listdir('./' + rootDir + '/photos' +  unknownFaces):
            imgData = image.imread('./' + rootDir + '/photos' +  unknownFaces + '/' + filename)
            unknownFacesImageList.append(imgData)

        return knownFacesImageList, unknownFacesImageList


    def getOfflineVideo(self):
        pass

    def getOfflineVideos(self):
        pass

if __name__ = "__main__":
    unit = OfflineStorage ()

