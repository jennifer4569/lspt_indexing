import heapq
from document import Document
from doc_dict import DocDict
# indexingData dictionary: key is the token, value is the priority queue of documents
indexingData = {}
docDict = DocDict()

# addIndex(token, doc): adds the document to indexes, based on the token
# 
# inputs: token (string): the token to add the document in
#         doc (Document): the document to add to indexes
#         indexes (dictionary): the indexing data to add this document to -- defaults to indexingData
#         score (integer): score of the token within document-- to be used as priority in heap
#         positions (dictionary): gives frequencies for "title", "headers",  "links", and "other"
# modifies: indexes
# returns: none
# notes: none
def addIndex(token, docId, score, positions, indexes = indexingData):
    # if the token doesn't exist, add the token in, initializing its priority queue
    if(not token in indexes):
        indexes[token] = []

    # higher score means higher priority -- heapq prioritizes lower priority
    priority = score * -1

    # adds the document into the respective token's priority queue
    heapq.heappush(indexes[token], (priority, docId)) #(priority, doc, positions))

# getTopNDocs(token, n): gets the top n documents associated with the given token
#
# inputs: token (string): the token to get the top n documents from
#         n (integer): the number of top documents to retrieve from the respective token
#         indexes (dictionary): the indexing data to get docs from -- defaults to indexingData
# modifies: none
# returns: a list of Documents, containing the top n documents of the token
# notes: returns empty list if the token doesn't exist
def getTopNDocs(token, n = 1, indexes = indexingData):
    # if the token doesn't exist, return empty list
    if(not token in indexes):
        return []
    
    # loop through and return the top n documents associated with the token
    docs = []
    for doc in heapq.nlargest(n, indexes[token]):
        docId = doc[1]
        docs.append(getDocument(docId))
    return docs

# getAllDocs(token): gets all the documents associated with the given token
#
# inputs: token (string): the token to get all the documents from
#         indexes (dictionary): the indexing data to get docs from -- defaults to indexingData
# modifies: none
# returns: a list of Documents, containing all the documents associated with the token
# notes: returns empty list if the token doesn't exist
def getAllDocs(token, indexes = indexingData): 
    # if the token doesn't exist, return empty list
    if(not token in indexes):
        return []

    return getTopNDocs(token, len(indexes[token]), indexes)

# getAllTokens(): gets all the indices stored in indexes
#
# inputs: indexes (dictionary): the indexing data to get tokens from -- defaults to indexingData
# modifies: none
# returns: a list of strings, containing all the tokens stored in indexes
# notes: none
def getAllTokens(indexes = indexingData):
    tokens = []
    for token in indexes:
        tokens.append(token)
    return tokens

# updateDoc(token, doc, indexes): updates the document with its new document score
#
# inputs: token (string): the token associated with the given document 
#         doc (Document): the document to update
#         indexes (dictionary): the indexing data to apply this update to -- defaults to indexingData
# modifies: indexes
# returns: none
# notes: raises KeyError if the token doesn't exist
#        raises LookupError if the document doesn't exist within the token
def updateDoc(token, doc, indexes = indexingData):
    pass

# clearIndexes(): clears all the indexing data that has been stored
#
# inputs: indexes (dictionary): the indexing data to clear -- defaults to indexingData
# modifies: indexes
# returns: none
# notes: none
def clearIndexes(indexes = indexingData):
    indexes.clear()