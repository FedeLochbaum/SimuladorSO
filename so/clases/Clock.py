from threading import Thread
import time


class Clock(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.observers=[]
    
    def registerObserver(self,observer):
        self.observers.append(observer)
        
    def notifyObservers(self):
        for elem in self.observers:
            elem.notify()
    
    def run(self):
        Thread.run(self)
        self.notifyObservers()
        time.sleep(1)
       
