
def parseData(data):
    vals = data.split(',')
    strings = [list(v) for v in vals]
    strings[-1] = strings[-1][:-1]

    return strings

def part1():
    with open('input2.txt', 'r') as f:
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
    # with open('temp2.txt', 'r') as f:
    with open('2023/input2.txt', 'r') as f:
        data = f.readlines()

    strings_list = parseData(data[0])
    strings = data[0].split(',')
    strings[-1] = strings[-1][:-1]

    hash_map = {}
    for i in range(256):
        hash_map[i] = []

    sum = 0
    for string, str in zip(strings_list, strings):
        current_value = 0
        if '-' in string:
            idx = string.index('-')
        elif '=' in string:
            idx = string.index('=')


        for c in string[:idx]:
            ascii_code = ord(c)
            current_value = 17 * (current_value + ascii_code)
            current_value = current_value % 256

        if '=' in string:
            vals = str.split('=')
            label = vals[0] + ' ' + vals[1]
            if len(hash_map[current_value]) == 0:
                hash_map[current_value].append(label)
            else:
                found = False
                for i, temp in enumerate(hash_map[current_value]):
                    if vals[0] == temp[:len(vals[0])]:
                        found = True
                        hash_map[current_value][i] = label
                        break
                if found is False:
                    hash_map[current_value].append(label)
        elif '-' in string:
            vals = str.split('-')
            label = vals[0] + ' ' + vals[1]
            for i, temp in enumerate(hash_map[current_value]):
                if vals[0] == hash_map[current_value][i][:len(vals[0])]:
                    hash_map[current_value].pop(i)
                    break
        else:
            debug = 1

    sum = 0
    for box_number, vals in hash_map.items():
        print(vals)
        for i, string in enumerate(vals):
            sum += (box_number+1) * (i+1) * int(string[-1])

    print(sum)

'''
285036 is too low
'''

if __name__=="__main__":
    # part1()

    part2()
