import threading  
import time
import sys
import logging



class Clock(threading.Thread):
    
    def __init__(self,cpu):
        threading.Thread.__init__(self)
        self.observers=[]
        self.registerObserver(cpu)
        self.stoprequest = threading.Event()
        #self.logger=logging.basicConfig(filename='logSo.log',level=logging.DEBUG)
        self.cycleNum=0
        
        self.RUNNING=True
    
    def registerObserver(self,observer):
        self.observers.append(observer)
        
    def notifyCycle(self):
        #self.logger.debug('Notifying Cycle Number %i' % self.cycleNum)
        self.notifyUserMode()
        self.notifyKernelMode()
        self.cycleNum+=1
        
    def notifyUserMode(self):
        
        for elem in self.observers:
            elem.notifyUserMode()
    
    def notifyKernelMode(self):
        
        for elem in self.observers:
            elem.notifyKernelMode()        
    
    def run(self):
        while self.RUNNING:
            
            self.notifyCycle()
            sys.stdout.flush()
            time.sleep(1)
        
        
        
            