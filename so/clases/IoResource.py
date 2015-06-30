from queue import Queue
from threading import Thread
class IoResource(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.ioWaitingQueue=Queue()
        
    def canHandle(self,resource):
        pass
    
    def handle(self,pcb):
        self.ioWaitingQueue.put(pcb)