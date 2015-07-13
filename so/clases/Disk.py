import logging

class Disk:

    def __init__(self):
        self.programs = {}
        logging.basicConfig(filename='logSo.log',level=logging.DEBUG)

    def getProgram(self,programName):
        logging.debug('getting program %s from disk ' % programName)
        if(self.programs[programName] == None):
            logging.debug('No progrma with that name')
            return;
        logging.debug('succesfully getting program: %s' % programName)
        return self.programs[programName]  

    def addProgram(self,program):
        logging.debug('added program %s' % program.getName())
        self.programs[program.getName()] = program

    def removeProgram(self, nameProgram):
        logging.debug('remvoed program %s' % nameProgram)
        self.programs[nameProgram] = None
            
    def getProgramas(self):
        return self.programs


