from os.path import os

from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandLs(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.ls.value 
    
    def handle(self,param =None, command,shell,kernel,file =None):
        RoutineCommand.handle(self, command)
        shell.showFiles(os.listdir(file))