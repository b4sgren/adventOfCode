
def parseData(data):
    snapshot_locations = []
    for line in data:
        vals = line[:-1].split('~')
        temp1 = (int(c) for c in vals[0].split(','))
        temp2 = (int(c) for c in vals[1].split(','))
        snapshot_locations.append((temp1, temp2))

    return snapshot_locations

def part1():
    with open('temp.txt', 'r') as f:
        data = f.readlines()

    snapshot_locations = parseData(data)

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
