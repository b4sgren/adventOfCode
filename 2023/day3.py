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

    if tracking_number:
        numbers.append(num)

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

def find_num(line, num):
    indices = [i for i in range(len(line)) if line[i] == num[0]]

    max_id = len(line)
    size = len(num)

    vals = []
    for idx in indices:
        is_num = True
        # No digits preceding the number
        if idx > 0 and line[idx-1].isdigit() is True:
            is_num = False
        # no digits right after number + length of number
        if idx+size < max_id and line[idx+size].isdigit() is True:
            is_num = False
        for i in range(1, len(num)):
            if idx+i >= max_id or line[idx+i] != num[i]:
                is_num = False
                break
        if is_num is True:
            vals.append(idx)  # if all digits appear then append the start index

    return vals


def get_gear_locations(idx, size, line, gear_dict, num, line_num):
    locs = []
    if idx > 0:
        if line[idx-1] == '*':
            if (line_num, idx-1) not in gear_dict.keys():
                gear_dict[(line_num, idx-1)] = []
            gear_dict[(line_num, idx-1)].append(num)
            locs.append((line_num, idx-1))

    if idx+size < len(line):  # idx + size to get to end of line. -1 to ignore new line character
        if line[idx+size] == '*':
            if (line_num, idx+size) not in gear_dict.keys():
                gear_dict[(line_num, idx+size)] = []

            gear_dict[(line_num, idx+size)].append(num)
            locs.append((line_num, idx+size))

    for i in range(idx, idx+size):
        if line[i] == '*':
            if (line_num, i) not in gear_dict.keys():
                gear_dict[(line_num, i)] = []

            gear_dict[(line_num, i)].append(num)
            locs.append((line_num, i))

    return gear_dict, locs


def is_gear(idxs, size, prev_line, line, next_line, gear_dict, num, line_num):
    # Can be connected to multiple stars
    # prev line
    locs = []
    for idx in idxs:
        if not prev_line is None:
            gear_dict, locs = get_gear_locations(idx, size, prev_line, gear_dict, num, line_num-1)

        # current line
        gear_dict, temp = get_gear_locations(idx, size, line, gear_dict, num, line_num)
        locs.extend(temp)

        # next line
        if not next_line is None:
            gear_dict, temp = get_gear_locations(idx, size, next_line, gear_dict, num, line_num+1)
            locs.extend(temp)

    return gear_dict, locs

def part2():
    with open('day3.txt', 'r') as f:
    # with open('temp.txt', 'r') as f:  # answer is 467835
        temp = f.readlines()
        data = [list(line) for line in temp]

    gear_dict = {}  # key is index of *, value are the numbers connected to it

    prev_line = None
    next_line = data[1]
    for i, line in enumerate(data):
        line = line[:-1]  # get rid of \n
        if i == 3:
            debug = 1
        numbers, symbols = getNumbersInLine(line)
        numbers = list(set(numbers))  # get unique elements
        debug = 1
        for num in numbers:
            if num == '941':
                debug = 1
            idx = find_num(line, num)
            size = len(num)
            n = int(num)

            gear_dict, locations = is_gear(idx, size, prev_line, line, next_line, gear_dict, n, i)

            if len(locations) > 0:
                print(i, num)
                print(locations)
                print("-----------------------------")
                debug = 1

        prev_line = data[i]
        if i + 2 < len(data):
            next_line = data[i+2]
        else:
            next_line = None

    # print(list(gear_dict.keys()))
    keys = list(gear_dict.keys())
    keys.sort()
    for key in keys:
        print(key, len(gear_dict[key]), gear_dict[key])

    ratio = 0
    for key, vals in gear_dict.items():
        if len(vals) == 2:
            ratio += vals[0] * vals[1]
    print(ratio)

'''
Part 2 notes:
73307538 is too low
73904898 is too low
74707315 is too low
76263677 is not right
77509019 is right. Several bugs with parsing >:(
'''


if __name__=="__main__":
    part1()

    part2()
