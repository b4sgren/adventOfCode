import numpy as np
import bisect

def parseSection(data, line_num):
    line_num += 1
    line = data[line_num].split()
    src_vals = []
    dest_vals = []
    flag = True

    while(len(line) == 3 and flag):
        dest_num = int(line[0])
        src_num = int(line[1])
        range_num = int(line[2])

        src_vals.append([src_num, src_num + range_num - 1])
        dest_vals.append([dest_num, dest_num + range_num - 1])

        line_num += 1
        if line_num < len(data):
            line = data[line_num].split()
        else:
            flag = False

    line_num += 1
    return src_vals, dest_vals, line_num


def getValueFromMap(val, srcs, dest):
    found_val = False
    for i, src in enumerate(srcs):
        if val >= src[0] and val <= src[1]:
            found_val = True
            dist = val - src[0]
            ans = dest[i][0] + dist
            break

    if found_val is False:
        ans = val

    return ans

def getValue(src_list, data, line_num):
    src_vals, dest_vals, line_num = parseSection(data, line_num)

    dest_list = []
    for val in src_list:
        dest_list.append(getValueFromMap(val, src_vals, dest_vals))

    return dest_list, line_num


def part1():
    # with open('temp.txt', 'r') as f:
    with open('day5.txt', 'r') as f:
        data = f.readlines()

    line = data[0].split(':')[1]
    nums = line.split()
    seeds = [int(val) for val in nums]
    line_num = 2

    soil, line_num = getValue(seeds, data, line_num)
    fertilizer, line_num = getValue(soil, data, line_num)
    water, line_num = getValue(fertilizer, data, line_num)
    light, line_num = getValue(water, data, line_num)
    temperature, line_num = getValue(light, data, line_num)
    humidity, line_num = getValue(temperature, data, line_num)
    locations, line_num = getValue(humidity, data, line_num)


    print(np.min(locations))

def parseSectionSorted(data, line_num):
    src_vals, dest_vals, line_num = parseSection(data, line_num)
    src_vals.sort()
    dest_vals.sort()

    max_val = int(1e14)
    src_vals = np.concatenate(src_vals).tolist()
    src_vals.append(max_val)
    if src_vals[0] > 0:
        src_vals.insert(0, 0)
    dest_vals = np.concatenate(dest_vals).tolist()
    dest_vals.append(max_val)
    if dest_vals[0] > 0:
        dest_vals.insert(0, 0)

    return src_vals, dest_vals, line_num

def getRanges(src_vals, dest_ranges):
    src_ranges = []
    for d_range in dest_ranges:
        min_idx = bisect.bisect_left(src_vals, d_range[0]) - 1
        if min_idx < 0: min_idx += 1
        max_idx = bisect.bisect_left(src_vals, d_range[1]) - 1
        if max_idx < 0: max_idx += 1
        if max_idx == min_idx + 1:
            src_ranges.append((src_vals[min_idx], src_vals[max_idx]))
        else:
            src_ranges.append((src_vals[min_idx], src_vals[min_idx+1]))
            src_ranges.append((src_vals[max_idx], src_vals[max_idx+1]))

    src_ranges = list(set(src_ranges))
    return src_ranges

def getPossibleSeeds(seed_ranges, seeds):
    possible_seeds = []
    for seed_range in seed_ranges:
        for seed in seeds:
            min_seed = seed[0]
            max_seed = seed[0] + seed[1]

            for i in range(seed_range[0], seed_range[1]):
                if not (i >= min_seed and i < max_seed):
                    break
                possible_seeds.append(i)

    possible_seeds = list(set(possible_seeds))
    return possible_seeds

def getValue2(src, src_map, dest_map):
    return getValueFromMap(src, src_map, dest_map)


# dynamic programming approach?? Can't brute force it
def part2():
    # with open('temp.txt', 'r') as f:
    with open('day5.txt', 'r') as f:
        data = f.readlines()

    line = data[0].split(':')[1]
    nums = line.split()
    # pair [seed_num, # of seeds in range]
    seeds = [[int(nums[i]), int(nums[i+1])] for i in range(0, len(nums), 2)]
    line_num = 2


    seed_src_vals, soil_dest_vals, line_num = parseSection(data, line_num)
    soil_src_vals, fertilizer_dest_vals, line_num = parseSection(data, line_num)
    fertilizer_src_vals, water_dest_vals, line_num = parseSection(data, line_num)
    water_src_vals, light_dest_vals, line_num = parseSection(data, line_num)
    light_src_vals, temp_dest_vals, line_num = parseSection(data, line_num)
    temp_src_vals, humid_dest_vals, line_num = parseSection(data, line_num)
    humid_src_vals, location_dest_vals, line_num = parseSection(data, line_num)

    inc = 10000
    flag = True
    location = 1
    while flag is True:
        humidity = getValue2(location, location_dest_vals, humid_src_vals)
        temperature = getValue2(humidity, humid_dest_vals, temp_src_vals)
        light = getValue2(temperature, temp_dest_vals, light_src_vals)
        water = getValue2(light, light_dest_vals, water_src_vals)
        fertilizer = getValue2(water, water_dest_vals, fertilizer_src_vals)
        soil = getValue2(fertilizer, fertilizer_dest_vals, soil_src_vals)
        seed = getValue2(soil, soil_dest_vals, seed_src_vals)

        for s in seeds:
            if seed >= s[0] and seed < s[0] + s[1]:
                flag = False
                break

        location += inc

    location -= 2*inc
    flag = True
    for i in range(location, location+inc, 1):
        humidity = getValue2(i, location_dest_vals, humid_src_vals)
        temperature = getValue2(humidity, humid_dest_vals, temp_src_vals)
        light = getValue2(temperature, temp_dest_vals, light_src_vals)
        water = getValue2(light, light_dest_vals, water_src_vals)
        fertilizer = getValue2(water, water_dest_vals, fertilizer_src_vals)
        soil = getValue2(fertilizer, fertilizer_dest_vals, soil_src_vals)
        seed = getValue2(soil, soil_dest_vals, seed_src_vals)

        for s in seeds:
            if seed >= s[0] and seed < s[0] + s[1]:
                flag = False

        if flag is False:
            break

    print(i)

'''
20284001 is to high
'''

if __name__=="__main__":
    part1()

    part2()
