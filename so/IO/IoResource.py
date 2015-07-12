from queue import Queue
from threading import Thread  
import time
import sys
class IoResource(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.ioWaitingQueue={}
        self.actualPcb=None
        self.info=''
        
    def canHandle(self,resource):
        pass
    
    def handle(self,pcb,ioInstruction):
        index=self.ioWaitingQueue.__len__()
        self.ioWaitingQueue[index]=(pcb,ioInstruction)
        
    def run(self):
        while self.RUNNING:
            
            self.takePcbAndExecute()
            sys.stdout.flush()
            time.sleep(1)
            
    def takePcbAndExecute(self):
        self.actualPcb=self.ioWaitingQueue.get()[0]
        message=self.ioWaitingQueue.get()[1].getMessage()
        self.info+=message
        
    def get(self,index):
        return self.ioWaitingQueue[index]
    
    def pcbCount(self):
        return self.ioWaitingQueue._qsize()
            
    