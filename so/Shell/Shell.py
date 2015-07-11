from os.path import os


class Shell():

    def __init__(self, kernel,commandHandler):
        self.kernel=kernel
        self.commandHandler=commandHandler
        self.successCommands=[]
        os.chdir("C:/")
        self.root = os.getcwd()
        
    def readCommand(self,param =None,command,file=None):
        success=self.commandHandler.handle(command,param,self,self.kernel,file)
        self.addOrDiscard(success,command) 
        return success
    
    def addOrDiscard(self,success,command):
        if(success):
            self.successCommands.append(command)
            
    def successCommandCount(self):
        return self.successCommands.__len__()
    
    def getSuccessCommands(self):
        return self.successCommands
    
    def showFiles(self,list):
        print(list)