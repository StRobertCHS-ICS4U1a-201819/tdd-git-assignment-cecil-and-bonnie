
def mean(num_list):
    if len(num_list) == 0:
        raise ValueError("Illegal empty list")
        pass
    total = 0
    try:
        for number in num_list:
            total += number
    except TypeError:
        raise TypeError("A non-negative integer was not provided.")
    total /= len(num_list)
    return total
