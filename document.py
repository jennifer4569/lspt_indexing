class Document:
    docName = ""

    # constructor
    def __init__(self, name, numWords):
        self.docName = name
        self.numWords = numWords

    # TEMPORARY -- NEED TO ACTUALLY CALCULATE DOC SCORE
    # assuming calculateDocScore takes in a dictionary of form
    """      {
            "title": 1, 
            "headers": 2, 
            "links": 0,
            "other": 2
        } """
    def calculateDocScore(self, tokenInfo):
        #if certain information isn't available
        raise Exception("Not enough information to calculate score")
        return ord(self.docName[0])