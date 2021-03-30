class Document():
    """Document Class"""
    def __init__(self, numberOfPages = 1, type = "blankPage", id = -1):
        self.numberOfPages = numberOfPages # number of pages of the doc
        self.type = type # type of doc
        self.id = id # id of doc