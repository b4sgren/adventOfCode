
def parseData(data):
    for line in data:
        if len(line) == 1:
            continue
        if line[0] == '{':
            pass  # Part
        else:
            pass # Instruction

def part1():
    with open('temp2.txt', 'r') as f:
        data = f.readlines()

    parts, instructions = parseData(data)

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
