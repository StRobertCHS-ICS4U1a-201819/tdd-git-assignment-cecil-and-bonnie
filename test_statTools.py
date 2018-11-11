import pytest
from statTools import *


def test_mean_basic1():
    assert(mean([2]) == 2)


def test_mean_basic2():
    assert(mean([1, 2, 3, 4, 5]) == 3)


def test_mean_basic3():
    assert(mean([1, 2.4, 1.6, 9.4]) == 3.6)


def test_mean_emptyList():
    with pytest.raises(ValueError) as errmsg:
        mean([])
    assert("Illegal empty list" == str(errmsg.value))


def test_mean_wrongType():
    with pytest.raises(TypeError) as errmsg:
        mean([1, 2, "Banana Bread", 4, 5])
    assert("A non-negative integer was not provided." == str(errmsg.value))


def test_mean_onlyZeroes():
    assert(mean([0, 0, 0, 0]) == 0)


def test_mode_basic1():
    assert(mode([1, 2, 3, 3]) == 3)


def test_mode_basic2():
    assert(mode([5, 2, 3, 4, 5]) == 5)
