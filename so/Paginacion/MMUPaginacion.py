from Paginacion.LogicMemory import LogicMemory
from clases.MemoryManager import MemoryManager


class MMUPaginacion(MemoryManager):
    
    def __init__(self,memory):
        MemoryManager.__init__(self,memory)
        #asumiendo que creo la memoria logica aca pasandole el tamańo de sus bloques o paginas(igual al de los marcos de la memoria)
        self.logicMemory = LogicMemory(memory.sizeFrame())
        self.physicalMemory=memory
        self.pageTable = {}
        #esta emptysFrame nose si va. pero seria los marcos libres
        #self.EmptysFrame = {} Esto va en la memoria fisica
        
    def loadProgram(self,program):
        if(self.hayMemoriaSuficiente(program)):
            self.logicMemory.setandLoadPages(program)
            for page in program.pages():
                #frame = self.physicalMemory.get   los frames ya estarain cargados, lo que hay que ahces es setearle la page
                #creo que pop podria sacar el elemento tambien
                logicDir=self.logicMemory.get(page)
                frame=self.pageTable[logicDir]
                frame.setPage(page)
                #self.loadInMemory(page)  El setPage haria lo de loadInMemory
     
        
    def loadInMemory(self,page):
        frame = self.pageTable(page.number())
        inicial = frame.baseDir()
        for instruction in page.instructions():
            if(inicial <= frame.finalDir()):
                self.physicalMemory.put(inicial,instruction)
                inicial = inicial+1