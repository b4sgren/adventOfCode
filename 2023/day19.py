class Part:
    def __init__(self, tokens):
        self.x = tokens[0]
        self.m = tokens[1]
        self.a = tokens[2]
        self.s = tokens[3]
        self.map = {'x': self.x, 'm': self.m, 'a':self.a, 's':self.s}

    def sum(self):
        return self.x + self.m + self.a + self.s

    def getVal(self, char):
        return self.map[char]

class Instructions:
    def __init__(self, inst, default_instr):
        self.default_instr = default_instr
        # [part value, symbol operator, threshold, next instr]
        self.instructions = inst

    def execute(self, part):
        for instruction in self.instructions:
            if instruction[1] == '<' and part.getVal(instruction[0]) < instruction[2]:
                return instruction[-1]
            elif instruction[1] == '>' and part.getVal(instruction[0]) > instruction[2]:
                return instruction[-1]
        # return default instruction
        return self.default_instr


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
    # with open('temp2.txt', 'r') as f:
    with open('input2.txt', 'r') as f:
        data = f.readlines()

    parts, instructions = parseData(data)

    # begin in workflow named in
    sum = 0
    for part in parts:
        instruction = 'in'
        while instruction != 'A' and instruction != 'R':
            instruction = instructions[instruction].execute(part)

        print(instruction)
        if instruction =='A':
            sum += part.sum()

    print(sum)

# How many combinations of ratings will be accepted
# Range from 1 to 4000 for each part#
def part2():
    with open('temp2.txt', 'r') as f:
    # with open('input2.txt', 'r') as f:
        data = f.readlines()

    _, instructions = parseData(data)


if __name__=="__main__":
    part1()

    part2()
