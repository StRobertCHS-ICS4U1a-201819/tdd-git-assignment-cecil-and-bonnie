"""
------------------------------------------------------------------------------------------
Name:		statTools.py
Purpose:	To be able to calculate Measures of Central Tendency and Measures of Spread.


Author:		Cecil.Cao, Bonnie.Li

Created:	11/11/2018
------------------------------------------------------------------------------------------
"""
import math

def mean(num_list):
    """ Calculate the average of a given list of numbers
      :param num_list: list The list of numbers needed to calculate the mean
      :return: int/float The average of the list of numbers
    """
    # Checks if the inputted list is empty, if it does, raise an exception and exit the function
    if len(num_list) == 0:
        # If there is an empty list, return an error message and skip the rest of the function
        raise ValueError("Illegal empty list")
        pass
    # The sum of all the numbers
    total = 0
    # Try if we can add all the numbers in the list together
    try:
        # Adds the numbers together from num_list
        for number in num_list:
            total += number
    # If the list has something other than an int or float, raise a TypeError exception
    except TypeError:
        # Print an error message and end the code
        raise TypeError("A number was not provided.")
        pass
    # Calculates the mean
    total = total / len(num_list)
    return total


def median(num_list):
    """Compute median of a given list of values

    :param num_list: list   List of values to find median
    :return median: int    Median of the given list

    """
    if len(num_list) == 0:
        raise ValueError("Illegal empty list")
        pass
    for count in range(len(num_list)):
        if not (type(num_list[count]) is int or type(num_list[count]) is float):
            raise TypeError("List contain non-integer value")
            pass
    # sort the list
    num_list.sort()
    # if list length is even, find the average of the 2 middle numbers
    if len(num_list) % 2 == 0:
        mid_1 = int(len(num_list) / 2)
        mid_2 = int(len(num_list) / 2 + 1)
        median = (num_list[mid_1 - 1] + num_list[mid_2 - 1]) / 2
    # if list length is odd, find the value of the middle number
    else:
        mid = int((len(num_list) + 1) / 2)
        median = num_list[mid - 1]
    return median


def mode(num_list):
    """ Calculate the most recurring number from a list of numbers.
          :param num_list: list The list of numbers used to calculate the mode
          :return: int/list Returns the most recurring number(s) from num_list
    """
    # Checks if the list is empty, if it is, raise an exception and end the program
    if len(num_list) == 0:
        raise ValueError("Illegal empty list")
        pass
    num_list.sort()
    current_num = num_list[0]
    current_count = 0
    # The highest occurrence of a number
    highest_count = 0
    # Used to check all the unique numbers in num_list
    unique_numbers = []
    # Used to check how many times a certain number pops up in the list
    num_frequency = []
    # Used last to determine the most frequent number(s) for mode
    most_frequent_num = []
    for count in range(len(num_list)):
        # Checks each element in the list is an int or a float if not, raise an exception
        if not(type(num_list[count]) is int or type(num_list[count]) is float):
            raise TypeError("An integer or float was not provided.")
            pass

        # Checks if the number being checked is the same as the previous
        if current_num == num_list[count]:
            # Increment by 1 if True
            current_count += 1
            # If the high score is less than the current score, change highest score to current score
            if highest_count < current_count:
                highest_count = current_count

        # Check if current number isn't equal to previous number
        elif current_num != num_list[count]:
            # If so, change current number to new number and add that number to the unique numbers list
            unique_numbers.append(current_num)
            num_frequency.append(current_count)
            current_num = num_list[count]
            current_count = 1

        # Finally check if we reach the end of num_list and add the final increment onto the 2 other lists.
        if count == len(num_list) - 1:
            unique_numbers.append(current_num)
            num_frequency.append(current_count)

    # Checks which numbers occurred the most out of the set of unique numbers and adds it to the most_frequent_num list
    for counter in range(len(unique_numbers)):
        if num_frequency[counter] == highest_count:
            most_frequent_num.append(unique_numbers[counter])

    # If there's only one number in the list, return that number as an integer
    if len(most_frequent_num) == 1:
        return most_frequent_num[0]

    # Otherwise, if there's more than one number, return the most_frequent_num list
    else:
        return most_frequent_num


