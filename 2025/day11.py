num_paths = {}

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

if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt"

    part1(file)
    # part2(file)
