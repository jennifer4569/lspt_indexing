from document import Document
from indexing import *
from indexing import docDict



#processIncomingData(docId, numWords, wordDict)
#adds a document to the index through its contained tokens
# inputs:
#   docID (string): the uid document for the document
#   numWords (integer): the number of words in the document
#   wordDict (dictiorary): contained in document along with positional info
# modifies: adds to index
# returns: none  

def processIncomingData(docID, numWords, wordDict):
    #use document class to create document score.
    #check DoctDic
    doc = Document(docID, numWords)
    exists = docDict.checkIfDocExists(docID)
    #some low score we can assign words with improper information so that they can still be indexed, albeit, not accurately
    #this should probaly be adjusted or relative somehow
    defaultScore = 0.1
    for word, positions in wordDict.items():
        try:
            wordScore = doc.calculateDocScore(positions)
        except Exception as e:
            print("Word: {} doesn't have enough information to calculate score. Indexing word with low priority")
            #going to index the word low
            wordScore = defaultScore
        if (exists):
            #this is still being worked on
            updateDoc()
            doc.addToken(word, positions)
        else:
            addIndex(word, docID, wordScore)
    #after document is completed, add doc to DocDic
    docDict.addDocument(doc)

        


# getDocsAnd(tokens, start, n)
#returns the information for <=n documents which contain all inputted tokens
# inputs:
#   tokens (List[string]): A list of words
#   start (integer): the point in index priority where we should start searching for results
#   n (integer): the number of document results requested
# modifies: none
# returns: list of documents objects and their scores
def getDocsAnd(tokens, start, n):
    tokenDict = {}
    docsDict = {}
    first = True
    #compile a set of documents, sharedDocSet, which only contain the inputted tokens
    for token in tokens:
        #(priority, doc, positions)
        tokenDict[token] = getAllDocs(token)
        docList = []
        for docTup in tokenDict[token]:
            #docTup[1] is a doc object
            docList.append(docTup[1])
            docsDict.setdefault(docTup[1], []).append(docTup)
        #turn docList into a set and then compare it with the main set
        if first:
            sharedDocSet = set(docList)
            first = False
        else:
            sharedDocSet = sharedDocSet.intersection(set(docList))
    #for each document in sharedDocSet, run through docsDict and compile total score 
    docsAndScores = []
    #doc is a doc object
    for doc in sharedDocSet:
        totalDocScore = sum(i[0] for i in docsDict[doc])
        docsAndScores.append(doc, totalDocScore)
    #sort list by score
    docsAndScores.sort(key=lambda x: x[1])
    return docsAndScores[ start: n]
    

# getDocsOr(tokens, start, n)
#returns a dictionary with tokens as keys. Values <=n  of documents which contain the token, sorted by score
# inputs:
#   tokens (List[string]): A list of words
#   start (integer): the point in index priority where we should start searching for results
#   n (integer): the number of document results requested
# modifies: none
# returns: a dictionary, key = token, value = (wordScore, docObject, positionsDict))
def getDocsOr(tokens, start, n):
    allDocs = {}
    #use score addition to decide the order in which documents are returned
    #TODO: add exception handling
    for token in tokens:
        allDocs[token] = getTopNDocs(token, n)

    return allDocs

    """ nDocs = []
    for docI in heapq.merge(docI for docI in allDocs):
        nDocs.append(docI)
        if len(nDocs)== n: return nDocs

    return nDocs """

