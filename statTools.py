import math
def median(num_list):
    if len(num_list) == 0:
        raise ValueError("Illegal empty list")
        pass      
    for count in range(len(num_list)):
        if not(type(num_list[count]) is int or type(num_list[count]) is float):
            raise TypeError("List contain non-integer value")
            pass
    num_list.sort()
    if len(num_list) % 2 == 0:
        mid_1 = int(len(num_list) / 2)
        mid_2 = int(len(num_list) / 2 + 1)
        median = (num_list[mid_1 - 1] + num_list[mid_2 - 1]) /2
    else:
        mid = int((len(num_list) + 1) / 2)
        median = num_list[mid-1]
    return median

def upr_quartile(num_list):
    for count in range(len(num_list)):
        if not(type(num_list[count]) is int or type(num_list[count]) is float):
            raise TypeError("List contain non-integer value")
            pass
    num_list.sort()
    if len(num_list) < 4:
        raise ValueError("List length shorter than 4")
        pass      
    num_list.sort()
    upperhalf = num_list[len(num_list)//2:]
    if len(upperhalf) % 2 == 0 :
        return (upperhalf[len(upperhalf)//2 - 1] + upperhalf[len(upperhalf)//2]) / 2
    else :
        return upperhalf[len(upperhalf)//2]
    
def variance(num_list):
    if len(num_list) == 0:
        raise ValueError("Illegal empty list")
        pass    
    for count in range(len(num_list)):
        if not(type(num_list[count]) is int or type(num_list[count]) is float):
            raise TypeError("List contain non-integer value")
            pass
    mean = sum(num_list)/len(num_list)
    variance = sum((x_i - mean) ** 2 for x_i in num_list) / len(num_list)
    return round(variance, 2)

def st_dev(num_list):
    mean = sum(num_list)/len(num_list)
    std = math.sqrt(sum((x_i - mean) ** 2 for x_i in num_list) / len(num_list))
    return round(std, 2)
    














    

    

    
