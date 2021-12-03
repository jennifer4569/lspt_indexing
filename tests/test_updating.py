# run tests with pytest
from .. import indexing
from .. document import Document
import util_functions
import pytest
import test_indexing

# test updating a document in a token that doesn't exist
@pytest.mark.skip(reason="test 10 not available yet")
def test17():
    # initial setup
    test_indexing.test10()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    try:
        indexing.updateDoc("Doge", Document("Dog Wiki"))
        # test failed -- above function call should've resulted in KeyError
        assert False
    except KeyError:
        pass
        
    # verifying test by ensuring indexing data is the same as before steps were ran
    util_functions.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test updating a document in a token that currently isn't associated with this document
@pytest.mark.skip(reason="test 10 not available yet")
def test18():
    # initial setup
    test_indexing.test10()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    try:
        indexing.updateDoc("cat", Document("Dog Wiki"))
        # test failed -- above function call should've resulted in LookupError (not KeyError)
        assert False
    except KeyError:
        assert False
    except LookupError:
        pass
        
    # verifying test by ensuring indexing data is the same as before steps were ran
    util_functions.assertSameIndexingData(indexing.indexingData, oldIndexingData)

# test updating a document that is only associated with one token
@pytest.mark.skip(reason="test 10 not available yet")
def test19():
    # initial setup
    test_indexing.test10()

    # steps
    indexing.updateDoc("dog", Document("Golden Retriever Wiki"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "animal" in allTokens
    assert "cat" in allTokens
    assert "dog" in allTokens

    # verifying test by checking documents within their respective tokens
    animalDocs = indexing.getAllDocs("animal")
    assert len(animalDocs) == 3
    animalDocNames = util_functions.getAllDocNames(animalDocs)
    assert animalDocNames[0] == "Dog Wiki"
    assert animalDocNames[1] == "Cat Wiki"
    assert animalDocNames[2] == "Bird Wiki"

    catDocs = indexing.getAllDocs("cat")
    assert len(catDocs) == 2
    catDocNames = util_functions.getAllDocNames(catDocs)
    assert catDocNames[0] == "Cat Wiki"
    assert catDocNames[1] == "Cat Pictures"

    dogDocs = indexing.getAllDocs("dog")
    assert len(dogDocs) == 2
    dogDocNames = util_functions.getAllDocNames(dogDocs)
    assert dogDocNames[0] == "Dog Wiki"
    assert dogDocNames[1] == "Golden Retriever Wiki"
    
# test updating a document that is associated with multiple tokens
@pytest.mark.skip(reason="test 10 not available yet")
def test20():
    # initial setup
    test_indexing.test10()

    # steps
    indexing.updateDoc("animal", Document("Dog Wiki"))
    indexing.updateDoc("dog", Document("Dog Wiki"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "animal" in allTokens
    assert "cat" in allTokens
    assert "dog" in allTokens

    # verifying test by checking documents within their respective tokens
    animalDocs = indexing.getAllDocs("animal")
    assert len(animalDocs) == 3
    animalDocNames = util_functions.getAllDocNames(animalDocs)
    assert animalDocNames[0] == "Cat Wiki"
    assert animalDocNames[1] == "Dog Wiki"
    assert animalDocNames[2] == "Bird Wiki"

    catDocs = indexing.getAllDocs("cat")
    assert len(catDocs) == 2
    catDocNames = util_functions.getAllDocNames(catDocs)
    assert catDocNames[0] == "Cat Wiki"
    assert catDocNames[1] == "Cat Pictures"

    dogDocs = indexing.getAllDocs("dog")
    assert len(dogDocs) == 2
    dogDocNames = util_functions.getAllDocNames(dogDocs)
    assert dogDocNames[0] == "Dog Wiki"
    assert dogDocNames[1] == "Golden Retriever Wiki"
   
# test updating a document with a token that only has this document associated with it
@pytest.mark.skip(reason="updateDoc() not available yet")
def test21():
    # initial setup
    indexing.test6()

    # steps
    indexing.updateDoc("language", Document("python"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "cs" in allTokens
    assert "tech" in allTokens
    assert "language" in allTokens

    # verifying test by checking documents within their respective tokens
    csDocs = indexing.getAllDocs("cs")
    assert len(csDocs) == 3
    csDocNames = util_functions.getAllDocNames(csDocs)
    assert "computer" in csDocNames
    assert "science" in csDocNames
    assert "python" in csDocNames

    techDocs = indexing.getAllDocs("tech")
    assert len(techDocs) == 1
    techDocNames = util_functions.getAllDocNames(techDocs)
    assert "phone" in techDocNames

    languageDocs = indexing.getAllDocs("language")
    assert len(languageDocs) == 1
    languageDocNames = util_functions.getAllDocNames(languageDocs)
    assert "python" in languageDocNames


# test updating a document with a token that currently has multiple other documents associated with it
@pytest.mark.skip(reason="test 10 not available yet")
def test22():
    # initial setup
    test_indexing.test10()

    # steps
    indexing.updateDoc("animal", Document("Bird Wiki"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "animal" in allTokens
    assert "cat" in allTokens
    assert "dog" in allTokens

    # verifying test by checking documents within their respective tokens
    animalDocs = indexing.getAllDocs("animal")
    assert len(animalDocs) == 3
    animalDocNames = util_functions.getAllDocNames(animalDocs)
    assert animalDocNames[0] == "Bird Wiki"
    assert animalDocNames[1] == "Dog Wiki"
    assert animalDocNames[2] == "Cat Wiki"

    catDocs = indexing.getAllDocs("cat")
    assert len(catDocs) == 2
    catDocNames = util_functions.getAllDocNames(catDocs)
    assert catDocNames[0] == "Cat Wiki"
    assert catDocNames[1] == "Cat Pictures"

    dogDocs = indexing.getAllDocs("dog")
    assert len(dogDocs) == 2
    dogDocNames = util_functions.getAllDocNames(dogDocs)
    assert dogDocNames[0] == "Dog Wiki"
    assert dogDocNames[1] == "Golden Retriever Wiki"
   