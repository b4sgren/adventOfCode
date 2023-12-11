import math
import numpy as np

def parseData(data):
    graph = []
    rows_with_galaxies = [False for _ in range(len(data))]
    cols_with_galaxies = [False for _ in range(len(data[0]))]
    counter = 0
    for i, line in enumerate(data):
        vals = list(line)[:-1]
        while '#' in vals:
            rows_with_galaxies[i] = True
            idx = vals.index('#')
            cols_with_galaxies[idx] = True
            vals[idx] = str(counter)
            counter += 1
        graph.append(vals)

    # Append space where no galaxies are in a row/col
    offset = 0
    for i, val in enumerate(rows_with_galaxies):
        if not val:
            graph.insert(i + offset, ['.']*len(graph[0]))
            offset += 1

    offset = 0
    for i, val in enumerate(cols_with_galaxies):
        if not val:
            for j in range(len(graph)):
                graph[j].insert(i+offset, '.')
            offset += 1

    return graph, counter


def part1():
    # with open('temp.txt', 'r') as f:
    with open('input.txt', 'r') as f:
        data = f.readlines()

    graph, num_galaxies = parseData(data)

    paths_dict = {}
    for i in range(num_galaxies-1):
        for j in range(i+1,num_galaxies):
            paths_dict[(i, j)] = []

    locations_dict = {}
    # Can just use addition and subtraction for apsp
    for i in range(num_galaxies):
        for j, line in enumerate(graph):
            if str(i) not in line:
                continue
            idx = line.index(str(i))
            locations_dict[i] = [j, idx]
            break

    path_length_dict = {}
    for key, loc in locations_dict.items():
        for key2, loc2 in locations_dict.items():
            if key == key2:
                continue

            path_length = abs(loc[0] - loc2[0]) + abs(loc[1] - loc2[1])
            path_key = [key, key2]
            path_key.sort()
            path_length_dict[tuple(path_key)] = path_length

    print(np.sum(list(path_length_dict.values())))




def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
