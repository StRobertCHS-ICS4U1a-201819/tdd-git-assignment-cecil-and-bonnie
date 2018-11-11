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
    assert("A number was not provided." == str(errmsg.value))


def test_mean_onlyZeroes():
    assert(mean([0, 0, 0, 0]) == 0)


def test_mode_basic1():
    assert(mode([1, 2, 3, 3]) == 3)


def test_mode_basic2():
    assert(mode([5, 2, 3, 4, 5]) == 5)


def test_mode_onlyZeroes():
    assert(mode([0, 0, 0]) == 0)


def test_mode_emptyList():
    with pytest.raises(ValueError) as errmsg:
        mode([])
    assert("Illegal empty list" == str(errmsg.value))


def test_mode_wrongType():
    with pytest.raises(TypeError) as errmsg:
        mode(["Is", "this", "the", "Krusty", "Krab?"])
    assert("An integer or float was not provided." == str(errmsg.value))


def test_mode_multipleAnswers():
    assert(mode([1, 1, 2, 3, 3]) == [1, 3])


def test_mode_equalOccurances():
    assert(mode([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])


def test_stat_range_basic1():
    assert(stat_range([1, 2, 7]) == 6)


def test_stat_range_basic2():
    assert(stat_range([11, 2, 1, 10]) == 10)


def test_stat_range_emptyList():
    with pytest.raises(ValueError) as errmsg:
        stat_range([])
    assert("Illegal empty list" == str(errmsg.value))


def test_stat_range_wrongType():
    with pytest.raises(TypeError) as errmsg:
        stat_range(["Space is infinite, but the stars are finite"])
    assert("An integer or float was not provided." == str(errmsg.value))


def test_stat_range_negativeNumbers():
    assert(stat_range([-10, 5, 10, 2]) == 20)
