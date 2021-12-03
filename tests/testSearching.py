# run tests with pytest
from .. import indexing
from .. document import Document
import utilFunctions
import pytest
import testIndexing

# test searching by token when no tokens are stored
def test11():
    # initial setup
    indexing.clearIndexes()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    try:
        indexing.getTopNDocs("animal", 1)
        # test failed -- above function call should've resulted in KeyError
        assert False
    except KeyError:
        pass

    # verifying test by ensuring indexing data is the same as before steps were ran
    utilFunctions.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test searching by token when only one token is stored
def test12():
    # initial setup
    indexing.clearIndexes()
    indexing.addIndex("animal", Document("Cat Wiki"))
    oldIndexingData = indexing.indexingData.copy()

    # steps
    result = indexing.getTopNDocs("animal", 1)

    # verifying test return value
    assert len(result) == 1
    resultDocNames = utilFunctions.getAllDocNames(result)
    assert "Cat Wiki" in resultDocNames

    # verifying test by ensuring indexing data is the same as before steps were ran
    utilFunctions.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test searching by token when multiple tokens are stored
@pytest.mark.skip(reason="test 10 not available yet")
def test13():
    # initial setup
    testIndexing.test10()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    result = indexing.getTopNDocs("animal", 1)

    # verifying test return value
    assert len(result) == 1
    resultDocNames = utilFunctions.getAllDocNames(result)
    assert "Dog Wiki" in resultDocNames

    # verifying test by ensuring indexing data is the same as before steps were ran
    utilFunctions.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test searching by a token that doesn't exist (yet)
@pytest.mark.skip(reason="test 10 not available yet")
def test14():
    # initial setup
    testIndexing.test10()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    try:
        result = indexing.getTopNDocs("yeti", 1)
        # test failed -- above function call should've resulted in KeyError
        assert False
    except KeyError:
        pass
        
    # verifying test by ensuring indexing data is the same as before steps were ran
    utilFunctions.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test searching by a token that currently only has one document associated with it
def test15():
    # initial setup
    testIndexing.test6()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    result = indexing.getTopNDocs("language", 1)

    # verifying test return value
    assert len(result) == 1
    resultDocNames = utilFunctions.getAllDocNames(result)
    assert "python" in resultDocNames

    # verifying test by ensuring indexing data is the same as before steps were ran
    utilFunctions.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test searching by a token that currently has multiple documents associated with it
@pytest.mark.skip(reason="test 10 not available yet")
def test16():
    # initial setup
    testIndexing.test10()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    result = indexing.getTopNDocs("animal", 1)

    # verifying test return value
    assert len(result) == 1
    resultDocNames = utilFunctions.getAllDocNames(result)
    assert "Dog Wiki" in resultDocNames

    # verifying test by ensuring indexing data is the same as before steps were ran
    utilFunctions.assertSameIndexingData(indexing.indexingData, oldIndexingData)