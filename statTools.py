import math
def median(num_list):
    """Compute median of a given list of values
    
    :param num_list: list   List of values to find median
    :return median: int    Median of the given list
        
    """
    if len(num_list) == 0:
        raise ValueError("Illegal empty list")
        pass      
    for count in range(len(num_list)):
        if not(type(num_list[count]) is int or type(num_list[count]) is float):
            raise TypeError("List contain non-integer value")
            pass
    #sort the list
    num_list.sort()
    #if list length is even, find the average of the 2 middle numbers
    if len(num_list) % 2 == 0:
        mid_1 = int(len(num_list) / 2)
        mid_2 = int(len(num_list) / 2 + 1)
        median = (num_list[mid_1 - 1] + num_list[mid_2 - 1]) /2
    #if list length is odd, find the value of the middle number
    else:
        mid = int((len(num_list) + 1) / 2)
        median = num_list[mid-1]
    return median

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
    #sort the list
    num_list.sort()
    #find the upper half of the list
    upperhalf = num_list[len(num_list)//2:]
    #if upperhalf length is even, find the average of the 2 middle numbers
    if len(upperhalf) % 2 == 0 :
        return (upperhalf[len(upperhalf)//2 - 1] + upperhalf[len(upperhalf)//2]) / 2
    #if upperhalf length is odd, find the value of the middle number
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
    #compute the mean of the data
    mean = sum(num_list)/len(num_list)
    #compute the sum of difference between data and mean squared the divided by list length
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
    #compute the mean of the list
    mean = sum(num_list)/len(num_list)
    #compute the square root of the sum of difference between data and mean squared over list length
    std = math.sqrt(sum((x_i - mean) ** 2 for x_i in num_list) / len(num_list))
    return round(std, 2)
    














    

    

    
