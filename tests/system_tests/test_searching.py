# run tests with pytest
from ... import indexing
from ... document import Document
from ... import util
import pytest
import test_indexing
import random

# test searching by token when no tokens are stored
def test11():
    # initial setup
    indexing.clearIndexes()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    result = indexing.getTopNDocs("animal", 1)
    
    # verifying test by ensuring result is empty list
    assert len(result) == 0

    # verifying test by ensuring indexing data is the same as before steps were ran
    util.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test searching by token when only one token is stored
def test12():
    # initial setup
    indexing.clearIndexes()
    indexing.docDict.addDocument(Document("Cat Wiki", random.randint(1,1000)))
    indexing.addIndex("animal", "Cat Wiki", random.randint(1,1000))
    oldIndexingData = indexing.indexingData.copy()

    # steps
    result = indexing.getTopNDocs("animal", 1)

    # verifying test return value
    assert len(result) == 1
    resultDocNames = util.getAllDocNames(result)
    assert "Cat Wiki" in resultDocNames

    # verifying test by ensuring indexing data is the same as before steps were ran
    util.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test searching by token when multiple tokens are stored
def test13():
    # initial setup
    test_indexing.test10()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    result = indexing.getTopNDocs("animal", 1)

    # verifying test return value
    assert len(result) == 1
    resultDocNames = util.getAllDocNames(result)
    assert "Dog Wiki" in resultDocNames

    # verifying test by ensuring indexing data is the same as before steps were ran
    util.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test searching by a token that doesn't exist (yet)
def test14():
    # initial setup
    test_indexing.test10()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    result = indexing.getTopNDocs("yeti", 1)
    
    # verifying test by ensuring result is empty list
    assert len(result) == 0
        
    # verifying test by ensuring indexing data is the same as before steps were ran
    util.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test searching by a token that currently only has one document associated with it
def test15():
    # initial setup
    test_indexing.test6()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    result = indexing.getTopNDocs("language", 1)

    # verifying test return value
    assert len(result) == 1
    resultDocNames = util.getAllDocNames(result)
    assert "python" in resultDocNames

    # verifying test by ensuring indexing data is the same as before steps were ran
    util.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test searching by a token that currently has multiple documents associated with it
def test16():
    # initial setup
    test_indexing.test10()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    result = indexing.getTopNDocs("animal", 1)

    # verifying test return value
    assert len(result) == 1
    resultDocNames = util.getAllDocNames(result)
    assert "Dog Wiki" in resultDocNames

    # verifying test by ensuring indexing data is the same as before steps were ran
    util.assertSameIndexingData(indexing.indexingData, oldIndexingData)