class Instruction:
    
    def __init__(self,message,resource=None):
        self.message=message
        self.resource=resource

    def execute(self):
        pass
        
    def getMessage(self):
        return self.message
    
    def isIO(self):
        pass
    
    def getResource(self):
        return self.resource