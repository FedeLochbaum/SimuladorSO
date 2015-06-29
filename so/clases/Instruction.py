class Instruction:
    
    def __init__(self,message,resource):
        self.message=message
        self.resourse=resource

    def execute(self):
        self.resourse.show(self.getMessage())
        
    def getMessage(self):
        return self.message
    
    def isIO(self):
        pass
    
    def getResource(self):
        return self.resourse