import logging


class RoutineCommand:
    
    def __init__(self):
        logging.basicConfig(filename='logSo.log',level=logging.DEBUG)
    
    def canHandle(self,command):
        pass
    
    def handle(self,command,param=None ,shell=None,file =None):
        pass