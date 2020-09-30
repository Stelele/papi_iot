from papi_storage_online import OnlineStorage
from papi_storage_offline import OfflineStorage 

class StorageManager(OnlineStorage, OfflineStorage):
    
    def __init__(self):
        OnlineStorage.__init__(self)
        OfflineStorage.__init__(self)

        self.useOnlineStorage = False
        self.useOfflineStorage = True

    def storeOfflinePhotosOnline(self):
        pass

    def storeOfflineVideosOnline(self):
        pass

    
