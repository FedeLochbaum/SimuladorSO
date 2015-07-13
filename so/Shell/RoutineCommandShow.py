from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command
import logging


class RoutineCommandShow(RoutineCommand):
    

    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.show.value 
    
    def handle(self,command,param=None ,shell=None,file= None):
        logging.debug('Executed Show %s' %file)
        RoutineCommand.handle(self, command,shell,file)
        shell.showData(open(file,"rb").read())
        