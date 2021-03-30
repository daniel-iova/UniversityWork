from CerereImprimare import CerereImprimare

class CoadaDocumente():
    """Job Queue Class"""
    def __init__(self):
        self.jobQueue = [] # job queue, which holds CerereImprimare objects
        self.minRamase = 0 # holds the number of remaining minutes until all the requests are completed
        self.isWorking = False # bool flag that states whether the queue is empty or not
    
    def Push(self, cerereImprimare : CerereImprimare):
        """Appends the given request to the job queue and sets the queue as active."""
        self.isWorking = True
        self.jobQueue.append(cerereImprimare)
    
    def Pop(self):
        """Pops an element at the start."""
        popped = self.jobQueue.pop(0)

        # If the queue is empty, set the isWorking flag to false
        if self.Length() == 0:
            self.isWorking = False
        
        return popped

    def Length(self):
        """Returns the length of the job queue."""
        return len(self.jobQueue)