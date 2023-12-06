import numpy as np

def parseData(data):
    line = data[0].split(':')[1]
    vals = line.split()
    times = [int(val) for val in vals]

    line = data[1].split(':')[1]
    vals = line.split()
    distances = [int(val) for val in vals]

    return times, distances

def parseData2(data):
    line = data[0].split(':')[1]
    vals = line.split()
    time = ''
    for val in vals:
        time += val
    times = [int(time)]

    line = data[1].split(':')[1]
    vals = line.split()
    dist = ''
    for val in vals:
        dist += val
    distances = [int(dist)]

    return times, distances


def findIntMax(time):
    max = int(time/2)

    return max

def findWaysToWin(time, record_dist, optimal_hold):
    counter = 0
    low_time = optimal_hold
    flag = True
    while flag and low_time > 0:
        dist = low_time * (time - low_time)
        if dist > record_dist:
            counter += 1
        else :
            flag = False
        low_time -= 1

    high_time = optimal_hold + 1
    flag = True
    while flag and high_time < time:
        dist = high_time * (time - high_time)
        if dist > record_dist:
            counter += 1
        else:
            flag = False
        high_time += 1

    return counter

def part1():
    # with open('temp2.txt', 'r') as f:
    with open('day6.txt', 'r') as f:
        data = f.readlines()

    times, distances = parseData(data)

    ways_to_win = []
    for time, dist in zip(times, distances):
        optimal_hold = findIntMax(time)
        ways_to_win.append(findWaysToWin(time, dist, optimal_hold))

    print(np.product(ways_to_win))



def part2():
    # with open('temp2.txt', 'r') as f:
    with open('day6.txt', 'r') as f:
        data = f.readlines()

    times, distances = parseData2(data)

    ways_to_win = []
    for time, dist in zip(times, distances):
        optimal_hold = findIntMax(time)
        ways_to_win.append(findWaysToWin(time, dist, optimal_hold))

    print(np.product(ways_to_win))

if __name__=="__main__":
    # part1()

    part2()
