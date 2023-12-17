
def part1():
    with open('temp.txt', 'r') as f:
        data = f.readlines()

    # Convert to a grid
    grid = []
    for line in data:
        temp = list(line)[:-1]
        row = [int(v) for v in temp]
        grid.append(row)

    debug = 1

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
