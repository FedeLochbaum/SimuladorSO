from queue import Queue
class FIFOReadyQueue:

    def __init__(self):
        self.readyQueue = Queue()

    def put(self,elemet):
        self.readyQueue._put(elemet)

    def get(self,element):
        self.readyQueue._get()
        