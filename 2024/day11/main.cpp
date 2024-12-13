#include <algorithm>
#include <fstream>
#include <iostream>
#include <regex>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <vector>

int counterThresh = 75;
int globalCnt = 0;

// Store function calls here
std::map<std::pair<uint64_t, uint64_t>, uint64_t> mapping{};

void parseData(const std::string &file, std::vector<uint64_t> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    std::getline(fin, line);
    std::stringstream ss(line);
    while (std::getline(ss, line, ' ')) {
        data.push_back(std::atoll(line.c_str()));
    }
}

void part1(std::vector<uint64_t> data) {
    for (size_t j{0}; j != counterThresh; ++j) {
        std::vector<uint64_t> new_data = data;
        size_t numInserts{0};
        for (size_t i{0}; i != data.size(); ++i) {
            if (data[i] == 0) {
                ++new_data[i + numInserts];
            } else if (std::to_string(data[i]).size() % 2 == 0) {
                std::string num = std::to_string(data[i]);
                size_t len = num.size() / 2;
                new_data[i + numInserts] = std::atoll(num.substr(0, len).c_str());
                new_data.insert(new_data.begin() + i + numInserts + 1, std::atoll(num.substr(len, len).c_str()));
                ++numInserts;
            } else {
                new_data[i + numInserts] = data[i] * 2024;
            }
        }
        data = new_data;
        // for (auto v : data) {
        //     std::cout << v << " ";
        // }
        // std::cout << "===================================\n"
        //           << std::endl;
    }
    // for (auto v : data) {
    //     std::cout << v << " ";
    // }
    std::cout << "\nPart 1: " << data.size() << std::endl;
}

// Counter = 10, stop on the 5th 8
uint64_t getVector(uint64_t value, uint64_t counter) {
    if (counter == counterThresh) {
        // std::cout << value << " ";
        return 1;  // Just 1 number here
    }

    ++counter;
    std::string num = std::to_string(value);
    if (value == 0) {
        std::pair<uint64_t, uint64_t> pair{value + 1, counter};
        if (mapping.count(pair) != 0) {
            return mapping[pair];
        } else {
            uint64_t cnt = getVector(value + 1, counter);
            mapping.insert({{value + 1, counter}, cnt});
            return cnt;
        }
    } else if (num.size() % 2 == 0) {
        uint64_t val1 = std::stoull(num.substr(0, num.size() / 2));
        uint64_t val2 = std::stoull(num.substr(num.size() / 2, num.size() / 2));
        std::pair<uint64_t, uint64_t> pair1{val1, counter};
        std::pair<uint64_t, uint64_t> pair2{val2, counter};

        uint64_t cnt1{0};
        if (val1 != 0) {
            if (mapping.count(pair1) != 0) {
                cnt1 = mapping[pair1];
            } else {
                cnt1 = getVector(val1, counter);
                mapping.insert({{val1, counter}, cnt1});
            }
        }

        uint64_t cnt2{0};
        if (mapping.count(pair2) != 0) {
            cnt2 = mapping[pair2];
        } else {
            cnt2 = getVector(val2, counter);
            mapping.insert({{val2, counter}, cnt2});
        }
        return cnt1 + cnt2;
    } else {
        std::pair<uint64_t, uint64_t> pair{value * 2024, counter};
        if (mapping.count(pair) != 0) {
            return mapping[pair];
        } else {
            uint64_t cnt = getVector(value * 2024, counter);
            mapping.insert({{value * 2024, counter}, cnt});
            return cnt;
        }
    }
}

// Need some way to speed it up
void part2(std::vector<uint64_t> data) {
    // May need a table of partial mappings
    uint64_t sum{0};
    for (int i{0}; i != data.size(); ++i) {
        uint64_t stepCounter{0};
        std::vector<uint64_t> temp{data[i]};
        // The code for this section
        // Probably easiest with recursion
        sum += getVector(data[i], stepCounter);
    }

    std::cout << "\nPart 2: " << sum << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<uint64_t> data;
    parseData(input_file, data);

    // part1(data);
    part2(data);  // 1066883794  is to low

    return 0;
}
