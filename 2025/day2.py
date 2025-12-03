import math
import numpy as np

def invalidPartsInRange(id1, id2):
    min_digits = math.floor(len(id1)/2.0)
    max_digits = math.floor(len(id2)/2.0)+1

    if min_digits > 0:
        x0 = int(id1[:min_digits])
    else:
        x0 = 1
    xf = int(id2[:max_digits])

    max_num = float(id2)
    min_num = float(id1)
    invalid_ids = []
    # Maybe max_digits + 1
    for i in range(x0, xf+1):
        num_str = str(i) + str(i)
        num = int(num_str)
        if num >= min_num and num <= max_num:
            invalid_ids.append(num)
    
    return invalid_ids


def part1(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    total = 0
    id_ranges = data[0].split(',')
    for z, id_range in enumerate(id_ranges):
        ids = id_range.split('-')
        temp_ids = invalidPartsInRange(ids[0], ids[1])
        temp_ids.sort()
        for id in temp_ids:
            total += id

    print(total)

def invalidPartsInRange2(id1, id2):
    num_digits1 = len(id1)
    num_digits2 = len(id2)
    min_num = int(id1)
    max_num = int(id2)

    max_base_number_length = math.ceil(num_digits2/2)
    # What to do if they are different


    # Multiplier has to be bigger than 1
    invalid_ids = []
    for i in range(1, 10**max_base_number_length):
        base = str(i)
        num_digits = len(base)
        multiplier = num_digits1//num_digits
        if multiplier > 1:
            num_str = base * multiplier
            num = int(num_str)
            if num >= min_num and num <= max_num and num not in invalid_ids:
                invalid_ids.append(num)

        multiplier2 = num_digits2//num_digits
        if multiplier2 > 1 and multiplier != multiplier2:
            num_str = base * multiplier2
            num2 = int(num_str)
            if num2 >= min_num and num2 <= max_num and num2 not in invalid_ids:
                invalid_ids.append(num2)

    
    return invalid_ids

def part2(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    total = 0
    id_ranges = data[0].split(',')
    for z, id_range in enumerate(id_ranges):
        ids = id_range.split('-')
        temp_ids = invalidPartsInRange2(ids[0], ids[1])
        print(ids, temp_ids)
        debug = 1
        for id in temp_ids:
            total += id

    print(total)


if __name__=="__main__":
    file = "test_input.txt"
    # file = "input.txt" 

    part1(file)
    part2(file)  