class Calculator():
    """Computer Class"""
    def __init__(self, uniqueId):
        self.uniqueId = uniqueId

    def TrimiteCerereImprimare(self, dataGenerator, requestList, startingTimes, timeTracker):
        """Updates and returns given request list and starting times list.\n
        Uses given timeTracker to correctly generate new elements for the two lists."""
        requestList, startingTimes = dataGenerator.GenRequestList(self.uniqueId, requestList, startingTimes, timeTracker)
        return requestList, startingTimes