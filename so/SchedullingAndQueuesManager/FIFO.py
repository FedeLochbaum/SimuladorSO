from SchedullingAndQueuesManager.SchedullingPolitic import SchedullingPolitic


class FIFO(SchedullingPolitic):
    def __init__(self,queuesManager):  
        SchedullingPolitic.__init__(self, queuesManager)        

  
