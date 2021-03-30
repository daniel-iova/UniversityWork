from Calculator import Calculator
from ServiciuImprimare import ServiciuImprimare
from DataGenerator import DataGenerator
from random import shuffle

def Simulate(dataGenerator : DataGenerator):
    #-------------------------------------------------------------------------------
    # Setting up the printing service
    #-------------------------------------------------------------------------------
    serviciuImprimare = ServiciuImprimare()
    serviciuImprimare.SetPPMValue(dataGenerator.GenRandomPPMList())
    
    #-------------------------------------------------------------------------------
    # Setting up the computer list
    #-------------------------------------------------------------------------------
    calcList = []
    for i in range(80):
        calcList.append(Calculator(i))
    shuffle(calcList) # shuffle so we have random computer order

    #-------------------------------------------------------------------------------
    # Setting up the request and starting times lists
    #-------------------------------------------------------------------------------
    requestList = []
    startingTimes = []
    timeTracker = 0
    for calc in calcList:
        requestList, startingTimes = calc.TrimiteCerereImprimare(dataGenerator, requestList, startingTimes, timeTracker - 1)
        timeTracker = startingTimes[-1] + 1 # timeTracker is updated with the value after the last generated one
    
    #-------------------------------------------------------------------------------
    # Executing the printing requests
    #-------------------------------------------------------------------------------
    serviciuImprimare.Execute(requestList, startingTimes, 0)

if __name__ == '__main__':
    dataGenerator = DataGenerator()
    Simulate(dataGenerator)
