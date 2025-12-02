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


def part2(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    total = 0
    id_ranges = data[0].split(',')
    for z, id_range in enumerate(id_ranges):
        ids = id_range.split('-')
        temp_ids = invalidPartsInRange2(ids[0], ids[1])
        temp_ids.sort()
        for id in temp_ids:
            total += id

    print(total)


if __name__=="__main__":
    file = "test_input.txt"
    # file = "input.txt" 

    part1(file)
    part2(file)  # 6907

    # line = []
    # with open("input.txt", "r") as f:
    #     line = f.readlines()[0]

    # # Sanitize the line
    # line_clean = line[:-1]

    # # Isolate the ID ranges
    # id_ranges = [tuple(ranges.split("-")) for ranges in line_clean.split(",")]
    # id_ranges = [tuple([int(ranges[0]), int(ranges[1])]) for ranges in id_ranges]
    # id_ranges = sorted(id_ranges, key=lambda x: x[0])

    # # Going to try an approach where all possible duplicate sequences are precreated.

    # # 1. identify the largest value to generate
    # #   - only need the second tuple elements
    # largest_value = sorted([id_range[1] for id_range in id_ranges])[-1]

    # # 2. for all duplicate sequences below this value, add them to an ordered list.
    # #   - sequence must appear twice
    # longest_duplicate_sequence_length = int(len(str(largest_value))/2)
    # largest_possible_value = (10 ** longest_duplicate_sequence_length) - 1 
    # value_range = [x for x in range(1, largest_possible_value + 1)] 

    # # Part 1
    # #'''
    # duplicated_values = [int(str(value) + str(value)) for value in value_range]

    # total = 0
    # id_ranges_iter = iter(id_ranges)

    # first_range = next(id_ranges_iter)
    # start_index = first_range[0]
    # end_index = first_range[1]

    # for value in duplicated_values:
    #   while value > end_index:
    #     next_range = []
    #     try:
    #       next_range = next(id_ranges_iter)
    #     except StopIteration:
    #       break
    #     start_index = next_range[0]
    #     end_index = next_range[1]
    #   if value >= start_index and value <= end_index:
    #     total = total + value

    # print(total)