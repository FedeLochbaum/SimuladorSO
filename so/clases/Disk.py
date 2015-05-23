from clases.Program import Program
from _overlapped import NULL
class Disk:

    def __init__(self):
        self.programas = {}

    def getProgram(self,programName):
        if(self.programas[programName] == NULL):
            print('no existe ese programa en el Disco')
        return self.programas[programName]  
    
    def indexProgram(self, nameProgram):
        return self.programs.index(self.returnProgram(nameProgram))#nose que carajo es esto 

    def addProgram(self,program):
            self.programas[program.getName()] = program

    def removeProgram(self, nameProgram):
            self.programas[nameProgram] = None
            
    def getProgramas(self):
        return self.programs


