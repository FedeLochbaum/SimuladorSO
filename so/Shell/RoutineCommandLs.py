from os.path import os

from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command
import logging


class RoutineCommandLs(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.ls.value 
    
    def handle(self,command,param= None ,shell=None,file= None):
        logging.debug('Executed Ls command')
        RoutineCommand.handle(self, command,shell,file)
        return os.listdir(os.getcwd())