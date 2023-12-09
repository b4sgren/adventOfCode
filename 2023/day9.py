import numpy as np

def parseData(data):
    readings = []
    for line in data:
        vals = line.split()
        temp = [int(val) for val in vals]
        readings.append(np.array(temp))

    return readings


def part1():
    # with open('temp.txt', 'r') as f:
    with open('day9.txt', 'r') as f:
        data = f.readlines()

    readings = parseData(data)

    sum = 0
    for reading in readings:
        diff = np.diff(reading)
        history = [reading]
        while np.any(diff):
            history.append(diff)
            diff = np.diff(diff)

        history.reverse()
        val = 0
        for i in range(len(history)):
            val += history[i][-1]

        # print(val)
        sum += val


    print(sum)


def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
