import numpy as np

def is_symbol(c):
    return (not c.isdigit() and not c == '.')

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
    if idx < len(line):
        b2 = is_symbol(line[idx + size + 1])
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
    # with open('day3.txt', 'r') as f:
    with open('temp.txt', 'r') as f:
        data = f.readlines()
        max_lines = len(data)

    prev_line = None
    next_line = data[1]
    part_nums = []
    for i, line in enumerate(data):
        numbers, symbols = getNumbersInLine(line)
        for num in numbers:
            idx = line.find(num)
            if is_part_num(idx, len(num), prev_line, line, next_line):
                part_nums.append(int(num))

    print(np.sum(part_nums))


if __name__=="__main__":
    part1()

    # part2()
