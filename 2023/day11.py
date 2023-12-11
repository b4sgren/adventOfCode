
def parseData(data):
    graph = []
    rows_with_galaxies = [False for _ in range(len(data))]
    cols_with_galaxies = [False for _ in range(len(data[0]))]
    counter = 0
    for i, line in enumerate(data):
        vals = list(line)
        while '#' in vals:
            rows_with_galaxies[i] = True
            idx = vals.index('#')
            cols_with_galaxies[idx] = True
            vals[idx] = str(counter)
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

    return graph


def part1():
    with open('temp.txt', 'r') as f:
        data = f.readlines()

    graph = parseData(data)

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
