def median(num_list):
    num_list.sort()
    if len(num_list) % 2 == 0:
        mid_1 = int(len(num_list) / 2)
        mid_2 = int(len(num_list) / 2 + 1)
        median = (num_list[mid_1 - 1] + num_list[mid_2 - 1]) /2
    else:
        mid = int((len(num_list) + 1) / 2)
        median = num_list[mid-1]
    return median

    
