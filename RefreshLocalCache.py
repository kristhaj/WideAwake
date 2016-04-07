
from threading import Thread
import time

class RefreshCacheLocal(Thread):

    def __init__(self, external, local):
        super().__init__()
        self.daemon =  True
        self.external = external
        self.internal = local
        self.lastrefresh = time.time()

    def run(self):
        while True:
            if time.time() - self.lastrefresh > (60*5):
                self.internal.updateLocalDatebase(self.external.getResultSet("SELECT Latitude,Longitude, Timestamp FROM Coordinates"))

