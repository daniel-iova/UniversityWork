from Calculator import Calculator
import random
from CerereImprimare import CerereImprimare
from Document import Document

class DataGenerator():
    """Data Generator Class"""
    def __init__(self):
        # self.types is a dictionary where:
        # - keys : tuples of document types
        # - values : number of pages for the specific types, having a default value of 1 
        self.types = {
            tuple(["Fotografie", "Certificat", "Adeverinta", "Trimitere", "Diploma"]) : 1,
            tuple(["CV", "Contract"]) : 1,
            tuple(["Lucrare Stiintifica", "Licenta"]) : 1,
            tuple(["Revista", "Ziar"]) : 1,
            tuple(["Carte", "Caiet"]) : 1
        }
    def GenRandomPPMList(self):
        """Generates a list of 4 random pages/min (ppm) values for the 4 printers."""
        return [random.randint(3, 20),
                random.randint(3, 20),
                random.randint(3, 20),
                random.randint(3, 20)
                ]
    
    def GenerareTimpEmitere(self, timpPrecedent):
        """Generates a random time starting from the previous minute + 1"""
        return random.randint(timpPrecedent + 1, timpPrecedent + random.randint(1, 5))

    def GenDocTypeAndNumPgs(self):
        """Generates a random document type and a number of pages associated with it."""

        # We assign a random value corresponding to the number of pages for each document type
        # i.e. a CV or a Contract can have from 1 to 4 pages
        # the first doc types will always have 1 page, so no need to reassign
        self.types[list(self.types.keys())[1]] = random.randint(1, 4)
        self.types[list(self.types.keys())[2]] = random.randint(10, 40)
        self.types[list(self.types.keys())[3]] = random.randint(5, 100)
        self.types[list(self.types.keys())[4]] = random.randint(30, 400)

        # We then choose a random tuple of doc types and a random type from the chosen tuple
        # Finally we return the random type and the number of pages 
        key = random.choice(list(self.types.keys()))
        randomType = random.choice(key)
        return randomType, self.types[key]
    
    def GenRequestList(self, id, requestList, startingTimes, timeOffset):
        """Updates and returns the given request list and starting times list based on the given time offset."""
        # Start from an issuance time of 0, and a random number of generated requests between 1 and 3.
        timpEmitere = 0
        numarCereri = random.randint(1, 3)

        for i in range(0, numarCereri):
            # Generate document type and number of pages using the GenDocTypeAndNumPgs method
            type, numPgs = self.GenDocTypeAndNumPgs()

            # Update the issuance time
            timpEmitere = self.GenerareTimpEmitere(timpEmitere)

            # Expand the requestList and startingTimes lists using the generated values
            # The timeOffset variable is used to avoid non-sequential generation
            # So the request starting time becomes : timpEmitere + timeOffset
            startingTimes.append(timpEmitere + timeOffset)
            requestList.append(CerereImprimare(Calculator(id), # Calculator object with given parameter id
                                Document(numPgs, type, i), # Document object with the generated numPgs, type, and id i
                                timpEmitere + timeOffset)) # timestamp value equal to the starting time described above
        
        # Return the updated requestList and startingTimes
        return requestList, startingTimes