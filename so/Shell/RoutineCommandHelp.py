from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command
import logging


class RoutineCommandHelp(RoutineCommand):
    MESSAGE='Bienvenido a la ayuda del Sistema Operativo, tiene los siguientes comando disponibles:\n-help,-?,-load,-ls,-show\n'
    #Modificar texto

    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.help1.value or command==Command.help2.value or command==Command.help3.value 
    
    def handle(self,command,param=None ,shell=None,file=None):
        logging.debug('Executed help command')
        RoutineCommand.handle(self, command,shell,file)
        return self.MESSAGE
        

        