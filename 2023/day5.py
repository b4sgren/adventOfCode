import numpy as np

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


def parseFile(data):
    line = data[0].split(':')[1]
    nums = line.split()
    seeds = [int(val) for val in nums]

    line_num = 2
    # seed-to-soil map:
    seed_soil_map, line_num = parseSection(data, line_num)

    # soil-to-fertilizer map
    soil_fertilizer_map, line_num = parseSection(data, line_num)

    # fertilizer-to-water map:
    fertilizer_water_map, line_num = parseSection(data, line_num)

    # water-to-light map:
    water_light_map, line_num = parseSection(data, line_num)

    #light-to-temperature map:
    light_temperature_map, line_num = parseSection(data, line_num)

    # temperature-to-humidity map:
    temperature_humidity_map, line_num = parseSection(data, line_num)

    # humidity-to-location map
    humidity_location_map, line_num = parseSection(data, line_num)

    return seeds, seed_soil_map, soil_fertilizer_map, fertilizer_water_map, water_light_map, light_temperature_map, temperature_humidity_map, humidity_location_map


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
    # seeds, seed_soil_map, soil_fertilizer_map, fertilizer_water_map, water_light_map, light_temperature_map, temperature_humidity_map, humidity_location_map = parseFile(data)

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

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
