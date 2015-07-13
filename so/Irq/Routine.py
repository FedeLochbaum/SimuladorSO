import logging


class Routine:
    
    def __init__(self):
        logging.basicConfig(filename='logSo.log',level=logging.DEBUG)
    
    def canHandle(self,irq):
        pass
    
    def handle(self,irq,cpu,program=None,ioInstruction=None):
        pass