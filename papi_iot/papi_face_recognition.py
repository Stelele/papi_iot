from PIL import Image, ImageDraw    # for image manipulation

class PapiFaceRecognition:
    # Class attributes here
    
    def __init__ (self):
        """
            Initial state of the object by assigning the values of the object’s properties
        """
        
        # Add code here
        pass
    
    def addAllowedUser (self):
        '''
            Add the users that the residence-room owner wants to the online
            database. 
            
            args:
                image_face (Image): a record of facial images
            
            return:
                None
        '''
        
        # Add code here
        
        pass
    
    def addBannedUser (self):
        '''
            Add the users that are banned from residence-room by the owner to the 
            online database. 
            
            args:
                image_face (Image): a record of facial images
            
            return:
                None
        '''
        
        # Add code here
        
        pass
    
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
        
        # Add code here
        
        pass
    
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