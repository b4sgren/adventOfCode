import numpy as np

def is_symbol(c):
    return (not c.isdigit() and not c == '.')

def printLines(prev, curr, next):
    print(prev)
    print(curr)
    print(next)

def getNumbersInLine(line):
    numbers = []
    symbols = []

    tracking_number = False
    num = ''
    for i, char in enumerate(line):
        tracking_number = char.isdigit()
        if tracking_number:
            num = num + char
        elif not tracking_number and len(num) > 0:
            numbers.append(num)
            num = ''
        elif not tracking_number and not char == '.' and not char =='\n':
            symbols.append(char)

    return numbers, symbols

def check_line(idx, size, line):
    b1 = False
    b2 = False
    if idx > 0:
        b1 = is_symbol(line[idx-1])
    if idx+size < len(line)-1:  # idx + size to get to end of line. -1 to ignore new line character
        b2 = is_symbol(line[idx + size])
    if b1 or b2:
        return True

    for i in range(idx, idx+size):
        if is_symbol(line[i]):
            return True

    return False

def is_part_num(idx, size, prev_line, line, next_line):
    # Check prev line
    if not prev_line is None:
        if check_line(idx, size, prev_line):
            return True

    # Check line
    if check_line(idx, size, line):
        return True

    # Check next line
    if not next_line is None:
        if check_line(idx, size, next_line):
            return True

    return False

def part1():
    with open('day3.txt', 'r') as f:
    # with open('temp.txt', 'r') as f:  # answer is 4361
    # with open('temp2.txt', 'r') as f:  # answer is 925
        data = f.readlines()

    prev_line = None
    next_line = data[1]
    part_nums = []
    for i, line in enumerate(data):
        numbers, symbols = getNumbersInLine(line)
        for num in numbers:
            idx = line.find(num)
            size = len(num)

            if is_part_num(idx, size, prev_line, line, next_line):
                part_nums.append(int(num))
            line = line[:idx] + "."*size + line[idx+size:]

        prev_line = data[i]
        if i + 2 < len(data):
            next_line = data[i+2]
        else:
            next_line = None

    print(np.sum(part_nums))

def get_gear_locations(idx, size, line, gear_dict, num, line_num):
    if idx > 0:
        if line[idx-1] == '*':
            if (line_num, idx-1) not in gear_dict.keys():
                gear_dict[(line_num, idx-1)] = []
            gear_dict[(line_num, idx-1)].append(num)
    if idx+size < len(line)-1:  # idx + size to get to end of line. -1 to ignore new line character

        if line[idx+size] == '*':
            if (line_num, idx+size) not in gear_dict.keys():
                gear_dict[(line_num, idx+size)] = []

            gear_dict[(line_num, idx+size)].append(num)

    for i in range(idx, idx+size):
        if line[i] == '*':
            if (line_num, i) not in gear_dict.keys():
                gear_dict[(line_num, i)] = []

            gear_dict[(line_num, i)].append(num)

    return gear_dict



def is_gear(idx, size, prev_line, line, next_line, gear_dict, num, line_num):
    # Can be connected to multiple stars
    # prev line
    if not prev_line is None:
        gear_dict = get_gear_locations(idx, size, prev_line, gear_dict, num, line_num-1)

    # current line
    gear_dict = get_gear_locations(idx, size, line, gear_dict, num, line_num)

    # next line
    if not next_line is None:
        gear_dict = get_gear_locations(idx, size, next_line, gear_dict, num, line_num+1)

    return gear_dict

def part2():
    with open('day3.txt', 'r') as f:
    # with open('temp.txt', 'r') as f:  # answer is 467835
    # with open('temp2.txt', 'r') as f:  # answer is 6756
        data = f.readlines()

    gear_dict = {}  # key is index of *, value are the numbers connected to it

    prev_line = None
    next_line = data[1]
    for i, line in enumerate(data):
        numbers, symbols = getNumbersInLine(line)
        for num in numbers:
            idx = line.find(num)
            size = len(num)
            n = int(num)
            if n == 82:
                debug = 1

            gear_dict = is_gear(idx, size, prev_line, line, next_line, gear_dict, n, i)

        prev_line = data[i]
        if i + 2 < len(data):
            next_line = data[i+2]
        else:
            next_line = None

    for line in data:
        print(line)
    print(gear_dict)

    ratio = 0
    for key, vals in gear_dict.items():
        if len(vals) == 2:
            ratio += vals[0] * vals[1]
    print(ratio)

'''
Part 2 notes:
73307538 is too low
'''


if __name__=="__main__":
    # part1()

    part2()
