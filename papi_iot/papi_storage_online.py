from google.cloud import storage
import os

class OnlineStorage:

    def __init__(self):

        self.onlineStorageCredentials = None
        self.onlinePhotoStorageLocation = None
        self.onlineVideoStorageLocation = None
        self.photoBucket = None
        self.videoBucket = None

    def connectToOnlineStorage(self, credentialsFile, photoLocation, videoLocation):
        self.onlinePhotoStorageLocation = photoLocation
        self.onlineVideoStorageLocation = videoLocation

        self.onlineStorageCredentials = storage.Client.from_service_account_json(credentialsFile)

        self.photoBucket = self.onlineStorageCredentials.get_bucket(self.onlinePhotoStorageLocation)
        self.videoBucket = self.onlineStorageCredentials.get_bucket(self.onlineVideoStorageLocation)


    def setOnlinePhotoStorageLocation(self, photoLocation):
        self.onlinePhotoStorageLocation = photoLocation
        self.photoBucket = self.onlineStorageCredentials.get_bucket(self.onlinePhotoStorageLocation)

    def setOnlineVideoStorageLocation(self, videoLocation):
        self.onlineVideoStorageLocation = videoLocation
        self.videoBucket = self.onlineStorageCredentials.get_bucket(self.onlineVideoStorageLocation)

    def storeOnlinePhotos(self, folderLocation):
        pass
        
    def storeOnlineVideos(self):
        pass

    def getOnlinePhoto(self):
        pass

    def getOnlinePhotos(self):
        pass

    def getOnlineVideo(self):
        pass

    def getOnlineVideos(self):
        pass
    
if __name__ == "__main__":
    test = OnlineStorage()
    test.connectToOnlineStorage('papi-iot-credentials.json', 'papi_photo_bucket', 'papi_video_bucket')

