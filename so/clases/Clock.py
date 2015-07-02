import threading  
import time
import sys



class Clock(threading.Thread):
    
    def __init__(self,cpu,irq):
        threading.Thread.__init__(self)
        self.observers=[cpu,irq]
        self.stoprequest = threading.Event()
        #self.registerObserver(cpu)
        self.RUNNING=True
    
    def registerObserver(self,observer):
        self.observers.append(observer)
        
    def notifyObservers(self):
        for elem in self.observers:
            elem.notify()
            
    
    def run(self):
        while self.RUNNING:
            
            self.notifyObservers()
            sys.stdout.flush()
            time.sleep(1)
        
        
        
            