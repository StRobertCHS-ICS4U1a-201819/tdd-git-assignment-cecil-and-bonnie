import pytest
from statTools import *


def test_mean_basic1():
    assert(mean([2]) == 2)

def test_mean_basic2():
    assert(mean([1, 2, 3, 4, 5]) == 3)

def test_mean_emptyList():
    with pytest.raises(ValueError) as errmsg:
        mean([])
    assert("Illegal empty list" == str(errmsg.value))
