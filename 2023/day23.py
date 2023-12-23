
def part1():
    with open('temp2.txt', 'r') as f:
        data = f.readlines()

    grid = [list(line[:-1]) for line in data]

    debug = 1

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
