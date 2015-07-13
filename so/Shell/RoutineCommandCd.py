from os.path import os

from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command
import logging


class RoutineCommandCd(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.cd.value 
    
    def handle(self,command,param=None ,shell=None,file= None):
        logging.debug('Executed cd %s' % file)
        RoutineCommand.handle(self, command,shell,file)
        if(os.path.exists(file)):
            os.chdir(file) 
    