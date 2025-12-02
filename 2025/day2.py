import math

def invalidPartsInRange(id1, id2):
    min_digits = math.floor(len(id1)/2.0)
    max_digits = math.floor(len(id2)/2.0)+1

    if min_digits > 0:
        x0 = int(id1[:min_digits])
    else:
        x0 = 1
    xf = int(id2[:max_digits])

    max_num = float(id2)
    min_num = float(id1)
    invalid_ids = []
    # Maybe max_digits + 1
    for i in range(x0, xf+1):
        num_str = str(i) + str(i)
        num = float(num_str)
        if num >= min_num and num <= max_num:
            invalid_ids.append(num_str)
    
    return invalid_ids


def part1(file):
    with open(file, 'r') as f:
        data = f.readlines()
    
    # Don't count repeat serial numbers
    invalid_ids = []
    sum = 0
    id_ranges = data[0].split(',')
    for id_range in id_ranges:
        ids = id_range.split('-')
        temp_ids = invalidPartsInRange(ids[0], ids[1])
        # print(ids, temp_ids)
        debug = 1
        for id in temp_ids:
            if id not in invalid_ids:
                invalid_ids.append(id)
                sum += int(id)
    
    print(sum)

if __name__=="__main__":
    # file = "test_input.txt"
    file = "input.txt" # 505725543457 is to high for part 1

    part1(file)
    # part2(file)  # 6907

