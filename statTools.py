
def mean(num_list):
    sum = 0
    for number in num_list:
        sum += number
    sum /= len(num_list)
    return sum