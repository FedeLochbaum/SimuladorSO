from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command
import logging


class RoutineCommandLoad(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.load.value 
    
    def handle(self,command,param= None ,shell=None,file= None):
        logging.debug('Executed Load %s' % str(param))
        RoutineCommand.handle(self, command,shell,file)
        param=str(param)
        return shell.getKernel().loadProgram(param)
        