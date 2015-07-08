from Paginacion.LogicMemory import LogicMemory
from clases.MemoryManager import MemoryManager


class MMUPaginacion(MemoryManager):
    
    def __init__(self,memory):
        MemoryManager.__init__(self,memory)
        #asumiendo que creo la memoria logica aca pasandole el tamańo de sus bloques o paginas(igual al de los marcos de la memoria)
        self.logicMemory = LogicMemory(memory.getTotalSpace(),memory.sizeFrame)
        self.physicalMemory=memory
        self.pageTable = {}
        #esta emptysFrame nose si va. pero seria los marcos libres
        #self.EmptysFrame = {} Esto va en la memoria fisica
        
    def loadProgram(self,program):
        if(self.hayMemoriaSuficiente(program)):
            self.logicMemory.setandLoadPages(program)
            for page in program.getPages():
                frame = self.physicalMemory.getFrame()
                #creo que pop podria sacar el elemento tambien
                #logicDir=self.logicMemory.get(page)
                self.pageTable[page.getLogicDir()] = frame.getBaseDir()
                self.loadInMemory(page)
                
    def hayMemoriaSuficiente(self,program):
        return self.memoryFree() >= program.getInstructionsCount()
        
    def loadInMemory(self,page):
        frameDir = self.pageTable[page.getLogicDir()]
        print(frameDir)
        frameFinalDir = (frameDir + self.physicalMemory.getSizeFrame()) -1
        print(frameFinalDir)
        print(page.getInstructions())
        for instruction in page.getInstructions():
            if(frameDir <= frameFinalDir):
                self.physicalMemory.put(frameDir,instruction)
                frameDir +=1