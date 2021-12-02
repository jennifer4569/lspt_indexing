import heapq
from document import Document

# indexing: token, priority queue of documents
indexes = {}

# adds the document to the token index's priority queue
def addIndex(token, doc):
    # higher score means greater priority
    priority = doc.calculateDocScore(token) * -1

    # if the token doesn't exist, add the token in, initializing its priority queue
    if(not token in indexes):
        indexes[token] = []

    # adds the document into the respective token's priority queue
    heapq.heappush(indexes[token], (priority, doc))

def getTopNDocs(token, n = 1):
    if(not token in indexes):
        raise(KeyError)
    docs = []
    for doc in heapq.nlargest(n, indexes[token]):
        docs.append(doc[1])
    return docs

def getAllDocs(token):
    if(not token in indexes):
        raise(KeyError)
    docs = []
    for doc in heapq.nlargest(len(indexes[token]), indexes[token]):
        docs.append(doc[1])
    return docs

def getAllTokens():
    tokens = []
    for token in indexes:
        tokens.append(token)
    return tokens

def clearIndexes():
    indexes.clear()