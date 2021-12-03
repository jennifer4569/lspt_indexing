# run tests with pytest
from .. import indexing
from .. document import Document
import utilFunctions
import pytest
import testIndexing

# test indexing time efficiency
def test25():
    # initial setup
    indexing.clearIndexes()