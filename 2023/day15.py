
def parseData(data):
    vals = data.split(',')
    strings = [list(v) for v in vals]
    strings[-1] = strings[-1][:-1]

    return strings

def part1():
    with open('temp2.txt', 'r') as f:
        data = f.readlines()

    strings = parseData(data[0])

    sum = 0
    for string in strings:
        current_value = 0
        for c in string:
            ascii_code = ord(c)
            current_value = 17 * (current_value + ascii_code)
            current_value = current_value % 256
        sum += current_value

    print(sum)


def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
