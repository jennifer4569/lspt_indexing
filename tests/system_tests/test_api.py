# run tests with pytest
from ... import indexing
from ... document import Document
from ... import util
import pytest
import test_indexing

# test retrieving document metadata from text transformation
@pytest.mark.skip(reason="Text Transformation not ready to send information to us yet")
def test23():
    # initial setup
    indexing.clearIndexes()

# test sending indexing data to ranking
@pytest.mark.skip(reason="Ranking not ready to receive information from us yet")
def test24():
    # initial setup
    indexing.test10()

# test an indexing query that contains multiple tokens
@pytest.mark.skip(reason="Ranking not ready to receive information from us yet")
def test28():
    # initial setup
    indexing.test10()