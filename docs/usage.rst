.. toctree::
    :maxdepth: 3
    :numbered:

=====
Usage
=====

Basic Import 
---------------

To use entire PAPI IOT features at once do the following::

    from papi_iot.papi_iot import PAPIIOT

    papi = PAPIIOT()

Offline Storage Operations
-------------------------------

To add new user to offline storage::

    papi.offlineStorage.storeNewKnownUser('/photo/location/name.jpg')

To remove user from offline storage::

    papi.offlineStorage.removeKnownUser('name')

To get storage locations of photos and videoStorageBucketName::

    known_dir = papi.offlineStorage.getOfflinePhotoStorageLocation('knownFaces')
    unknown_dir = papi.offlineStorage.getOfflinePhotoStorageLocation('unknownFaces')
    vid_dir = papi.offlineStorage.getOfflineVideoStorageLocation()

To remove known users::

    papi.offlineStorage.removeKnownUser('name')

Online Storage Operations
----------------------------

To optionally setup online storage, download the `Google Cloud service account json`_ and execute::

    papi.onlineStorage.connectToOnlineStorage("json/sevice/account/file/","photoStorageBucketName", "videoStorageBucketName")

To change photo storage location::

    papi.onlineStorage.setOnlinePhotoStorageLocation("newPhotoBucketLocation")

To change video storage location::

    papi.onlineStorage.setOnlineVideoStorageLocation("newVideoStorageLocation")

To store photos online::

    papi.onlineStorage.storeOnlinePhotos("/photo/storage/folder")

To store videos online::

    papi.onlineStorage.storeOnlineVideos("/video/storage/folder")

To get a photo from online storage::

    papi.onlineStorage.getOnlinePhoto("photoname", "/dest/folder/location")

To get multiple photos from online storage::

    papi.onlineStorage.getOnlinePhotos("/dest/folder/location", startsWith="starting letters")

To get a video from online storage::

    papi.onlineStorage.getOnlineVideo("videoname", "/dest/folder/location")

To get multiple videos from online storage::

    papi.onlineStorage.getOnlineVideos("/dest/folder/location", startsWith="starting letters")

Camera Video Operations
--------------------------

To auto-adjust to light::

    papi.cameraVideo.autoAdjustToLight()

To set to camera mode::

    papi.cameraVideo.setCameraMode()

To take photo::

    papi.cameraVideo.takePhoto('/dest/folder/location/photoName')

To record a video for a certain time::

    papi.cameraVideo.recordVideoFor("/dest/folder/location/videoName", length=60#) #length in seconds

To record continuously::

    papi.cameraVideo.recordVideo("/dest/folder/location/videoname")

To stop recording::

    papi.cameraVideo.stopVideoRecording()

Face Recognition Operations
------------------------------

Instatiating photos in database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To load unknown faces to categorise::

    papi.offlineStorage.storeUnknownPhotos('/source/folder/location')

To load known faces to database::

    papi.offlineStorage.storeNewKnownUsers('/source/folder/location')

Facial Recognition from photos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To categorise faces in the unknown faces folder::

    papi.faceRecognition.faceRecognitionFromPhoto()

To compare if the same user is in the same photo::

    papi.faceRecognition.checkSamePerson('/first/photo/location/name1.jpg', '/second/photo/location/name2.jpg')

Facial Recognition from videos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To recognise faces from a live video feed::

    papi.faceRecognition.faceRecognitionFromVideo()

To recognise faces from a video file::

    papi.faceRecognition.faceRecognitionFromVideoFile('/folder/location/video.mp4')


.. _`Google Cloud service account json`: https://cloud.google.com/storage/docs/reference/libraries