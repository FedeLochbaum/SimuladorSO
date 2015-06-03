from enum import Enum


class Irq(Enum):
    kill='Kill'
    timeOut='TimeOut'
    newProcess='New Process'
    io='IO'
    
  
