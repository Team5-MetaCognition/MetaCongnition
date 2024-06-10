import threading
import time

class Timer(threading.Thread):
    def __init__(self, seconds, update_callback, finished_callback):
        super().__init__()
        self.seconds = seconds
        self.update_callback = update_callback
        self.finished_callback = finished_callback
        self.daemon = True
    
    def startTimer(self):
        while self.seconds > 0:
            # print(self.seconds)
            self.update_callback(self.seconds)
            time.sleep(1)
            self.seconds -= 1
        self.finished_callback()