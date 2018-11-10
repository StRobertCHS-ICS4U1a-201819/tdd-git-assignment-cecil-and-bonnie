import pytest
from statTools import *

def test_median_basic1():
    assert(median([1, 2, 3, 4, 5]) == 3)
