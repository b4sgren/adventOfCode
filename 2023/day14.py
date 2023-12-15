from copy import deepcopy as copy

weight_output_map = {}

def printMap(map):
    for line in map:
        print(line)
    print("-----------------------------")

def parseData(data):
    map = []
    for line in data:
        map.append(list(line)[:-1])

    return map

def part1():
    with open("input2.txt", 'r') as f:
        data = f.readlines()
    map = parseData(data)

    num_cols = len(map[0])
    num_rows = len(map)
    for i in range(num_cols):
        for j in range(0, num_rows):
            if map[j][i] != 'O':
                continue
            for k in range(j, 0, -1):
                if map[k-1][i] == '#' or map[k-1][i] == 'O':
                    break
                map[k-1][i] = 'O'
                map[k][i] = '.'

    weight = 0
    for i, line in enumerate(map):
        cnt = line.count('O')
        factor = num_rows - i
        weight += cnt * factor

    print(weight)

def shiftNorth(input):
    map = copy(input)

    num_cols = len(map[0])
    num_rows = len(map)
    for i in range(num_cols):
        for j in range(0, num_rows):
            if map[j][i] != 'O':
                continue
            for k in range(j, 0, -1):
                if map[k-1][i] == '#' or map[k-1][i] == 'O':
                    break
                map[k-1][i] = 'O'
                map[k][i] = '.'
    return map

def shiftSouth(input):
    map = copy(input)

    num_cols = len(map[0])
    num_rows = len(map)
    for i in range(num_cols):
        for j in range(num_rows-1, -1, -1):
            if map[j][i] != 'O':
                continue
            for k in range(j, num_rows-1, 1):
                if map[k+1][i] == '#' or map[k+1][i] == 'O':
                    break
                map[k+1][i] = 'O'
                map[k][i] = '.'
    return map

def shiftWest(input):
    map = copy(input)

    num_cols = len(map[0])
    num_rows = len(map)
    for i in range(num_rows):
        for j in range(0, num_cols):
            if map[i][j] != 'O':
                continue
            for k in range(j, 0, -1):
                if map[i][k-1] == '#' or map[i][k-1] == 'O':
                    break
                map[i][k-1] = 'O'
                map[i][k] = '.'
    return map

def shiftEast(input):
    map = copy(input)

    num_cols = len(map[0])
    num_rows = len(map)
    for i in range(num_rows):
        for j in range(num_cols-1, -1, -1):
            if map[i][j] != 'O':
                continue
            for k in range(j, num_cols-1, 1):
                if map[i][k+1] == '#' or map[i][k+1] == 'O':
                    break
                map[i][k+1] = 'O'
                map[i][k] = '.'
    return map

def cycleRocks(map):
    map1 = shiftNorth(map)
    map2 = shiftWest(map1)
    map3 = shiftSouth(map2)
    map4 = shiftEast(map3)

    return map4

def getWeight(map):
    num_rows = len(map)
    weight1 = 0
    for i, line in enumerate(map):
        cnt = line.count('O')
        factor = num_rows - i
        weight1 += cnt * factor

    num_cols = len(map[0])
    weight2 = 0
    for j in range(num_cols):
        cnt = 0
        for i, line in enumerate(map):
            if map[i][j] == 'O':
                cnt += 1
        factor = num_cols - j
        weight2 += cnt * factor


    return weight1, weight2

# Assume it reaches a steady state. When is the same after starting can stop
# Store the Input and output (induces a cycle)
def part2():
    # with open("temp2.txt", 'r') as f:
    with open("input2.txt", 'r') as f:
        data = f.readlines()
    map = parseData(data)
    weight = getWeight(map)

    num_iters = 1000000000
    for i in range(num_iters):
        if weight in weight_output_map:
            map = weight_output_map[weight]
            first_weight = weight
            weight = getWeight(map)
            break
        else:
            map = cycleRocks(map)
            # Associate weight with the next map
            weight_output_map[weight] = copy(map)
            weight = getWeight(map)
        # print(weight)

    # Other math to determine the final formation
    weight_order = [first_weight]
    loop_length = 1
    while weight != first_weight:
        weight_order.append(weight)
        map = weight_output_map[weight]
        weight = getWeight(map)
        loop_length += 1

    final_weight = weight_order[(num_iters - i-1)%loop_length]
    map = weight_output_map[final_weight]

    print(getWeight(map))


if __name__=="__main__":
    # part1()

    part2()
