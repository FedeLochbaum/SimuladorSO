from os.path import os

from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandCd(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.cd.value 
    
    def handle(self,command,param=None ,shell=None,kernel=None,file= None):
        RoutineCommand.handle(self, command,shell,kernel,file)
        if(os.path.exists(file)):
            os.chdir(file) 
    