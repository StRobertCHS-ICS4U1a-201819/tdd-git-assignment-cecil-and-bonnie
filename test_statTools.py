import pytest
from statTools import *


def test_statTools_basic1():
    assert(mean([2]) == 2)

def test_statTools_basic2():
    assert(mean([1, 2, 3, 4, 5]) == 3)

