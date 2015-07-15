import glob
import logging
from os.path import os

from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandLs(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.ls.value 
    
    def handle(self,command,param= None ,shell=None,file= None):
        logging.debug('Executed Ls command')
        RoutineCommand.handle(self, command,shell,file)
        list = []
        for p in os.listdir(os.getcwd()):
            if(not (p.startswith("install") or p.startswith("eula") or p.startswith("."))):
                list.append(glob.glob(p))
        return list