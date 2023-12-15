
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


def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
