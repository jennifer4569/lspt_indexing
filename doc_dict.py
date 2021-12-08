class DocDict(object):
    docDict = {}
    # constructor
    
    def addDocument(document, docs = docDict):
        docs[document.name] = document
    def removeDocument(docID, docs = docDict ):
        del docs[docID]
    def getDocument(docID, docs = docDict):
        return docs[docID]
    def checkIfDocExists(docID, docs = docDict):
        if docID in docs:
            return True
        else:
            return False



