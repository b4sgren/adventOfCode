import numpy as np

def parseSection(data, line_num):
    line_num += 1
    line = data[line_num].split()
    src_dest_map = {}
    flag = True

    while(len(line) == 3 and flag):
        dest_num = int(line[0])
        src_num = int(line[1])
        range_num = int(line[2])

        # Enter values here
        for i in range(range_num):
            src_dest_map[src_num+i] = dest_num + i

        line_num += 1
        if line_num < len(data):
            line = data[line_num].split()
        else:
            flag = False

    line_num += 1
    return src_dest_map, line_num

def getValue(val, map):
    if val in map.keys():
        ans = map[val]
    else:
        ans = val

    return ans


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

def part1():
    # with open('temp.txt', 'r') as f:
    with open('day5.txt', 'r') as f:
        data = f.readlines()
    parseFile(data)
    seeds, seed_soil_map, soil_fertilizer_map, fertilizer_water_map, water_light_map, light_temperature_map, temperature_humidity_map, humidity_location_map = parseFile(data)

    location_nums = []
    for seed in seeds:
        soil = getValue(seed, seed_soil_map)
        fertilizer = getValue(soil, soil_fertilizer_map)
        water = getValue(fertilizer, fertilizer_water_map)
        light = getValue(water, water_light_map)
        temperature = getValue(light, light_temperature_map)
        humidity = getValue(temperature, temperature_humidity_map)
        location = getValue(humidity, humidity_location_map)

        location_nums.append(location)

    print(np.min(location_nums))

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
