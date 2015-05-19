from concurrent.futures._base import RUNNING
from ctypes.test.test_errno import threading
import sys
import time


class trhead(threading.Thread):
    RUNNING = True
    
    def run(self):
        while RUNNING:
            print('thread')
            sys.stdout.flush()
            time.sleep(0.1)
            
    def signal_handler(self,signal,fram):
        global RUNNING
        print('\nyou pressed Ctrl+C!')
        RUNNING = False
        
        ''' Esto no va a ir en el futuro, esto va a ser de la cpu, que va a ser un Thread''' 