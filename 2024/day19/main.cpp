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

std::map<std::string, bool> mapping{};

void parseData(const std::string &file, std::vector<std::string> &towels, std::vector<std::string> &designs) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    std::getline(fin, line);
    std::stringstream ss{line};
    std::string temp;
    while (std::getline(ss, temp, ',')) {
        // strip white space
        temp.erase(std::remove_if(temp.begin(), temp.end(), ::isspace), temp.end());
        towels.push_back(temp);
    }

    while (std::getline(fin, line)) {
        if (line.size() == 0) continue;
        designs.push_back(line);
    }
}

bool canMakeDesign(const std::string &design, const std::vector<std::string> &towels) {
    if (mapping.count(design) != 0) return mapping[design];

    for (std::string towel : towels) {
        const size_t size = towel.size();
        if (size > design.size()) continue;
        if (size == design.size() && towel == design) {
            mapping[design] = true;
            return true;
        } else if (size == design.size()) {
            continue;
        }

        const std::string temp = design.substr(0, size);
        if (temp == towel) {
            if (canMakeDesign(design.substr(size), towels)) {
                mapping[design] = true;
                return true;
            }
        }
    }

    mapping[design] = false;
    return false;
}

// Have to use dynamic programming
void part1(const std::vector<std::string> &towels, const std::vector<std::string> &designs) {
    int numPossible{0};

    for (std::string design : designs) {
        mapping.clear();
        if (canMakeDesign(design, towels))
            ++numPossible;
    }

    std::cout << "Part 1: " << numPossible << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<std::string> towels{};
    std::vector<std::string> designs{};
    parseData(input_file, towels, designs);

    part1(towels, designs);

    return 0;
}
