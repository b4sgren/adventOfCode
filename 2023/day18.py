
def parseData(data):
    directions, distances, colors = [], [], []
    for line in data:
        vals = line[:-1].split()
        directions.append(vals[0])
        distances.append(int(vals[1]))
        colors.append(vals[2][1:-1])

    return directions, distances, colors

def part1():
    with open('temp2.txt', 'r') as f:
        data = f.readlines()

    directions, distances, colors = parseData(data)

    # Get max rows/cols

    # Outline the loop

    # Flood fill

    # Count size

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
