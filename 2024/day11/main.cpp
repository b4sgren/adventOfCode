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
    for (size_t j{0}; j != 25; ++j) {
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
    }
    std::cout << "Part 1: " << data.size() << std::endl;
}

// Need some way to speed it up
void part2(std::vector<uint64_t> data) {
    // May need a table of partial mappings
    std::map<uint64_t, std::vector<uint64_t>> baseMappings{
        {0, std::vector<uint64_t>{1}},
        {1, std::vector<uint64_t>{2, 0, 2, 4}},
        {2, std::vector<uint64_t>{4, 0, 4, 8}},
        {3, std::vector<uint64_t>{6, 0, 7, 2}},
        {4, std::vector<uint64_t>{8, 0, 9, 6}},
        {5, std::vector<uint64_t>{2, 0, 4, 8, 2, 8, 8, 0}},
        {6, std::vector<uint64_t>{2, 4, 5, 7, 9, 4, 5, 6}},
        {7, std::vector<uint64_t>{2, 8, 6, 7, 6, 0, 3, 2}},
        {8, std::vector<uint64_t>{3, 2, 7, 7, 2, 6, 0, 8}},
        {9, std::vector<uint64_t>{3, 6, 8, 6, 9, 1, 8, 4}},
    };
    std::map<uint64_t, int> numSteps{{0, 1}, {1, 3}, {2, 3}, {3, 3}, {4, 3}, {5, 5}, {6, 5}, {7, 5}, {8, 5}, {9, 5}};
    std::vector<int> stepCnt(data.size(), 0);

    std::vector<uint64_t> newData{};
    for (int i{0}; i != data.size(); ++i) {
        int stepCounter{0};
        std::vector<uint64_t> temp{data[i]};
        while (stepCounter != 75) {
            // The code for this section
            // Probably easiest with recursion
        }
    }

    std::cout << "Part 2: " << data.size() << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<uint64_t> data;
    parseData(input_file, data);

    part1(data);
    part2(data);

    return 0;
}
