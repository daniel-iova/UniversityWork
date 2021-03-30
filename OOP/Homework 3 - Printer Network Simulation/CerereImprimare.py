from Calculator import Calculator
from Document import Document
from math import ceil

class CerereImprimare():
    """Request Class"""
    def __init__(self, sender : Calculator, doc : Document, timestamp):
        self.sender = sender # sender computer
        self.doc = doc # document
        self.timestamp = timestamp # value that holds the starting minute of the request
        self.finishTime = -1 # holds the finish minute of the request; will be computed when executing

    def ExecTimeForImp(self, ppm):
        """Returns the number of minutes it takes to execute the current request with the given ppm value."""
        # We return the result of the following formula : ceil(numPages / ppm)
        return ceil(self.doc.numberOfPages / ppm)