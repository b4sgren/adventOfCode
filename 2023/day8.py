
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

        if num_z == len(nodes):
            flag = False

        counter += 1

    print(counter)

if __name__=="__main__":
    part1()

    part2()
