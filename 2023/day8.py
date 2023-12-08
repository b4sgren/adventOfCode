import numpy as np
import math

def parseData(data):
    directions = list(data[0])
    directions.pop()

    graph = {}
    for i in range(2, len(data)):
        line = data[i].split()
        node = line[0]
        left = line[2][1:4]
        right = line[3][0:3]

        graph[node] = [left, right]

    return graph, directions

def part1():
    # with open('temp.txt', 'r') as f:
    with open('day8.txt', 'r') as f:
        data = f.readlines()
    graph, directions = parseData(data)

    node = 'AAA'

    num_directions = len(directions)
    counter = 0
    while node != 'ZZZ':
        direction = directions[counter % num_directions]
        if direction == 'L':
            idx = 0
        else:
            idx = 1

        node = graph[node][idx]
        counter += 1

    print(counter)


def part2():
    # with open('temp.txt', 'r') as f:
    with open('day8.txt', 'r') as f:
        data = f.readlines()
    graph, directions = parseData(data)

    nodes = []
    for key in graph.keys():
        if key[-1] == 'A':
            nodes.append(key)

    orig_nodes = nodes.copy()
    cycles_found = [False for i in range(len(nodes))]
    cycle_len = [0 for i in range(len(nodes))]


    num_directions = len(directions)
    flag = True
    counter = 0
    while flag:
        direction = directions[counter % num_directions]
        if direction == 'L':
            idx = 0
        else:
            idx = 1

        num_z = 0
        for i, node in enumerate(nodes):
            nodes[i] = graph[node][idx]
            if nodes[i][-1] == "Z":
                num_z += 1
                cycles_found[i] = True
                cycle_len[i] = counter
            # if counter > 0 and nodes[i] == orig_nodes[i] and cycles_found[i] is False:
            #     cycles_found[i] = True
            #     cycle_len[i] = counter

        if all(val for val in cycles_found):
            counter = np.product(cycle_len)
            flag = False
            break

        if num_z == len(nodes):
            flag = False

        counter += 1

    # find LCM of a number
    ans = math.lcm(cycle_len)

    print(ans)

'''
815342452108675623720 is too high
'''

if __name__=="__main__":
    part1()

    part2()
