import heapq
from document import Document

# indexingData dictionary: key is the token, value is the priority queue of documents
indexingData = {}

# addIndex(token, doc): adds the document to indexes, based on the token
# 
# inputs: token (string): the token to add the document in
#         doc (Document): the document to add to indexes
#         indexes (dictionary): the indexing data to apply this change to -- defaults to indexingData
# modifies: indexes
# returns: none
# notes: none
def addIndex(token, doc, indexes = indexingData):
    # if the token doesn't exist, add the token in, initializing its priority queue
    if(not token in indexes):
        indexes[token] = []

    # higher score means greater priority
    priority = doc.calculateDocScore(token) * -1

    # adds the document into the respective token's priority queue
    heapq.heappush(indexes[token], (priority, doc))

# getTopNDocs(token, n): gets the top n documents associated with the given token
#
# inputs: token (string): the token to get the top n documents from
#         n (integer): the number of top documents to retrieve from the respective token
#         indexes (dictionary): the indexing data to apply this change to -- defaults to indexingData
# modifies: none
# returns: a list of Documents, containing the top n documents of the token
# notes: none
def getTopNDocs(token, n = 1, indexes = indexingData):
    # if the token doesn't exist, raise exception
    if(not token in indexes):
        raise(KeyError)
    
    # loop through and return the top n documents associated with the token
    docs = []
    for doc in heapq.nlargest(n, indexes[token]):
        docs.append(doc[1])
    return docs

# getAllDocs(token): gets all the documents associated with the given token
#
# inputs: token (string): the token to get all the documents from
#         indexes (dictionary): the indexing data to apply this change to -- defaults to indexingData
# modifies: none
# returns: a list of Documents, containing all the documents associated with the token
# notes: none
def getAllDocs(token, indexes = indexingData): 
    # if the token doesn't exist, raise exception
    if(not token in indexes):
        raise(KeyError)

    # loop through and return all the documents associated with the token
    docs = []
    for doc in heapq.nlargest(len(indexes[token]), indexes[token]):
        docs.append(doc[1])
    return docs

# getAllTokens(): gets all the indices stored in indexes
#
# inputs: indexes (dictionary): the indexing data to apply this change to -- defaults to indexingData
# modifies: none
# returns: a list of strings, containing all the tokens stored in indexes
# notes: none
def getAllTokens(indexes = indexingData):
    tokens = []
    for token in indexes:
        tokens.append(token)
    return tokens

# clearIndexes(): clears all the indexing data that has been stored
#
# inputs: indexes (dictionary): the indexing data to apply this change to -- defaults to indexingData
# modifies: indexes
# returns: none
# notes: none
def clearIndexes(indexes = indexingData):
    indexes.clear()