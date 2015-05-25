from clases.IrqHandler import IrqHandler


class IrqKill:

    def __init__(self,IrqHandler,pcb):
        pass
        self.handler = IrqHandler
        self.pcb = pcb
        self.execute()
    
    def execute(self):
        pass 
        #TODO : aca decirle de alguna forma que la memoryManager borre todas las intrucciones de pcb
        self.handler.next() #TODO : handler lo que hace aca es pedir el sig y asignarlo al cpu pero para eso.. deberia conocer al scheduller
        