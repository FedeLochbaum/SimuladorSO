import logging
import sys
from threading import Thread  
import time


class IoResource(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.ioWaitingQueue={}
        self.actualPcb=None
        self.info=''
        logging.basicConfig(filename='logSo.log',level=logging.DEBUG)
        
    def canHandle(self,resource):
        pass
    
    def handle(self,pcb,ioInstruction):
        index=self.ioWaitingQueue.__len__()
        self.ioWaitingQueue[index]=(pcb,ioInstruction)
        logging.debug('Added %s to IoWaiting Queue of IoResource' % pcb.getName())
        
    def run(self):
        while self.RUNNING:
            
            self.takePcbAndExecute()
            sys.stdout.flush()
            time.sleep(1)
            
    def takePcbAndExecute(self):
        self.actualPcb=self.ioWaitingQueue.get(0)[0]
        logging.debug('Io Resource took %s' % self.actualPcb.getName())
        message=self.ioWaitingQueue.get(0)[1].getMessage()
        logging.debug('Io Instruction message: %s' % message)

        self.info+=message
        
    def get(self,index):
        return self.ioWaitingQueue[index]
    
    def pcbCount(self):
        return self.ioWaitingQueue._qsize()
            
    