# run tests with pytest
from .. import indexing
from .. document import Document
import utilFunctions
import pytest
import testIndexing

# test retrieving document metadata from text transformation
@pytest.mark.skip(reason="text transformation not available yet")
def test23():
    # initial setup
    indexing.clearIndexes()

# test sending indexing data to ranking
@pytest.mark.skip(reason="not ready to send to ranking yet")
def test24():
    # initial setup
    indexing.test10()