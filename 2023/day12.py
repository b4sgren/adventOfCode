import numpy as np
from math import factorial as fact
import itertools
from copy import deepcopy as copy

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

# Brute force will take way to long. Think about more efficient solution
def part2():
    with open('temp.txt', 'r') as f:
    # with open('input.txt', 'r') as f:
        data = f.readlines()

    records, broken_groups = parseData(data)

    total_combinations = 0
    for orig_record, orig_group in zip(records, broken_groups):
        # Make the problem bigger
        group = copy(orig_group)
        record = list(orig_record)
        for i in range(5):
            record.append('?')
            record.extend(list(orig_record))
            group.extend(orig_group)

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


if __name__=="__main__":
    # part1()

    part2()
