# run tests with pytest
from ... import indexing
from ... document import Document
from ... import util
import pytest
import random 

# test indexing unique tokens only
def test1():
    # initial setup
    indexing.clearIndexes()

    # steps
    indexing.docDict.addDocument(Document("A", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("B", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("C", random.randint(1,1000)))
    
    indexing.addIndex("banana", "B", random.randint(1,1000))
    indexing.addIndex("apple", "A", random.randint(1,1000))
    indexing.addIndex("carrot", "C", random.randint(1,1000))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "banana" in allTokens
    assert "apple" in allTokens
    assert "carrot" in allTokens

    # verifying test by checking documents within their respective tokens
    bananaDocs = indexing.getAllDocs("banana")
    assert len(bananaDocs) == 1
    bananaDocNames = util.getAllDocNames(bananaDocs)
    assert "B" in bananaDocNames

    appleDocs = indexing.getAllDocs("apple")
    assert len(appleDocs) == 1
    appleDocNames = util.getAllDocNames(appleDocs)
    assert "A" in appleDocNames

    carrotDocs = indexing.getAllDocs("carrot")
    assert len(carrotDocs) == 1
    carrotDocNames = util.getAllDocNames(carrotDocs)
    assert "C" in carrotDocNames

# test indexing many documents for one token, inserted in the order of the word frequency (highest to lowest) for that token
def test2():
    # initial setup
    indexing.clearIndexes()

    # steps
    indexing.docDict.addDocument(Document("Z", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("V", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("Y", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("U", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("X", random.randint(1,1000)))
    
    indexing.addIndex("people", "Z", 20)
    indexing.addIndex("people", "V", 19)
    indexing.addIndex("people", "Y", 15)
    indexing.addIndex("people", "U", 10)
    indexing.addIndex("people", "X", 1)

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 1
    assert "people" in allTokens

    # verifying test by checking documents within "people" token
    peopleDocs = indexing.getAllDocs("people")
    assert len(peopleDocs) == 5
    peopleDocNames = util.getAllDocNames(peopleDocs)
    assert peopleDocNames[0] == "Z"
    assert peopleDocNames[1] == "V"
    assert peopleDocNames[2] == "Y"
    assert peopleDocNames[3] == "U"
    assert peopleDocNames[4] == "X"

# test indexing many documents for one token, inserted in the order of the word frequency (lowest to highest) for that token
def test3():
    # initial setup
    indexing.clearIndexes()

    # steps
    indexing.docDict.addDocument(Document("Z", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("V", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("Y", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("U", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("X", random.randint(1,1000)))
    
    indexing.addIndex("people", "X", 1)
    indexing.addIndex("people", "U", 10)
    indexing.addIndex("people", "Y", 15)
    indexing.addIndex("people", "V", 19)
    indexing.addIndex("people", "Z", 20)

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 1
    assert "people" in allTokens

    # verifying test by checking documents within "people" token
    peopleDocs = indexing.getAllDocs("people")
    assert len(peopleDocs) == 5
    peopleDocNames = util.getAllDocNames(peopleDocs)
    assert peopleDocNames[0] == "Z"
    assert peopleDocNames[1] == "V"
    assert peopleDocNames[2] == "Y"
    assert peopleDocNames[3] == "U"
    assert peopleDocNames[4] == "X"

# test indexing many documents for one token, inserted in random order of the word frequency for that token
def test4():
    # initial setup
    indexing.clearIndexes()

    # steps
    indexing.docDict.addDocument(Document("Z", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("V", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("Y", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("U", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("X", random.randint(1,1000)))
    
    indexing.addIndex("people", "Z", 20)
    indexing.addIndex("people", "Y", 15)
    indexing.addIndex("people", "X", 1)
    indexing.addIndex("people", "V", 19)
    indexing.addIndex("people", "U", 10)

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 1
    assert "people" in allTokens

    # verifying test by checking documents within "people" token
    peopleDocs = indexing.getAllDocs("people")
    assert len(peopleDocs) == 5
    peopleDocNames = util.getAllDocNames(peopleDocs)
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
    indexing.docDict.addDocument(Document("B", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("A", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("C", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("Ba", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("Ban", random.randint(1,1000)))

    indexing.addIndex("banana", "B", random.randint(1,1000))
    indexing.addIndex("apple", "A", random.randint(1,1000))
    indexing.addIndex("carrot", "C", random.randint(1,1000))
    indexing.addIndex("banana", "Ba", random.randint(1,1000))
    indexing.addIndex("banana", "Ban", random.randint(1,1000))

    # verifying test by checking tokens
    allTokens = indexing.getAllTokens()
    assert len(allTokens) == 3
    assert "banana" in allTokens
    assert "apple" in allTokens
    assert "carrot" in allTokens

    # verifying test by checking documents within their respective tokens
    bananaDocs = indexing.getAllDocs("banana")
    assert len(bananaDocs) == 3
    bananaDocNames = util.getAllDocNames(bananaDocs)
    assert "B" in bananaDocNames
    assert "Ban" in bananaDocNames
    assert "Ba" in bananaDocNames

    appleDocs = indexing.getAllDocs("apple")
    assert len(appleDocs) == 1
    appleDocNames = util.getAllDocNames(appleDocs)
    assert "A" in appleDocNames

    carrotDocs = indexing.getAllDocs("carrot")
    assert len(carrotDocs) == 1
    carrotDocNames = util.getAllDocNames(carrotDocs)
    assert "C" in carrotDocNames

# test indexing when only one token is stored
def test6():
    # initial setup
    indexing.clearIndexes()

    indexing.docDict.addDocument(Document("computer", random.randint(1,1000)))
    indexing.addIndex("cs", "computer", random.randint(1,1000))

    # steps
    indexing.docDict.addDocument(Document("science", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("phone", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("python", random.randint(1,1000)))

    indexing.addIndex("cs", "science", random.randint(1,1000))
    indexing.addIndex("tech", "phone", random.randint(1,1000))
    indexing.addIndex("language", "python", random.randint(1,1000))
    indexing.addIndex("cs", "python", random.randint(1,1000))

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

# test indexing when multiple tokens are stored
def test7():
    # initial setup
    test6()

    # steps
    indexing.docDict.addDocument(Document("english", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("laptop", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("computer", random.randint(1,1000)))
    
    indexing.addIndex("language", "english", random.randint(1,1000))
    indexing.addIndex("tech", "laptop", random.randint(1,1000))
    indexing.addIndex("tech", "computer", random.randint(1,1000))

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
    assert len(techDocs) == 3
    techDocNames = util.getAllDocNames(techDocs)
    assert "phone" in techDocNames
    assert "computer" in techDocNames
    assert "laptop" in techDocNames

    languageDocs = indexing.getAllDocs("language")
    assert len(languageDocs) == 2
    languageDocNames = util.getAllDocNames(languageDocs)
    assert "english" in languageDocNames
    assert "python" in languageDocNames

# test indexing document with a new token
def test8():
    # initial setup
    test6()

    # steps
    indexing.docDict.addDocument(Document("system", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("unit", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("system integration", random.randint(1,1000)))
    
    indexing.addIndex("testing", "system", random.randint(1,1000))
    indexing.addIndex("testing", "unit", random.randint(1,1000))
    indexing.addIndex("testing", "system integration", random.randint(1,1000))

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

    testingDocs = indexing.getAllDocs("testing")
    assert len(testingDocs) == 3
    testingDocNames = util.getAllDocNames(testingDocs)
    assert "system" in testingDocNames
    assert "unit" in testingDocNames
    assert "system integration" in testingDocNames

# test indexing a document with a token that currently only has one other document associated with it
def test9():
    # initial setup
    test6()

    # steps
    indexing.docDict.addDocument(Document("java", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("C++", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("javascript", random.randint(1,1000)))
    
    indexing.addIndex("language", "java", random.randint(1,1000))
    indexing.addIndex("language", "C++", random.randint(1,1000))
    indexing.addIndex("language", "javascript", random.randint(1,1000))

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
    assert len(languageDocs) == 4
    languageDocNames = util.getAllDocNames(languageDocs)
    assert "python" in languageDocNames
    assert "C++" in languageDocNames
    assert "java" in languageDocNames
    assert "javascript" in languageDocNames

# test indexing a document with a token that currently has multiple other documents associated with it
def test10():
    # initial setup
    indexing.clearIndexes()

    indexing.docDict.addDocument(Document("Dog Wiki", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("Cat Wiki", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("Bird Wiki", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("Golden Retriever Wiki", random.randint(1,1000)))
    indexing.docDict.addDocument(Document("Cat Pictures", random.randint(1,1000)))
    
    indexing.addIndex("animal", "Dog Wiki", 6)
    indexing.addIndex("animal", "Bird Wiki", 3)
    indexing.addIndex("cat", "Cat Pictures", 4)
    indexing.addIndex("dog", "Dog Wiki", 23)
    indexing.addIndex("dog", "Golden Retriever Wiki", 14)
    indexing.addIndex("cat", "Cat Wiki", 20)

    # steps
    indexing.addIndex("animal", "Cat Wiki", 5)

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