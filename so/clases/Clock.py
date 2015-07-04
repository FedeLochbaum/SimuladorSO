import threading  
import time
import sys



class Clock(threading.Thread):
    
    def __init__(self,cpu):
        threading.Thread.__init__(self)
        self.observers=[]
        self.registerObserver(cpu)
        self.stoprequest = threading.Event()
        
        self.RUNNING=True
    
    def registerObserver(self,observer):
        self.observers.append(observer)
        
    def notifyObservers(self):
        self.notifyUserMode()
        self.notifyKernelMode()
        
    def notifyUserMode(self):
        
        for elem in self.observers:
            elem.notifyUserMode()
    
    def notifyKernelMode(self):
        
        for elem in self.observers:
            elem.notifyKernelMode()        
    
    def run(self):
        while self.RUNNING:
            
            self.notifyObservers()
            sys.stdout.flush()
            time.sleep(1)
        
        
        
            