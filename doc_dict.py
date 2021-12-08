class DocDict(object):
    docs = {}
    # constructor
    
    def addDocument(self, document):
        self.docs[document.docName] = document
    def removeDocument(self, docID):
        self.docs.pop(docID)
    def getDocument(self, docID):
        return self.docs[docID]
    def checkIfDocExists(self, docID):
        if docID in self.docs:
            return True
        else:
            return False
    def clearDict(self):
        self.docs.clear()