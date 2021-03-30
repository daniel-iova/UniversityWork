import math

class OutputHandler():
    """Output Handling Class"""
    def __init__(self):
        self.outf = open("out.txt", "w") # output file

    def PrintTimeTracker(self, timeTracker):
        """Prints the current minute."""
        print (f"MINUTUL {timeTracker}\n", file = self.outf)

    def PrintStatus(self, imp, operation, cerere):
        """Prints a push or pop status."""
        # imp - given printer
        # operation - given string containing what happened : "a inceput", "a terminat"
        # cerere - given request

        # "finishedPages" = variable which changes the format when a doc is finished to show that all pages were completed (i.e. 23/23, 85/85)
        finishedPages = ""
        if (operation == "a terminat"):
            finishedPages = f"{cerere.doc.numberOfPages}/"

        print(f"Imprimanta #{imp.id} ({imp.ppm} pagini/min) {operation} documentul #{cerere.doc.id} al Calculatorului #{cerere.sender.uniqueId} ({finishedPages}{cerere.doc.numberOfPages} pagini)\n"  , file = self.outf)
        # Example of start  : Imprimanta #1 (8 pagini/min) a inceput documentul #2 al Calculatorului #27 (1 pagini)
        # Example of finish : Imprimanta #3 (11 pagini/min) a terminat documentul #0 al Calculatorului #65 (238/238 pagini)

    def PrintIndividualRequest(self, index, imp, cerere):
        """Prints an individual request."""

        numPag = cerere.doc.numberOfPages # number of pages of given request's document
        ppm = imp.ppm # pages per minute value of the given printer
        finishTime = cerere.finishTime # request's finish time
        paginiDone = ppm * (math.ceil(numPag/ppm) - finishTime) # use the formula to compute number of done pages

        # Edge case : Execution hasn't started, so number of done pages must stay 0 until it gets executed
        if paginiDone < 0:
            paginiDone = 0
        
        print (f"\n\t\t{index} : [ Calculatorul: #{cerere.sender.uniqueId}, Documentul: #{cerere.doc.id}, Tip: {cerere.doc.type}, Status: {finishTime}m left, Pagini procesate: {paginiDone}/{cerere.doc.numberOfPages} ] ", end = ' ', file = self.outf)
        # Example :  0 : [ Calculatorul: #40, Documentul: #1, Tip: Caiet, Status: 2m left, Pagini procesate: 220/247 ]

    def PrintPrinterStatus(self, serviciu):
        """Prints the status of the four printers of the given printing service."""
        print ("STATUS IMPRIMANTE", file = self.outf)

        # Iterates through the given service's printers
        for imp in serviciu.impr:
            print (f"\n\tImprimanta #{imp.id} cu ({imp.ppm} pagini/min) are in queue: ", end = '', file = self.outf)
            # The index signals the individual requests' positions in the job queue
            index = 0
            # We print all requests that each printer has in queue and increment the index
            for cerere in imp.coadaDoc.jobQueue:
                self.PrintIndividualRequest(index, imp, cerere)
                index += 1
            print('', file = self.outf)
        print('\n', file = self.outf)