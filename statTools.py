
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


def mode(num_list):
    if len(num_list) == 0:
        raise ValueError("Illegal empty list")
        pass
    num_list.sort()
    current_num = num_list[0]
    current_count = 0
    highest_count = 0
    highest_number = num_list[0]
    for number in num_list:
        if current_num == number:
            current_count += 1
        else:
            current_num = number
            current_count = 1
        if current_count > highest_count:
            highest_count = current_count
            highest_number = number
    return highest_number
