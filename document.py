class Document:
    docName = ""

    # constructor
    def __init__(self, name):
        self.docName = name

    # TEMPORARY -- NEED TO ACTUALLY CALCULATE DOC SCORE
    def calculateDocScore(self, token):
        return ord(self.docName[0])