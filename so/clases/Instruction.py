class Instruction:
    
    def __init__(self,message,window):
        self.message=message
        self.window=window

    def execute(self):
        self.window.show(self.getMessage())
        
    def getMessage(self):
        return self.message
