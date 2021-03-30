from CerereImprimare import CerereImprimare
from CoadaDocumente import CoadaDocumente

class Imprimanta():
    """Printer Class"""
    def __init__(self, id):
        self.id = id # printer id
        self.ppm = -1 # pages per min number, assigned by a DataGenearator object
        self.coadaDoc = CoadaDocumente() # CoadaDocumente object which holds the requests

    def TotalMinsWithCerere(self, ci : CerereImprimare):
        """Returns the total time it takes to execute the given request for the current printer."""
        # The formula is : execTimeForPrinter + minRamase
        return ci.ExecTimeForImp(self.ppm) + self.coadaDoc.minRamase