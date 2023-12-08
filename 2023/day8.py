
def parseData(data):
    directions = list(data[0])
    directions.pop()

    graph = {}
    for i in range(2, len(data)):
        line = data[i].split()
        node = line[0]
        left = line[2][1:4]
        right = line[3][0:3]

        if i == 2:
            first_node = node

        graph[node] = [left, right]

    return graph, directions, first_node

def part1():
    # with open('temp.txt', 'r') as f:
    with open('day8.txt', 'r') as f:
        data = f.readlines()
    graph, directions, node = parseData(data)

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
    pass

if __name__=="__main__":
    part1()

    part2()
