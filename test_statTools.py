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

#Connor case 1: Empty list
list_empty = []

#Conner case 2: List with single number
list_single = [8]

#Exception case 1: List that contains a string
list_str = ["hello", 3, 5, 6, 7]

#Exception case 2: List that contains float
list_float = [4.5, 6.7, 8.9, 7.6]


def test_median_basic1():
    assert(median(list_1) == 5)

def test_median_basic2():
    assert(median(list_2) == 5.5)
    
def test_median_basic3():
    assert(median(list_3) == 3)
    
def test_median_basic4():
    assert(median(list_4) == 0)