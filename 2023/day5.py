
def parseSection(data, line_num):
    line_num += 1
    line = data[line_num].split()
    src_dest_map = {}
    while(len(line) == 3):
        dest_num = int(line[0])
        src_num = int(line[1])
        range_num = int(line[2])

        # Enter values here

        line_num += 1
        line = data[line_num].split()

    return src_dest_map, line_num


def parseFile(data):
    line = data[0].split(':')[1]
    seeds = [int(val) for val in line]

    line_num = 2
    # seed-to-soil map:
    seed_soil_map, line_num = parseSection(data, line_num)

    # soil-to-fertilizer map
    soil_fertilizer_map = {}

    # fertilizer-to-water map:
    fertilizer_water_map = {}

    # water-to-light map:
    water_light_map = {}

    #light-to-temperature map:
    light_temperature_map = {}

    # temperature-to-humidity map:
    temperature_humidity_map = {}

    # humidity-to-location map
    humidity_location_map = {}

    return seeds, seed_soil_map, soil_fertilizer_map, fertilizer_water_map, water_light_map, light_temperature_map, temperature_humidity_map, humidity_location_map

def part1():
    with open('temp.txt', 'r') as f:
    # with open('day5.txt', 'r') as f:
        data = f.readlines()
    parseFile(data)

def part2():
    pass

if __name__=="__main__":
    part1()

    part2()
