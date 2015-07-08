
class Disk:

    def __init__(self):
        self.programs = {}

    def getProgram(self,programName):
        if(self.programs[programName] == None):
            print('no existe ese programa en el Disco')
            return;
        return self.programs[programName]  

    def addProgram(self,program):
            self.programs[program.getName()] = program

    def removeProgram(self, nameProgram):
            self.programs[nameProgram] = None
            
    def getProgramas(self):
        return self.programs


