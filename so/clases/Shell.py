

class Shell():

    def __init__(self, kernel,commandHandler):
        self.kernel=kernel
        self.commandHandler=commandHandler
        self.successCommands=[]
        
    def readCommand(self,command):
        success=self.commandHandler.handle(command)
        self.addOrDiscard(success,command) 
        return success
    
    def addOrDiscard(self,success,command):
        if(success):
            self.successCommands.append(command)
            
    def successCommandCount(self):
        return self.successCommands.__len__()
    
    def getSuccessCommands(self):
        return self.successCommands