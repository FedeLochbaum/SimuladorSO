from os.path import os

from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandCd(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.cd.value 
    
    def handle(self,param =None, command,shell,kernel,file):
        RoutineCommand.handle(self, command)
        if(os.path.exists(file)):
            os.chdir(file) 
    