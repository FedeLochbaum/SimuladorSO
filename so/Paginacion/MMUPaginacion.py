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
        self.EmptysFrame = {}
        
    def loadProgram(self,program):
        if(self.hayMemoriaSuficiente(program)):
            self.logicMemory.setandLoadPages(program)
            for page in program.pages():
                frame = self.EmptysFrame.pop()
                #creo que pop podria sacar el elemento tambien
                self.pageTable[page.number()] = frame
                self.loadInMemory(page)
        '''
        #lo deje aca porque no sabia que debia verificar aca te dejo una serie de cosas que creo que deberian pasar:
        #preguntar si hay memoria..(ya sea para todo el program o una instrucicon))
        #pedir la direccion fisica y asignar la memoria
        # guardar la/las paginas usadas en el programa
        #para hacer lo de saber la direccion fisica.. habria que ver que ahcemos o como asignamos a la tabla de paginas
        
        #pd : hoy domingo no ovya  poder codear hasta la noche si podes avanzar avanza TODO lo posible... 
        #pdd: no parece ser tanto como asignacion continua pero hay que contemplar mas cosas 
        #pddd : PUTO ;)  asi no te olvidas de lo que sos 
        '''
        
    def loadInMemory(self,page):
        frame = self.pageTable(page.number())
        inicial = frame.baseDir()
        for instruction in page.instructions():
            if(inicial <= frame.finalDir()):
                self.physicalMemory.put(inicial,instruction)
                inicial = inicial+1