
def mean(num_list):
    if len(num_list) == 0:
        raise ValueError("Illegal empty list")
        pass
    total = 0
    try:
        for number in num_list:
            total += number
    except TypeError:
        raise TypeError("A number was not provided.")
    total = total / len(num_list)
    return total


def mode(num_list):
    if len(num_list) == 0:
        raise ValueError("Illegal empty list")
        pass
    num_list.sort()
    current_num = num_list[0]
    current_count = 0
    highest_count = 0
    unique_numbers = []
    num_frequency = []
    most_frequent_num = []
    for count in range(len(num_list)):
        if not(type(num_list[count]) is int or type(num_list[count]) is float):
            raise TypeError("An integer or float was not provided.")
            pass

        if current_num == num_list[count]:
            current_count += 1
            if highest_count < current_count:
                highest_count = current_count

        elif current_num != num_list[count]:
            unique_numbers.append(current_num)
            num_frequency.append(current_count)
            current_num = num_list[count]
            current_count = 1

        if count == len(num_list) - 1:
            unique_numbers.append(current_num)
            num_frequency.append(current_count)

    for counter in range(len(unique_numbers)):
        if num_frequency[counter] == highest_count:
            most_frequent_num.append(unique_numbers[counter])

    if len(most_frequent_num) == 1:
        return most_frequent_num[0]

    else:
        return most_frequent_num
