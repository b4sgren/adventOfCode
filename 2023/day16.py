
def part1():
    grid = []
    with open('temp.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            grid.append(list(line)[:-1])

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
