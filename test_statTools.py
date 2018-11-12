"""
------------------------------------------------------------------------------------------
Name:		test_statTools.py
Purpose:	To be able to test the functions being developed in statTools.py


Author:		Cecil.Cao, Bonnie.Li

Created:	11/11/2018
------------------------------------------------------------------------------------------
"""

import pytest
from statTools import *

# Test case 1: Odd number of length
list_1 = [2, 5, 7, 4, 6]

# Test case 2: Even number of length
list_2 = [9, 3, 5, 7, 4, 6]

# Test case 3: list with negatives
list_3 = [3, 5, -2, -5, 7]

# Test case 4: List of zeros
list_4 = [0, 0, 0, 0, 0]

# Conner case 1: List with single number
list_5 = [8]

# Conner case 2: List that contains float
list_6 = [4.5, 6.7, 8.9, 7.6]

# Exception case 1 Empty list
list_7 = []

# Exception case 2: List that contains a string
list_8 = ["hello", 3, 5, 6, 7]

# Corner Case: Tests to see if the mean function can properly output through taking in 1 number
def test_mean_basic1():
    assert(mean([2]) == 2)


# General Case: Tests to see if the mean function properly calculates the mean
def test_mean_basic2():
    assert(mean([1, 2, 3, 4, 5]) == 3)


# Corner Case: Tests to see if the mean function properly handles strings
def test_mean_basic3():
    assert(mean([1, 2.4, 1.6, 9.4]) == 3.6)


# Unusual Case: Tests to see if an exception is raised when given an empty string
def test_mean_emptyList():
    with pytest.raises(ValueError) as errmsg:
        mean([])
    assert("Illegal empty list" == str(errmsg.value))


# Unusual Case: Tests to see if an exception is raised when given a string within the list
def test_mean_wrongType():
    with pytest.raises(TypeError) as errmsg:
        mean([1, 2, "Banana Bread", 4, 5])
    assert("A number was not provided." == str(errmsg.value))


# Corner Case: Tests to see if the program can properly handle a list with only zeroes
def test_mean_onlyZeroes():
    assert(mean([0, 0, 0, 0]) == 0)


def test_median_basic1():
    assert (median(list_1) == 5)


def test_median_basic2():
    assert (median(list_2) == 5.5)


def test_median_basic3():
    assert (median(list_3) == 3)


def test_median_basic4():
    assert (median(list_4) == 0)


def test_median_conner1():
    assert (median(list_5) == 8)


def test_median_conner2():
    assert (median(list_6) == 7.15)


def test_median_Exception1():
    with pytest.raises(ValueError) as errmsg:
        median(list_7)
    assert ("Illegal empty list" == str(errmsg.value))


def test_median_Exception2():
    with pytest.raises(TypeError) as errmsg:
        median(list_8)
    assert ("List contain non-integer value" == str(errmsg.value))


# General Case: Tests to see if it properly outputs the most frequent occurrence of a number in the list
def test_mode_basic1():
    assert(mode([1, 2, 3, 3]) == 3)


# General Case: Tests to see if it properly sorts the list and outputs the most frequent number; 5
def test_mode_basic2():
    assert(mode([5, 2, 3, 4, 5]) == 5)


# Corner Case: Checks if the function can properly handle a list of only zeroes
def test_mode_onlyZeroes():
    assert(mode([0, 0, 0]) == 0)


# Unusual Case: Checks if the function properly raises an exception when given an empty string
def test_mode_emptyList():
    with pytest.raises(ValueError) as errmsg:
        mode([])
    assert("Illegal empty list" == str(errmsg.value))


# Unusual Case: Checks if the function properly raises an exception when given an empty string
def test_mode_wrongType():
    with pytest.raises(TypeError) as errmsg:
        mode(["Is", "this", "the", "Krusty", "Krab?"])
    assert("An integer or float was not provided." == str(errmsg.value))


# General Case: Checks if the function works and can output multiple answers if there are any
def test_mode_multipleAnswers():
    assert(mode([1, 1, 2, 3, 3]) == [1, 3])


