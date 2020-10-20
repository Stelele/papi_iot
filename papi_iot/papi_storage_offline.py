from shutil import copy
from os import listdir
from os import makedirs
from matplotlib import image

class OfflineStorage:
    rootDir = 'home/pi'
    knownFaces = '/knownFaces'
    # nameLabel = '/name'
    unknownFaces = '/unknownFaces'

    def __init__(self):
        """
            Initial state of the object by assigning the values of the object’s properties.
            Create knownFaces and unknownFaces folders.
        """
        self.setOfflinePhotoStorageLocation()
        self.setOfflineVideoStorageLocation()
        
    def setOfflinePhotoStorageLocation(self):
        makedirs(self.rootDir + '/photos' +  self.knownFaces)
        makedirs(self.rootDir + '/photos' +  self.unknownFaces)

    #def setOfflinePhotoStorageNameLabelLocation(self, name)
    #    '''
    #        Create subfolders for name labels
    #        args:
    #            name (string): label of known user 
    #    '''
    #    self.nameLabel = name
    #    makedirs(rootDir + '/photos' +  knownFaces + nameLabel)
    
    #def getOfflinePhotoStorageNameLabelLocation(self):
    #    return '.' + self.rootDir + '/photos' + self.knownFaces + self.nameLabel

    def getOfflinePhotoStorageLocation(self, category):
        if category == 'knownFaces':
            return './' + self.rootDir + '/photos' + self.knownFaces
        else: 
            return './' + self.rootDir + '/photos' + self.unknownFaces

    def setOfflineVideoStorageLocation(self):
        makedirs(self.rootDir + '/videos')

    def storeOfflinePhotos(self, filename, destination):
        """
            Store photos from pi camera into the given folder

            args:
                filename (string): filename for image
                destination (string): location to store image
        """
        copy(filename, destination)

    def storeOfflineVideos(self, filename):
        """
            Store video from pi camera into the given video folder

            args:
                filename (string): filename for video
        """
        copy(filename, self.rootDir + '/videos')

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
        for filename in listdir('./' + self.rootDir + '/photos' +  self.knownFaces):
            imgData = image.imread('./' + self.rootDir + '/photos' +  self.knownFaces + '/' + filename)
            knownFacesImageList.append(imgData)

        for filename in listdir('./' + self.rootDir + '/photos' +  self.unknownFaces):
            imgData = image.imread('./' + self.rootDir + '/photos' +  self.unknownFaces + '/' + filename)
            unknownFacesImageList.append(imgData)

        return knownFacesImageList, unknownFacesImageList

    def getOfflinesVideo(self):
        videoList = list()
        for filename in listdir('./' + self.rootDir + '/videos'):
            videoData = image.imread('./' + self.rootDir + '/videos' + '/' + filename)
            videoList.append(videoData)
        return videoList

if __name__ == "__main__":
    unit = OfflineStorage ()

