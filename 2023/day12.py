import numpy as np
from math import factorial as fact
import itertools
from copy import deepcopy as copy
from functools import cache

def parseData(data):
    record = []
    broken_groups = []
    for line in data:
        vals = line.split()
        groups = vals[1].split(',')

        broken_groups.append([int(v) for v in groups])
        record.append(vals[0])

    return record, broken_groups

def checkValidCombos(combos, group, orig_record):
    valid_combos = 0
    record_size = len(orig_record)
    for combo in combos:
        record = copy(orig_record)
        for id in combo:
            record[id] = '#'

        temp_group = []
        count = 0
        for i, val in enumerate(record):
            if val != '#':
                if count > 0: temp_group.append(count)
                count = 0
            else:
                count += 1

        if val == "#": temp_group.append(count)

        if temp_group == group:
            valid_combos += 1

    return valid_combos

def part1():
    # with open('temp.txt', 'r') as f:
    with open('input.txt', 'r') as f:
        data = f.readlines()

    records, broken_groups = parseData(data)

    total_combinations = 0
    for record, group in zip(records, broken_groups):
        record_list = list(record)
        unknown_ids = [i for i,v in enumerate(record_list) if v == '?']
        num_unknown = record_list.count('?')
        num_broken = record_list.count('#')
        num_working = record_list.count('.')
        total_broken = np.sum(group)
        total_springs = len(record_list)

        broken_springs_left = total_broken - num_broken
        combos = list(itertools.combinations(unknown_ids, int(broken_springs_left)))

        valid_combos = checkValidCombos(combos, group, record_list)
        total_combinations += valid_combos

    print(total_combinations)

@cache
def getNumCombos(record, group):
    # No more groups left. If it doesn't end with # then valid group
    if len(group) == 0:
        return 1 if '#' not in record else 0
    # Not enough characters for required '#'
    if sum(group) + len(group) - 1 > len(record) :
        return 0

    # Not at start of valid group. Shorten string
    if record[0] == '.':
        return getNumCombos(record[1:], group)

    combos = 0
    # If first character is unknown, shorten the string and see if other valid combos
    if record[0] == '?':
        combos += getNumCombos(record[1:], group)

    # Compare with length of the first group
    # 1. Verify group can be valid (no '.' in first n characters)
    # 2. Goal is to make sure that record[group[0]] is not '#'. Makes group invalid. However, we have to check that record is long enough to check that index
    # 2a. Check if record is shorten than the group size
    # 2b. Record is bigger than group size and index group[0] is not '#' (invalid group)
    if '.' not in record[:group[0]] and (len(record) <= group[0] or ( len(record) > group[0] and record[group[0]] != '#')):
        # Go 1 past end of current group to look for a new group
        # Also get rid of the current group
        combos += getNumCombos(record[group[0]+1:], group[1:])

    return combos

# Using recursion
def part1_2():
    with open('temp.txt', 'r') as f:
    # with open('input.txt', 'r') as f:
        data = f.readlines()

    records, broken_groups = parseData(data)

    total_combinations = 0
    for record, group in zip(records, broken_groups):
        total_combinations += getNumCombos(tuple(record), tuple(group))

    print(total_combinations)


# Brute force will take way to long. Think about more efficient solution
def part2():
    # with open('temp.txt', 'r') as f:
    with open('input.txt', 'r') as f:
        data = f.readlines()

    records, broken_groups = parseData(data)

    total_combinations = 0
    for orig_record, orig_group in zip(records, broken_groups):
        # Make the problem bigger
        # group = 5*orig_group
        # record = (5*(orig_record+'?'))[:-1]

        record = list(orig_record)
        group = copy(orig_group)
        for i in range(4):
            record.append('?')
            record.extend(list(orig_record))
            group.extend(orig_group)

        total_combinations += getNumCombos(tuple(record), tuple(group))

    print(total_combinations)


if __name__=="__main__":
    # part1()
    # part1_2()

    part2()
