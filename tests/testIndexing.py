# run tests with pytest
from .. import indexing
from .. document import Document

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
    assert bananaDocs[0].docName == "B"

    appleDocs = indexing.getAllDocs("apple")
    assert len(appleDocs) == 1
    assert appleDocs[0].docName == "A"

    carrotDocs = indexing.getAllDocs("carrot")
    assert len(carrotDocs) == 1
    assert carrotDocs[0].docName == "C"

# test indexing many documents for one token, inserted in the order of the word frequency (highest to lowest) for that token
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
    assert peopleDocs[0].docName == "Z"
    assert peopleDocs[1].docName == "V"
    assert peopleDocs[2].docName == "Y"
    assert peopleDocs[3].docName == "U"
    assert peopleDocs[4].docName == "X"

# test indexing many documents for one token, inserted in the order of the word frequency (lowest to highest) for that token
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
    assert peopleDocs[0].docName == "Z"
    assert peopleDocs[1].docName == "V"
    assert peopleDocs[2].docName == "Y"
    assert peopleDocs[3].docName == "U"
    assert peopleDocs[4].docName == "X"

# test indexing many documents for one token, inserted in random order of the word frequency for that token
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
    assert peopleDocs[0].docName == "Z"
    assert peopleDocs[1].docName == "V"
    assert peopleDocs[2].docName == "Y"
    assert peopleDocs[3].docName == "U"
    assert peopleDocs[4].docName == "X"