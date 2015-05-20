from clases.SchedullingPolitic import SchedullingPolitic


class PriorityPolitic(SchedullingPolitic):

    def __init__(self,queuesManager):
        SchedullingPolitic.__init__(self,queuesManager)



    def next(self):
        return self.queuesManager.getReadyQueue().get()
    