import numpy as np
from math import factorial as f

def parseData(data):
    record = []
    broken_groups = []
    for line in data:
        vals = line.split()
        groups = vals[1].split(',')

        broken_groups.append([int(v) for v in groups])
        record.append(vals[0])

    return record, broken_groups

def part1():
    with open('temp.txt', 'r') as f:
        data = f.readlines()

    records, broken_groups = parseData(data)

    for record, group in zip(records, broken_groups):
        record_list = list(record)
        unknown_ids = [i for i,v in enumerate(record_list) if v == '?']
        num_unknown = record_list.count('?')
        num_broken = record_list.count('#')
        num_working = record_list.count('.')
        total_broken = np.sum(group)
        total_springs = len(record_list)

        broken_springs_left = total_broken - num_broken

        debug = 1


def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
