# run tests with pytest
from ... import indexing
from ... document import Document
from ... import util
import pytest
import test_indexing
import random

# test updating a document in a token that doesn't exist
def test17():
    # initial setup
    test_indexing.test10()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    indexing.updateDoc("Doge", "Dog Wiki", 1000)
    
    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 4
    assert "animal" in allTokens
    assert "cat" in allTokens
    assert "dog" in allTokens
    assert "Doge" in allTokens

    # verifying test by checking documents within their respective tokens
    animalDocs = indexing.getAllDocs("animal")
    assert len(animalDocs) == 3
    animalDocNames = util.getAllDocNames(animalDocs)
    assert animalDocNames[0] == "Dog Wiki"
    assert animalDocNames[1] == "Cat Wiki"
    assert animalDocNames[2] == "Bird Wiki"

    catDocs = indexing.getAllDocs("cat")
    assert len(catDocs) == 2
    catDocNames = util.getAllDocNames(catDocs)
    assert catDocNames[0] == "Cat Wiki"
    assert catDocNames[1] == "Cat Pictures"

    dogDocs = indexing.getAllDocs("dog")
    assert len(dogDocs) == 2
    dogDocNames = util.getAllDocNames(dogDocs)
    assert dogDocNames[0] == "Dog Wiki"
    assert dogDocNames[1] == "Golden Retriever Wiki"

    dogeDocs = indexing.getAllDocs("Doge")
    assert len(dogeDocs) == 1
    dogeDocNames = util.getAllDocNames(dogeDocs)
    assert dogDocNames[0] == "Dog Wiki"

# test updating a document in a token that currently isn't associated with this document
def test18():
    # initial setup
    test_indexing.test10()
    oldIndexingData = indexing.indexingData.copy()

    # steps
    indexing.updateDoc("cat", "Dog Wiki", 1)
        
    # verifying test by ensuring indexing data is the same as before steps were ran
    # util.assertSameIndexingData(indexing.indexingData, oldIndexingData)
        
    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "animal" in allTokens
    assert "cat" in allTokens
    assert "dog" in allTokens

    # verifying test by checking documents within their respective tokens
    animalDocs = indexing.getAllDocs("animal")
    assert len(animalDocs) == 3
    animalDocNames = util.getAllDocNames(animalDocs)
    assert animalDocNames[0] == "Dog Wiki"
    assert animalDocNames[1] == "Cat Wiki"
    assert animalDocNames[2] == "Bird Wiki"

    catDocs = indexing.getAllDocs("cat")
    assert len(catDocs) == 3
    catDocNames = util.getAllDocNames(catDocs)
    assert catDocNames[0] == "Cat Wiki"
    assert catDocNames[1] == "Cat Pictures"
    assert catDocNames[2] == "Dog Wiki"

    dogDocs = indexing.getAllDocs("dog")
    assert len(dogDocs) == 2
    dogDocNames = util.getAllDocNames(dogDocs)
    assert dogDocNames[0] == "Dog Wiki"
    assert dogDocNames[1] == "Golden Retriever Wiki"

# test updating a document that is only associated with one token
def test19():
    # initial setup
    test_indexing.test10()

    # steps
    indexing.updateDoc("dog", "Golden Retriever Wiki", 20)

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "animal" in allTokens
    assert "cat" in allTokens
    assert "dog" in allTokens

    # verifying test by checking documents within their respective tokens
    animalDocs = indexing.getAllDocs("animal")
    assert len(animalDocs) == 3
    animalDocNames = util.getAllDocNames(animalDocs)
    assert animalDocNames[0] == "Dog Wiki"
    assert animalDocNames[1] == "Cat Wiki"
    assert animalDocNames[2] == "Bird Wiki"

    catDocs = indexing.getAllDocs("cat")
    assert len(catDocs) == 2
    catDocNames = util.getAllDocNames(catDocs)
    assert catDocNames[0] == "Cat Wiki"
    assert catDocNames[1] == "Cat Pictures"

    dogDocs = indexing.getAllDocs("dog")
    assert len(dogDocs) == 2
    dogDocNames = util.getAllDocNames(dogDocs)
    assert dogDocNames[0] == "Dog Wiki"
    assert dogDocNames[1] == "Golden Retriever Wiki"
    
# test updating a document that is associated with multiple tokens
def test20():
    # initial setup
    test_indexing.test10()

    # steps
    indexing.updateDoc("animal", "Dog Wiki", 4)
    indexing.updateDoc("dog", "Dog Wiki", 20)

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "animal" in allTokens
    assert "cat" in allTokens
    assert "dog" in allTokens

    # verifying test by checking documents within their respective tokens
    animalDocs = indexing.getAllDocs("animal")
    assert len(animalDocs) == 3
    animalDocNames = util.getAllDocNames(animalDocs)
    assert animalDocNames[0] == "Cat Wiki"
    assert animalDocNames[1] == "Dog Wiki"
    assert animalDocNames[2] == "Bird Wiki"

    catDocs = indexing.getAllDocs("cat")
    assert len(catDocs) == 2
    catDocNames = util.getAllDocNames(catDocs)
    assert catDocNames[0] == "Cat Wiki"
    assert catDocNames[1] == "Cat Pictures"

    dogDocs = indexing.getAllDocs("dog")
    assert len(dogDocs) == 2
    dogDocNames = util.getAllDocNames(dogDocs)
    assert dogDocNames[0] == "Dog Wiki"
    assert dogDocNames[1] == "Golden Retriever Wiki"
   
# test updating a document with a token that only has this document associated with it
def test21():
    # initial setup
    test_indexing.test6()

    # steps
    indexing.updateDoc("language", "python", random.randint(1,1000))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "cs" in allTokens
    assert "tech" in allTokens
    assert "language" in allTokens

    # verifying test by checking documents within their respective tokens
    csDocs = indexing.getAllDocs("cs")
    assert len(csDocs) == 3
    csDocNames = util.getAllDocNames(csDocs)
    assert "computer" in csDocNames
    assert "science" in csDocNames
    assert "python" in csDocNames

    techDocs = indexing.getAllDocs("tech")
    assert len(techDocs) == 1
    techDocNames = util.getAllDocNames(techDocs)
    assert "phone" in techDocNames

    languageDocs = indexing.getAllDocs("language")
    assert len(languageDocs) == 1
    languageDocNames = util.getAllDocNames(languageDocs)
    assert "python" in languageDocNames


# test updating a document with a token that currently has multiple other documents associated with it
def test22():
    # initial setup
    test_indexing.test10()

    # steps
    indexing.updateDoc("animal", "Bird Wiki", 20)

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "animal" in allTokens
    assert "cat" in allTokens
    assert "dog" in allTokens

    # verifying test by checking documents within their respective tokens
    animalDocs = indexing.getAllDocs("animal")
    assert len(animalDocs) == 3
    animalDocNames = util.getAllDocNames(animalDocs)
    assert animalDocNames[0] == "Bird Wiki"
    assert animalDocNames[1] == "Dog Wiki"
    assert animalDocNames[2] == "Cat Wiki"

    catDocs = indexing.getAllDocs("cat")
    assert len(catDocs) == 2
    catDocNames = util.getAllDocNames(catDocs)
    assert catDocNames[0] == "Cat Wiki"
    assert catDocNames[1] == "Cat Pictures"

    dogDocs = indexing.getAllDocs("dog")
    assert len(dogDocs) == 2
    dogDocNames = util.getAllDocNames(dogDocs)
    assert dogDocNames[0] == "Dog Wiki"
    assert dogDocNames[1] == "Golden Retriever Wiki"
   