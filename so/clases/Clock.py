from threading import Thread
import time




class Clock(Thread):
    
    def __init__(self,cpu):
        Thread.__init__(self)
        self.observers=[]
        self.registerObserver(cpu)
        self.RUNNING=True
    
    def registerObserver(self,observer):
        self.observers.append(observer)
        
    def notifyObservers(self):
        for elem in self.observers:
            elem.notify()
            print("NOTIFICADO")
    
    def run(self):
        #Thread.run(self)
        self.notifyObservers()
        time.sleep(1)
        
    def start(self):
        Thread.start(self)
            
            