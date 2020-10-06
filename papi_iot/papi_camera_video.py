from time import sleep
from picamera import PiCamera

from picamera import PiCameraError

class PapiCameraVideo:
    
    # Class attributes here testing content
    def __init__ (self): 
        """ 
    
        Initial state of the object by assigning the values of the object properties
        
        """
        
        self.camera = PiCamera()
        
   
    def setCameraMode (self, resolution=(1024, 768)): 
        """ 
        
        Switch the camera between infared cut-off and no infared cut-off filter 
        
        """

        self.camera.resolution = resolution
        self.camera.start_preview()

        #camera warm-up time
        sleep(2)
        
    def setLowLightMode (self, alternateISO=False): 
        """
        
        Switch the camera mode to low light mode
        
        """
        
        self.autoAdjustToLight()

        # Set ISO to low light values
        self.camera.iso = 800 if alternateISO else 400 

        # wait for the automatic gain control to settle
        sleep(2)

        # now fix the values
        self.camera.shutter_speed = self.camera.exposure_speed
        self.camera.exposure_mode = 'off'
        
        gain = self.camera.awb_gains
        self.camera.awb_mode = 'off'
        self.camera.awb_gains = gain
    
    def setNormalLightMode (self, alternateISO=False): 
        """
        
        Switch the camera mode to normal light mode
        
        """

        self.autoAdjustToLight()

        # Set ISO to low light values
        self.camera.iso = 200 if alternateISO else 100 

        # wait for the automatic gain control to settle
        sleep(2)

        # now fix the values
        self.camera.shutter_speed = self.camera.exposure_speed
        self.camera.exposure_mode = 'off'
        
        gain = self.camera.awb_gains
        self.camera.awb_mode = 'off'
        self.camera.awb_gains = gain
        
    
    def autoAdjustToLight (self): 
        """
        
        Automatically adjust the camera lighting according to light conditions at the time
        
        """

        self.camera.iso = 0
        self.camera.exposure_mode = 'auto'
        self.shutter_speed = 0
        self.camera.awb_mode = 'auto'
        
        # wait for automatic gain control to settle
        sleep(2)
        
        
    
    def takePhoto (self, name): 
        """ 
        
        Capture the image of face in camera field of view. Note, assumes setCameraMode has been run
        before running this function 
        -------------------------------------------------------------------------------------------
        variables:
        name: chosen name of photo taken

        """
        name = name + '.jpg'
        self.camera.capture(name)
        
    
    def recordVideoFor (self): 
        """
        
        Capture the footage of face in camera field of view
        
        """
        
        # Add code here
        
        pass
    
    def recordVideo (self): 
        """
        
        Capture the footage of face in camera field of view
        
        """
        
        # Add code here
        
        pass
    
    def stopVideoRecording (self): 
        """
        
        Stop the video recording
        
        """
        
        # Add code here
        
        pass

if __name__ == "__main__":
    test = PapiCameraVideo()
    test.setCameraMode()
    test.autoAdjustToLight()
    test.takePhoto("test")