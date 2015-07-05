from clases.MemoryManager import MemoryManager
class MMUPaginacion(MemoryManager):
    
    def __init__(self,memory):
        MemoryManager.__init__(self,memory)
        #asumiendo que creo la memoria logica aca pasandole el tamaño de sus bloques o paginas(igual al de los marcos de la memoria)
        self.memoryLogic = MemoryLogic(memory.sizeFrame())
        self.pageTable = {}
        #esta emptysFrame nose si va. pero seria los marcos libres
        self.EmptysFrame = {}
        
    def loadProgram(self,program):
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