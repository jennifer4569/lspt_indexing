import heapq
from document import Document
from doc_dict import DocDict

# indexingData dictionary: key is the token, value is the priority queue of document IDs
indexingData = {}

# docDict dictionary: key is the document ID, value is the respective Document
docDict = DocDict()

# addIndex(token, docID, score, indexes): adds the document to indexes, based on the token
# 
# inputs: token (string): the token to add the document in
#         docID (string): the ID of the document to add to indexes
#         score (double): score of the token within document-- to be used as priority in heap
#         indexes (dictionary): the indexing data to add this document to -- defaults to indexingData
# modifies: indexes
# returns: none
# notes: adds token to indexes if it doesn't already exist
def addIndex(token, docID, score, indexes = indexingData):
    # if the token doesn't exist, add the token in, initializing its priority queue
    if(not token in indexes):
        indexes[token] = []

    # adds the document into the respective token's priority queue
    heapq.heappush(indexes[token], (score, docID))

# getTopNDocs(token, n, indexes): gets the top n documents associated with the given token
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
        docID = doc[1]
        docs.append(docDict.getDocument(docID))
    return docs

# getAllDocs(token, indexes): gets all the documents associated with the given token
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

# getAllTokens(indexes): gets all the indices stored in indexes
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

# updateDoc(token, docID, score, indexes): updates the document with its new document score
#
# inputs: token (string): the token associated with the given document 
#         docID (string): the document to update
#         score (double): the new score
#         indexes (dictionary): the indexing data to apply this update to -- defaults to indexingData
# modifies: indexes
# returns: none
# notes: adds token if the token doesn't exist
#        adds document within the token if the document doesn't exist within the token
def updateDoc(token, docID, score, indexes = indexingData):
    # adds token if the token doesn't already exist
    if(not token in indexes):
        indexes[token] = []

    # searches for the document within the token's priority queue
    val = indexes.get(token)
    docExists = False
    for element in val:
        # found the document -- update score
        if(element[1] == docID):
            indexes[token].remove(element)
            heapq.heappush(indexes[token], (score, docID))
            docExists = True
            break

    # adds document if the document doesn't exist in the token
    if(not docExists):
        heapq.heappush(indexes[token], (score, docID))

# clearIndexes(): clears all the indexing data that has been stored, including docDict
#
# inputs: indexes (dictionary): the indexing data to clear -- defaults to indexingData
# modifies: indexes, docDict
# returns: none
# notes: clears both indexes and docDict
def clearIndexes(indexes = indexingData):
    indexes.clear()
    docDict.clearDict()