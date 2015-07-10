from enum import Enum


class Command(Enum):
    help1='?'
    help2='help'
    help3='man'
    cd = 'cd'
    show = 'show'
    ls = 'ls'
    load = 'load'
