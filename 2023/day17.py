from collections import defaultdict
from heapq import heappop, heappush
import itertools

# help from here: https://github.com/tmo1/adventofcode/blob/main/2023/17.py

# part 1
heap = []
entries_map = {}
cost = defaultdict(lambda: 1e8)

def part1():
    with open('temp2.txt', 'r') as f:
        data = f.readlines()

    # Convert to a grid
    grid = []
    for line in data:
        temp = list(line)[:-1]
        row = [int(v) for v in temp]
        grid.append(row)

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
