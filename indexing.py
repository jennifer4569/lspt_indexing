import heapq

# indexing: token, priority queue of documents
indexes = {}

# calculates to document score
# NOTE: THIS IS TEMPORARY CODE, should include weights of the document itself
def getDocScore(document):
    return ord(document[0])

# adds the document to the token index's priority queue
def addIndex(token, document):
    # higher score means greater priority
    priority = getDocScore(document) * -1

    # if the token doesn't exist, add the token in, initializing its priority queue
    if(not token in indexes):
        indexes[token] = []

    # adds the document into the respective token's priority queue
    heapq.heappush(indexes[token], (priority, document))

def getTopNDocs(token, n = 1):
    docs = []
    for doc in heapq.nlargest(n, indexes[token]):
        docs.append(doc[1])
    return docs

def getAllDocs(token):
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
    indexes = {}