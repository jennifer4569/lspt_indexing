from .. import indexing
from .. document import Document

# getAllDocNames(docs): gets all the names from all the documents in docs
#
# inputs: docs (list of Documents): the list of documents to retrieve the document names from
# modifies: none
# returns: a list of string, containing all the document names from docs
# notes: none
def getAllDocNames(docs):
    docNames = []
    for doc in docs:
        docNames.append(doc.docName)
    return docNames

# assertSameIndexingData(indexingDataA, indexingDataB): ensures that the two indexing datas given are the same
#
# inputs: indexingDataA (dictionary): the first indexing data to compare
#         indexingDataB (dictionary): the second indexing data to compara
# modifies: none
# returns: none
# notes: asserts that the two indexing datas are equal
#        indexing datas are considered equal if:
#          - they contain an equal amount of tokens
#          - all the tokens match (including ordering)
#          - the number of documents associated with each token are respectively equal
#          - the documents associated with each token are respectively equal (checked by document name)
def assertSameIndexingData(indexingDataA, indexingDataB):
    # ensure equal number of tokens
    allTokensA = indexing.getAllTokens(indexingDataA)
    allTokensB = indexing.getAllTokens(indexingDataB)
    assert len(allTokensA) == len(allTokensB)

    # ensure all tokens match (ordering as well)
    for i in range(len(allTokensA)):
        tokenA = allTokensA[i]
        tokenB = allTokensB[i]
        assert tokenA == tokenB
        
        # ensure equal number of documents
        allDocsA = indexing.getAllDocs(tokenA)
        allDocsB = indexing.getAllDocs(tokenB)
        assert len(allDocsA) == len(allDocsB)

        # ensure all documents match (ordering as well)
        allDocNamesA = getAllDocNames(allDocsA)
        allDocNamesB = getAllDocNames(allDocsB)
        
        for j in range(len(allDocsA)):
            assert allDocNamesA[j] == allDocNamesB[j]