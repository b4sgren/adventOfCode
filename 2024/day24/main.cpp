#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <queue>
#include <regex>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <vector>

void parseData(const std::string &file, std::map<std::string, int> &wireMap, std::vector<std::string> &gateMap) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        if (line.empty()) break;
        size_t idx = line.find(':');
        std::string wire = line.substr(0, idx);
        int val = line.back() - '0';

        wireMap[wire] = val;
    }

    while (std::getline(fin, line))
        gateMap.push_back(line);
}

void part1(std::map<std::string, int> wireMap, const std::vector<std::string> &gateMap) {
    std::vector<bool> flags(gateMap.size(), false);
    while (std::find(flags.begin(), flags.end(), false) != flags.end()) {
        size_t cnt{0};
        for (std::string str : gateMap) {
            // Already performed this operation
            if (flags[cnt]) {
                ++cnt;
                continue;
            }
            std::stringstream ss{str};
            std::string wire1, wire2, wireOut, gate, temp;
            std::getline(ss, wire1, ' ');
            std::getline(ss, gate, ' ');
            std::getline(ss, wire2, ' ');
            std::getline(ss, temp, ' ');
            std::getline(ss, wireOut, ' ');

            // Can't do this one yet
            if (wireMap.count(wire1) == 0 || wireMap.count(wire2) == 0) {
                ++cnt;
                continue;
            }

            if (gate == "AND") {
                wireMap[wireOut] = (wireMap[wire1] == wireMap[wire2] && wireMap[wire1] == 1) ? 1 : 0;
            } else if (gate == "OR") {
                wireMap[wireOut] = (wireMap[wire1] == 1 || wireMap[wire2] == 1) ? 1 : 0;
            } else if (gate == "XOR") {
                wireMap[wireOut] = (wireMap[wire1] != wireMap[wire2]) ? 1 : 0;
            } else {
                std::cout << "ERROR: SHOULDN'T BE HERE" << std::endl;
            }
            flags[cnt] = true;
            ++cnt;
        }
    }

    // Compile the number
    int64_t num{0};
    for (auto it{wireMap.rbegin()}; it != wireMap.rend(); ++it) {
        std::cout << it->first << " " << it->second << std::endl;
        if (it->first[0] != 'z') continue;
        num = (num << 1) + it->second;
    }

    std::cout << "Part 1: " << num << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::map<std::string, int> wireMap{};
    std::vector<std::string> gateMap{};
    parseData(input_file, wireMap, gateMap);

    part1(wireMap, gateMap);

    return 0;
}
