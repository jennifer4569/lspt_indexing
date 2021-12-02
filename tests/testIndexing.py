# run tests with pytest
from .. import indexing
from .. document import Document
import utilFunctions
import pytest

# test indexing unique tokens only
def test1():
    # initial setup
    indexing.clearIndexes()

    # steps
    indexing.addIndex("banana", Document("B"))
    indexing.addIndex("apple", Document("A"))
    indexing.addIndex("carrot", Document("C"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "banana" in allTokens
    assert "apple" in allTokens
    assert "carrot" in allTokens

    # verifying test by checking documents within their respective tokens
    bananaDocs = indexing.getAllDocs("banana")
    assert len(bananaDocs) == 1
    bananaDocNames = utilFunctions.getAllDocNames(bananaDocs)
    assert "B" in bananaDocNames

    appleDocs = indexing.getAllDocs("apple")
    assert len(appleDocs) == 1
    appleDocNames = utilFunctions.getAllDocNames(appleDocs)
    assert "A" in appleDocNames

    carrotDocs = indexing.getAllDocs("carrot")
    assert len(carrotDocs) == 1
    carrotDocNames = utilFunctions.getAllDocNames(carrotDocs)
    assert "C" in carrotDocNames

# test indexing many documents for one token, inserted in the order of the word frequency (highest to lowest) for that token
@pytest.mark.skip(reason="document score not available yet")
def test2():
    # initial setup
    indexing.clearIndexes()

    # steps
    indexing.addIndex("people", Document("Z"))
    indexing.addIndex("people", Document("V"))
    indexing.addIndex("people", Document("Y"))
    indexing.addIndex("people", Document("U"))
    indexing.addIndex("people", Document("X"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 1
    assert "people" in allTokens

    # verifying test by checking documents within "people" token
    peopleDocs = indexing.getAllDocs("people")
    assert len(peopleDocs) == 5
    peopleDocNames = utilFunctions.peopleDocNames(peopleDocs)
    assert peopleDocNames[0] == "Z"
    assert peopleDocNames[1] == "V"
    assert peopleDocNames[2] == "Y"
    assert peopleDocNames[3] == "U"
    assert peopleDocNames[4] == "X"

# test indexing many documents for one token, inserted in the order of the word frequency (lowest to highest) for that token
@pytest.mark.skip(reason="document score not available yet")
def test3():
    # initial setup
    indexing.clearIndexes()

    # steps
    indexing.addIndex("people", Document("X"))
    indexing.addIndex("people", Document("U"))
    indexing.addIndex("people", Document("Y"))
    indexing.addIndex("people", Document("V"))
    indexing.addIndex("people", Document("Z"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 1
    assert "people" in allTokens

    # verifying test by checking documents within "people" token
    peopleDocs = indexing.getAllDocs("people")
    assert len(peopleDocs) == 5
    peopleDocNames = utilFunctions.peopleDocNames(peopleDocs)
    assert peopleDocNames[0] == "Z"
    assert peopleDocNames[1] == "V"
    assert peopleDocNames[2] == "Y"
    assert peopleDocNames[3] == "U"
    assert peopleDocNames[4] == "X"

# test indexing many documents for one token, inserted in random order of the word frequency for that token
@pytest.mark.skip(reason="document score not available yet")
def test4():
    # initial setup
    indexing.clearIndexes()

    # steps
    indexing.addIndex("people", Document("Z"))
    indexing.addIndex("people", Document("Y"))
    indexing.addIndex("people", Document("X"))
    indexing.addIndex("people", Document("V"))
    indexing.addIndex("people", Document("U"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 1
    assert "people" in allTokens

    # verifying test by checking documents within "people" token
    peopleDocs = indexing.getAllDocs("people")
    assert len(peopleDocs) == 5
    peopleDocNames = utilFunctions.peopleDocNames(peopleDocs)
    assert peopleDocNames[0] == "Z"
    assert peopleDocNames[1] == "V"
    assert peopleDocNames[2] == "Y"
    assert peopleDocNames[3] == "U"
    assert peopleDocNames[4] == "X"

# test indexing when no tokens are stored
def test5():
    # initial setup
    indexing.clearIndexes()

    # steps
    indexing.addIndex("banana", Document("B"))
    indexing.addIndex("apple", Document("A"))
    indexing.addIndex("carrot", Document("C"))
    indexing.addIndex("banana", Document("Ba"))
    indexing.addIndex("banana", Document("Ban"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "banana" in allTokens
    assert "apple" in allTokens
    assert "carrot" in allTokens

    # verifying test by checking documents within their respective tokens
    bananaDocs = indexing.getAllDocs("banana")
    assert len(bananaDocs) == 3
    bananaDocNames = utilFunctions.getAllDocNames(bananaDocs)
    assert "B" in bananaDocNames
    assert "Ban" in bananaDocNames
    assert "Ba" in bananaDocNames

    appleDocs = indexing.getAllDocs("apple")
    assert len(appleDocs) == 1
    appleDocNames = utilFunctions.getAllDocNames(appleDocs)
    assert "A" in appleDocNames

    carrotDocs = indexing.getAllDocs("carrot")
    assert len(carrotDocs) == 1
    carrotDocNames = utilFunctions.getAllDocNames(carrotDocs)
    assert "C" in carrotDocNames

# test indexing when only one token is stored
def test6():
    # initial setup
    indexing.clearIndexes()
    indexing.addIndex("cs", Document("computer"))

    # steps
    indexing.addIndex("cs", Document("science"))
    indexing.addIndex("tech", Document("phone"))
    indexing.addIndex("language", Document("python"))
    indexing.addIndex("cs", Document("python"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "cs" in allTokens
    assert "tech" in allTokens
    assert "language" in allTokens

    # verifying test by checking documents within their respective tokens
    csDocs = indexing.getAllDocs("cs")
    assert len(csDocs) == 3
    csDocNames = utilFunctions.getAllDocNames(csDocs)
    assert "computer" in csDocNames
    assert "science" in csDocNames
    assert "python" in csDocNames

    techDocs = indexing.getAllDocs("tech")
    assert len(techDocs) == 1
    techDocNames = utilFunctions.getAllDocNames(techDocs)
    assert "phone" in techDocNames

    languageDocs = indexing.getAllDocs("language")
    assert len(languageDocs) == 1
    languageDocNames = utilFunctions.getAllDocNames(languageDocs)
    assert "python" in languageDocNames

# test indexing when multiple tokens are stored
def test7():
    # initial setup
    test6()

    # steps
    indexing.addIndex("language", Document("english"))
    indexing.addIndex("tech", Document("laptop"))
    indexing.addIndex("tech", Document("computer"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "cs" in allTokens
    assert "tech" in allTokens
    assert "language" in allTokens

    # verifying test by checking documents within their respective tokens
    csDocs = indexing.getAllDocs("cs")
    assert len(csDocs) == 3
    csDocNames = utilFunctions.getAllDocNames(csDocs)
    assert "computer" in csDocNames
    assert "science" in csDocNames
    assert "python" in csDocNames

    techDocs = indexing.getAllDocs("tech")
    assert len(techDocs) == 3
    techDocNames = utilFunctions.getAllDocNames(techDocs)
    assert "phone" in techDocNames
    assert "computer" in techDocNames
    assert "laptop" in techDocNames

    languageDocs = indexing.getAllDocs("language")
    assert len(languageDocs) == 2
    languageDocNames = utilFunctions.getAllDocNames(languageDocs)
    assert "english" in languageDocNames
    assert "python" in languageDocNames

# test indexing document with a new token
def test8():
    # initial setup
    test6()

    # steps
    indexing.addIndex("testing", Document("system"))
    indexing.addIndex("testing", Document("unit"))
    indexing.addIndex("testing", Document("system integration"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 4
    assert "cs" in allTokens
    assert "tech" in allTokens
    assert "language" in allTokens
    assert "testing" in allTokens

    # verifying test by checking documents within their respective tokens
    csDocs = indexing.getAllDocs("cs")
    assert len(csDocs) == 3
    csDocNames = utilFunctions.getAllDocNames(csDocs)
    assert "computer" in csDocNames
    assert "science" in csDocNames
    assert "python" in csDocNames

    techDocs = indexing.getAllDocs("tech")
    assert len(techDocs) == 1
    techDocNames = utilFunctions.getAllDocNames(techDocs)
    assert "phone" in techDocNames

    languageDocs = indexing.getAllDocs("language")
    assert len(languageDocs) == 1
    languageDocNames = utilFunctions.getAllDocNames(languageDocs)
    assert "python" in languageDocNames

    testingDocs = indexing.getAllDocs("testing")
    assert len(testingDocs) == 3
    testingDocNames = utilFunctions.getAllDocNames(testingDocs)
    assert "system" in testingDocNames
    assert "unit" in testingDocNames
    assert "system integration" in testingDocNames

# test indexing a document with a token that currently only has one other document associated with it
def test9():
    # initial setup
    test6()

    # steps
    indexing.addIndex("language", Document("java"))
    indexing.addIndex("language", Document("C++"))
    indexing.addIndex("language", Document("javascript"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "cs" in allTokens
    assert "tech" in allTokens
    assert "language" in allTokens

    # verifying test by checking documents within their respective tokens
    csDocs = indexing.getAllDocs("cs")
    assert len(csDocs) == 3
    csDocNames = utilFunctions.getAllDocNames(csDocs)
    assert "computer" in csDocNames
    assert "science" in csDocNames
    assert "python" in csDocNames

    techDocs = indexing.getAllDocs("tech")
    assert len(techDocs) == 1
    techDocNames = utilFunctions.getAllDocNames(techDocs)
    assert "phone" in techDocNames

    languageDocs = indexing.getAllDocs("language")
    assert len(languageDocs) == 4
    languageDocNames = utilFunctions.getAllDocNames(languageDocs)
    assert "python" in languageDocNames
    assert "C++" in languageDocNames
    assert "java" in languageDocNames
    assert "javascript" in languageDocNames

# test indexing a document with a token that currently has multiple other documents associated with it
@pytest.mark.skip(reason="document score not available yet")
def test10():
    # initial setup
    indexing.clearIndexes()
    indexing.addIndex("animal", Document("Dog Wiki"))
    indexing.addIndex("animal", Document("Bird Wiki"))
    indexing.addIndex("cat", Document("Cat Pictures"))
    indexing.addIndex("dog", Document("Dog Wiki"))
    indexing.addIndex("dog", Document("Golden Retriever Wiki"))
    indexing.addIndex("cat", Document("Cat Wiki"))

    # steps
    indexing.addIndex("animal", Document("Cat Wiki"))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "animal" in allTokens
    assert "cat" in allTokens
    assert "dog" in allTokens

    # verifying test by checking documents within their respective tokens
    animalDocs = indexing.getAllDocs("animal")
    assert len(animalDocs) == 3
    animalDocNames = utilFunctions.getAllDocNames(animalDocs)
    assert animalDocNames[0] == "Dog Wiki"
    assert animalDocNames[1] == "Cat Wiki"
    assert animalDocNames[2] == "Bird Wiki"

    catDocs = indexing.getAllDocs("cat")
    assert len(catDocs) == 2
    catDocNames = utilFunctions.getAllDocNames(catDocs)
    assert catDocNames[0] == "Cat Wiki"
    assert catDocNames[1] == "Cat Pictures"

    dogDocs = indexing.getAllDocs("dog")
    assert len(dogDocs) == 2
    dogDocNames = utilFunctions.getAllDocNames(dogDocs)
    assert dogDocNames[0] == "Dog Wiki"
    assert dogDocNames[1] == "Golden Retriever Wiki"