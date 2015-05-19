class Disk:

    def __init__(self):
        self.programs = []

    def getProgram(self, programName):
        
        for program in self.programs:
            if program.getName()==programName:
                return program    
        return;   
    
    def indexProgram(self, nameProgram):
        return self.programs.index(self.returnProgram(nameProgram))

    def addProgram(self, program):
            self.programs.append(program)

    def removeProgram(self, nameProgram):
            self.programs.pop(self.indexProgram(nameProgram))
            
    def getProgramas(self):
        return self.programs

