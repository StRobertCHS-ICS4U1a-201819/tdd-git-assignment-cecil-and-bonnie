import pytest
from statTools import *

def test_median_basic1():
    assert(median([1, 2, 3, 4, 5]) == 3)

def test_median_basic2():
    assert(median([1, 2, 3, 4, 5, 6]) == 3.5)