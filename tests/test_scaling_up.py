# run tests with pytest
from .. import indexing
from .. document import Document
import util_functions
import pytest
import test_indexing
import time

# test indexing time efficiency
def test25():
    # initial setup
    indexing.clearIndexes()

    # steps
    start = time.time()
    for i in range(100):
        n = i + 1
        token = str(n)
        for j in range(10*n):
            docName = token + "," + str(j)
            indexing.addIndex(token, Document(docName))
    end = time.time()
    
    # verifying test by checking timer
    secondsTaken = end - start
    assert secondsTaken < 3

    # verifying test by checking indexing data
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 100
    for i in range(100):
        n = i + 1
        token = str(n)
        assert token in allTokens
        allDocs = indexing.getAllDocs(token)
        assert len(allDocs) == 10*n
        allDocNames = util_functions.getAllDocNames(allDocs)
        for j in range(10*n):
            docName = token + "," + str(j)
            assert docName in allDocNames

# test searching time efficiency
def test26():
    # initial setup
    test25()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    start = time.time()
    for i in range(100):
        n = i + 1
        token = str(n)
        result = indexing.getTopNDocs(token, n)
        # verifying test by ensuring each search results in the top n documents
        assert len(result) == n
    end = time.time()
    
    # verifying test by checking timer
    secondsTaken = end - start
    assert secondsTaken < 3

    # verifying test by ensuring indexing data is the same as before steps were ran
    util_functions.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test updating document time efficiency
@pytest.mark.skip(reason="updateDoc() not available yet")
def test27():
    # initial setup
    test25()

    # steps
    start = time.time()
    for i in range(100):
        n = i + 1
        token = str(n)
        for j in range(n):
            docName = token + "," + str(j)
            indexing.updateDoc(token, Document(docName))
    end = time.time()
    
    # verifying test by checking timer
    secondsTaken = end - start
    assert secondsTaken < 3


# test storage with large amounts of indexing requests
@pytest.mark.skip(reason="FAILS: takes too long, never finishes running")
def test29():
    # initial setup
    indexing.clearIndexes()

    # steps
    for i in range(1000):
        n = i + 1
        token = str(n)
        for j in range(100*n):
            docName = token + "," + str(j)
            indexing.addIndex(token, Document(docName))

    # verifying test by checking indexing data
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 1000
    for i in range(1000):
        n = i + 1
        token = str(n)
        assert token in allTokens
        allDocs = indexing.getAllDocs(token)
        assert len(allDocs) == 100*n
        allDocNames = util_functions.getAllDocNames(allDocs)
        for j in range(100*n):
            docName = token + "," + str(j)
            assert docName in allDocNames

# test storage with large amounts of updating document requests
@pytest.mark.skip(reason="updateDoc() not available yet")
def test30():
    # initial setup
    test25()

    # steps
    for i in range(1000):
        n = i + 1
        token = str(n)
        for j in range(10*n):
            docName = token + "," + str(j)
            indexing.updateDoc(token, Document(docName))