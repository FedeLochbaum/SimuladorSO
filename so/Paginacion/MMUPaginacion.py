import logging

from Paginacion.LogicMemory import LogicMemory
from clases.MemoryManager import MemoryManager


class MMUPaginacion(MemoryManager):
    
    def __init__(self,memory):
        MemoryManager.__init__(self,memory)
        self.logicMemory = LogicMemory(memory.getTotalSpace(),memory.sizeFrame)
        self.physicalMemory=memory
        self.pageTable = {}

        
    def loadProgram(self,program):
        logging.debug('Trying to add %s instructions to memory' % program.getName())
        if(self.hayMemoriaSuficiente(program)):
            self.logicMemory.setandLoadPages(program)
            for page in program.getPages():
                frame = self.physicalMemory.getFrame()
                self.pageTable[page.getLogicDir()] = frame.getBaseDir()
                self.loadInMemory(page,frame)
            logging.debug('Succesfully added %s instructions to memory' % program.getName())
            return True
        logging.debug('Failed no memory to add %s instructions to memory' % program.getName())
        return False
                
    def hayMemoriaSuficiente(self,program):
        return self.memoryFree() >= program.getInstructionsCount()
        
    def loadInMemory(self,page,frame):
        frameDir = frame.getBaseDir()
        frameFinalDir = frame.getEnd()
        for instruction in page.getInstructions():
            if(frameDir <= frameFinalDir):
                self.physicalMemory.put(frame,instruction)
                frameDir +=1
                
    def getInstruction(self,dirPage,dez):
        dirFrame = self.pageTable[dirPage]
        frame = self.physicalMemory.get(dirFrame)
        return frame.getInstructions()[dez]
      
    def isFinalInPage(self,dirPage,dez):
        dirFrame = self.pageTable[dirPage]
        frame = self.physicalMemory.get(dirFrame)
        #se fija si es la ultima instruccion.. si es none es porque ya paso por todas las inst
        return None == frame.getInstructions()[dez]  
    
    def cleanMemory(self,procces):
        logging.debug('Cleaned process %s instructins from Memory' % procces.getName())
        for dirPage in procces.getDirsPage():
            dirFrame = self.pageTable[dirPage]
            self.physicalMemory.removeFromFrame(dirFrame)
            
    def esContinua(self):
        return False
            