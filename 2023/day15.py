
def parseData(data):
    vals = data.split(',')
    strings = [list(v) for v in vals]
    strings[-1] = strings[-1][:-1]

    return strings

def part1():
    with open('temp2.txt', 'r') as f:
        data = f.readlines()

    strings = parseData(data[0])
    debug = 1

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