# Corner Case: Checks if the function properly outputs the list if the given list has numbers that all occur only once
def test_mode_equalOccurances():
    assert(mode([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])


# General Case: Checks to see if the program properly calculates the range of the given list
def test_stat_range_basic1():
    assert(stat_range([1, 2, 7]) == 6)


# General Case: Checks if the functions sorts the list and properly calculates the range of the given list
def test_stat_range_basic2():
    assert(stat_range([11, 2, 1, 10]) == 10)


# Unusual Case: Checks if the function raises an exception when given an empty list
def test_stat_range_emptyList():
    with pytest.raises(ValueError) as errmsg:
        stat_range([])
    assert("Illegal empty list" == str(errmsg.value))


# Unusual Case: Checks if the function raises an exception when there is are strings in the given list
def test_stat_range_wrongType():
    with pytest.raises(TypeError) as errmsg:
        stat_range(["Space is infinite", "but the stars are finite"])
    assert("An integer or float was not provided." == str(errmsg.value))


# General Case: Checks if the function works as intended and can use negative numbers
def test_stat_range_negativeNumbers():
    assert(stat_range([-10, 5, 10, 2]) == 20)


# Corner Case: Checks if the function is able to handle a list with only zeroes
def test_stat_range_onlyZeroes():
    assert(stat_range([0, 0, 0, 0, 0]) == 0)


# Unusual Case: Checks if the function raises an exception when given 1 element in the list
# A range cannot be calculated with only 1 integer or float
def test_stat_range_oneElement():
    with pytest.raises(ValueError) as errmsg:
        stat_range([1])
    assert("Only one element in list when there should be two or more." == str(errmsg.value))


# General Case: Checks if the function properly outputs a lower quartile from an odd numbered list
def test_lowerQuartile_basic1():
    assert(lowerQuartile([1, 2, 3, 4, 5, 6, 7]) == 2)


# General Case: Checks if the function properly works using an even numbered list
def test_lowerQuartile_basic2():
    assert(lowerQuartile([2, 3, 4, 4, 6, 7, 7, 7, 8, 8, 9, 10]) == 4)


# General Case: Checks if the function works given an even numbered list and calculates the average between them
def test_lowerQuartile_basic3():
    assert(lowerQuartile([1, 2, 3, 4]) == 1.5)


# Unusual Case: Checks if the function raises an exception when a string is in the list
def test_lowerQuartile_wrongType():
    with pytest.raises(TypeError) as errmsg:
        lowerQuartile(["Just", "let", "it", "go"])
    assert("An integer or float was not provided." == str(errmsg.value))


# Unusual Case: Checks if the function raises an exception when less than 4 numbers are in the list
def test_lowerQuartile_lessthan4elements():
    with pytest.raises(ValueError) as errmsg:
        lowerQuartile([1, 2, 3])
    assert("Less than 4 numbers when there should be more than 4." == str(errmsg.value))


# Corner Case: Checks if the program can handle a list of only zeroes
def test_lowerQuartile_onlyZeroes():
    assert(lowerQuartile([0, 0, 0, 0, 0]) == 0)


# General Case: Checks if the program can properly calculate the answer given negative numbers
def test_lowerQuartile_negativeNumbers():
    assert(lowerQuartile([-100, -10, -5, 10, 90]) == -55)


def test_upr_quartile_basic1():
    assert(upr_quartile(list_1) == 6)


def test_upr_quartile_basic2():
    assert(upr_quartile(list_2) == 7)


def test_upr_quartile_basic3():
    assert(upr_quartile(list_3) == 5)


def test_upr_quartile_basic4():
    assert(upr_quartile(list_4) == 0)


def test_upr_quartile_conner1():
    assert(upr_quartile(list_6) == 8.25)


def test_upr_quartile_exception1():
    with pytest.raises(ValueError) as errmsg:
        upr_quartile(list_5)
    assert("List length shorter than 4" == str(errmsg.value))


def test_upr_quartile_exception2():
    with pytest.raises(ValueError) as errmsg:
        upr_quartile(list_7)
    assert("List length shorter than 4" == str(errmsg.value))


def test_upr_quartile_exception3():
    with pytest.raises(TypeError) as errmsg:
        upr_quartile(list_8)
    assert("List contain non-integer value" == str(errmsg.value))


def test_variance_basic1():
    assert(variance(list_1) == 2.96)


def test_variance_basic2():
    assert(variance(list_2) == 3.89)


def test_variance_basic3():
    assert(variance(list_3) == 19.84)


def test_variance_basic4():
    assert(variance(list_4) == 0)


def test_variance_corner1():
    assert(variance(list_5) == 0)


def test_variance_corner2():
    assert(variance(list_6) == 2.57)


def test_variance_exception1():
    with pytest.raises(ValueError) as errmsg:
        variance(list_7)
    assert("Illegal empty list" == str(errmsg.value))


def test_variance_exception2():
    with pytest.raises(TypeError) as errmsg:
        variance(list_8)
    assert("List contain non-integer value" == str(errmsg.value))


def test_st_dev_basic1():
    assert(st_dev(list_1) == 1.72)


def test_st_dev_basic2():
    assert(st_dev(list_2) == 1.97)


def test_st_dev_basic3():
    assert(st_dev(list_3) == 4.45)


def test_st_dev_basic4():
    assert(st_dev(list_4) == 0)


def test_st_dev_corner1():
    assert(st_dev(list_6) == 1.60)


def test_st_dev_corner2():
    assert(st_dev(list_5) == 0)


def test_st_dev_exception1():
    with pytest.raises(ValueError) as errmsg:
        st_dev(list_7)
    assert("Illegal empty list" == str(errmsg.value))


def test_st_dev_exception2():
    with pytest.raises(TypeError) as errmsg:
        st_dev(list_8)
    assert("List contain non-integer value" == str(errmsg.value))
