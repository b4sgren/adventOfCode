import numpy as np
from copy import deepcopy as copy
num_paths = {}  # Map of number of paths
num_paths2 = {} # Map of the actual paths

def computeNumPaths(graph, node):
    global num_paths
    if node == 'out':
        return 1
    if node in num_paths.keys():
        return num_paths[node]
    
    sum = 0
    for n in graph[node]:
        sum += computeNumPaths(graph, n)
    num_paths[node] = sum

    return sum

def part1(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    graph = {}
    for line in data:
        vals = line.split(':')
        edges = vals[1].split()
        graph[vals[0]] = edges
    
    # Do a DFS with memoization
    computeNumPaths(graph, 'you')
    print(num_paths['you'])

def computeNumPaths2(graph, node, path):
    global num_paths2
    if ('fft' in path and node == 'dac') or ('dac' in path and node == 'fft'):
        return 1
    if node in num_paths2.keys():
        return num_paths2[node]
    if node == 'out':
        return 0
    
    path.append(node)
    paths = []
    sum = 0
    for n in graph[node]:
        sum += computeNumPaths2(graph, n, path)  # All nodes from n to the end
    num_paths2[node] = sum

    return sum

# way to many paths... need a way to cut out the ones that don't have the right nodes
def part2(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    graph = {}
    for line in data:
        vals = line.split(':')
        edges = vals[1].split()
        graph[vals[0]] = edges
    
    total = computeNumPaths2(graph, 'svr', [])

    print(total)


if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt"  # 7450 is to low

    # part1(file)
    part2(file)
