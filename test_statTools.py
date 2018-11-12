import pytest
from statTools import *

#Test case 1: Odd number of length
list_1 = [2, 5, 7, 4, 6]

#Test case 2: Even number of length
list_2 = [9, 3, 5, 7, 4, 6]

#Test case 3: list with negatives
list_3 = [3, 5, -2, -5, 7]

#Test case 4: List of zeros
list_4 = [0, 0, 0, 0, 0]

#Conner case 1: List with single number
list_5 = [8]

#Conner case 2: List that contains float
list_6 = [4.5, 6.7, 8.9, 7.6]

#Exception case 1 Empty list
list_7 = []

#Exception case 2: List that contains a string
list_8 = ["hello", 3, 5, 6, 7]


def test_median_basic1():
    assert(median(list_1) == 5)

def test_median_basic2():
    assert(median(list_2) == 5.5)
    
def test_median_basic3():
    assert(median(list_3) == 3)
    
def test_median_basic4():
    assert(median(list_4) == 0)
    
def test_median_conner1():
    assert(median(list_5) == 8)
    
def test_median_conner2():
    assert(median(list_6) == 7.15)
    
def test_median_Exception1():
    with pytest.raises(ValueError) as errmsg:
        median(list_7)
    assert("Illegal empty list" == str(errmsg.value))
    
def test_median_Exception2():
    with pytest.raises(TypeError) as errmsg:
        median(list_8)
    assert("List contain non-integer value" == str(errmsg.value))
    
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
    
    
    
    
    
    
    