def stat_range(num_list):
    """ Calculate the difference between the largest from the smallest number in the list
          :param num_list: list The list of at least 2 numbers needed to calculate the range
          :return: int/float Returns the difference between the largest and smallest number in the list
    """
    # Checks if the string is empty, if it is, raise an exception and end the function
    if len(num_list) == 0:
        raise ValueError("Illegal empty list")
        pass

    # Checks if there is only one number in the list, if so, raise an exception and end the function
    elif len(num_list) == 1:
        raise ValueError("Only one element in list when there should be two or more.")
        pass

    # Tests if the list contains only floats or integers, otherwise, raise an exception
    try:
        # After sorting the list, take the lowest number and highest number and subract the difference
        num_list.sort()
        lowest_num = num_list[0]
        highest_num = num_list[len(num_list) - 1]
        # Return the difference to the user
        return highest_num - lowest_num
    # Raises the exception if program finds non-integer/non-float
    except TypeError:
        raise TypeError("An integer or float was not provided.")


def lowerQuartile(num_list):
    """ Calculate the median of the smaller half of the list
          :param num_list: list The list of numbers given to calculate lower quartile
          :return: int/float The median of the smaller half of the list
    """
    # Checks if the list has less than 4 elements, if it does, raise an exception
    if len(num_list) < 4:
        """
        Since we cannot calculate a lower quartile with less than 4 values,
        should he user input a list with 3 or less elements, we need to raise an exception
        and end function
        """
        raise ValueError("Less than 4 numbers when there should be more than 4.")
        pass

    # Sorts the list and checks the position of the median
    num_list.sort()
    lower_half = (len(num_list) // 2)
    lower_half_list = []
    # Runs a loop to check each value and stores it if it's below the halfway mark of the list
    for element in range(len(num_list)):
        # If the element is not a integer or float, raise an exception and end the program
        if type(num_list[element]) is not float and type(num_list[element]) is not int:
            raise TypeError("An integer or float was not provided.")
            pass

        # Takes in all numbers that are before the halfway point of the list and put them into lower_half_list
        if element < lower_half:
            lower_half_list.append(num_list[element])

    # Sets the median position of the new list
    lower_half_median_position = len(lower_half_list) // 2
    # Checks if the new list is odd or even
    if len(lower_half_list) % 2 == 1:
        # If odd, return the number in the middle position of the list
        return lower_half_list[lower_half_median_position]
    else:
        # If even, add the numbers adjacent to the median and calculate the average. Return that value
        return (lower_half_list[lower_half_median_position] + lower_half_list[lower_half_median_position - 1]) / 2


def upr_quartile(num_list):
    """Compute upper quartile of given list of values
    
    :param num_list: list   List of values to compute upper quartile
    :return upr_quartile: int    Upper quartile of the list
    """
    for count in range(len(num_list)):
        if not(type(num_list[count]) is int or type(num_list[count]) is float):
            raise TypeError("List contain non-integer value")
            pass
    if len(num_list) < 4:
        raise ValueError("List length shorter than 4")
        pass    
    # Sort the list
    num_list.sort()
    # Find the upper half of the list
    upperhalf = num_list[len(num_list)//2:]
    # If upperhalf length is even, find the average of the 2 middle numbers
    if len(upperhalf) % 2 == 0 :
        return (upperhalf[len(upperhalf)//2 - 1] + upperhalf[len(upperhalf)//2]) / 2
    # If upperhalf length is odd, find the value of the middle number
    else :
        return upperhalf[len(upperhalf)//2]


def variance(num_list):
    """Compute variance of given list of values
    
    :param num_list: list   List of values to compute variance
    :return median: float    Variance of the list
    """
    if len(num_list) == 0:
        raise ValueError("Illegal empty list")
        pass    
    for count in range(len(num_list)):
        if not(type(num_list[count]) is int or type(num_list[count]) is float):
            raise TypeError("List contain non-integer value")
            pass
    # Compute the mean of the data
    mean = sum(num_list)/len(num_list)
    # Compute the sum of difference between data and mean squared the divided by list length
    variance = sum((x_i - mean) ** 2 for x_i in num_list) / len(num_list)
    return round(variance, 2)


def st_dev(num_list):
    """Compute standard deviation of given list of values
    
    :param num_list: list   List of values to compute standard deviation
    :return median: float    Standard deviation of the list
    """    
    if len(num_list) == 0:
        raise ValueError("Illegal empty list")
        pass 
    for count in range(len(num_list)):
        if not(type(num_list[count]) is int or type(num_list[count]) is float):
            raise TypeError("List contain non-integer value")
            pass
    # Compute the mean of the list
    mean = sum(num_list)/len(num_list)
    # Compute the square root of the sum of difference between data and mean squared over list length
    std = math.sqrt(sum((x_i - mean) ** 2 for x_i in num_list) / len(num_list))
    return round(std, 2)
