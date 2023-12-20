class Part:
    def __init__(self, tokens):
        self.x = tokens[0]
        self.m = tokens[1]
        self.a = tokens[2]
        self.s = tokens[3]

class Instructions:
    def __init__(self, inst, default_instr):
        self.default_instr = default_instr
        # [part value, symbol operator, threshold, next instr]
        self.instructions = inst

def parseData(data):
    parts = []
    instructions = {}
    for line in data:
        if len(line) == 1:
            continue
        if line[0] == '{':
            # part
            vals = line[1:-2].split(',')
            temp = []
            for val in vals:
                tokens = val.split('=')
                temp.append(int(tokens[1]))
            parts.append(Part(temp))
        else:
            # instruction
            vals = line[:-1].split('{')
            key = vals[0]
            tokens = vals[1][:-1].split(',')
            default_instr = tokens[-1]
            temp = []
            for i in range(len(tokens)-1):
                steps = tokens[i].split(':')
                id = steps[0][0]
                symbol = steps[0][1]
                val = int(steps[0][2:])
                next_instr = steps[1]
                temp.append([id, symbol, val, next_instr])
            instructions[key] = Instructions(temp, default_instr)

    return parts, instructions


def part1():
    with open('temp2.txt', 'r') as f:
        data = f.readlines()

    parts, instructions = parseData(data)

    # begin in workflow named in

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
