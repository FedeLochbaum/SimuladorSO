import logging
from os.path import os


class Shell():

    def __init__(self, kernel,commandHandler):
        self.kernel=kernel
        self.commandHandler=commandHandler
        self.successCommands=[]
        os.chdir("C:/")
        self.root = os.getcwd()
        logging.basicConfig(filename='logSo.log',level=logging.DEBUG)
        
    def readCommand(self,command,param= None,file=None):
        logging.debug('Reading Command')
        success=self.commandHandler.handle(command,param,self,file)
        self.addOrDiscard(success,command) 
        return success
    
    def addOrDiscard(self,success,command):
        if(success):
            self.successCommands.append(command)
            
    def successCommandCount(self):
        return self.successCommands.__len__()
    
    def getSuccessCommands(self):
        return self.successCommands
    
    def showData(self,data):
        print(data)
        
    def getKernel(self):
        return self.kernel
    
    def programs(self):
        return self.kernel.getDisk().getProgramas().keys()