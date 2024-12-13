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
uint64_t getVector(uint64_t value, int counter) {
    std::map<uint64_t, std::vector<uint64_t>> baseMappings{
        {0, std::vector<uint64_t>{1}},
        {1, std::vector<uint64_t>{2, 0, 2, 4}},
        {2, std::vector<uint64_t>{4, 0, 4, 8}},
        {3, std::vector<uint64_t>{6, 0, 7, 2}},
        {4, std::vector<uint64_t>{8, 0, 9, 6}},
        {5, std::vector<uint64_t>{2, 0, 4, 8, 2, 8, 8, 0}},
        {6, std::vector<uint64_t>{2, 4, 5, 7, 9, 4, 5, 6}},
        {7, std::vector<uint64_t>{2, 8, 6, 7, 6, 0, 3, 2}},
        // {8, std::vector<uint64_t>{3, 2, 7, 7, 2, 6, 0, 8}},
        {8, std::vector<uint64_t>{32, 77, 26, 8}},
        {9, std::vector<uint64_t>{3, 6, 8, 6, 9, 1, 8, 4}},
    };
    std::map<uint64_t, int> numSteps{{0, 1}, {1, 3}, {2, 3}, {3, 3}, {4, 3}, {5, 5}, {6, 5}, {7, 5}, {8, 4}, {9, 5}};

    if (counter == 10 && value == 8096) {
        // if (counter == 10 && globalCnt > 40) {
        ++counter;
        --counter;
    }

    if (counter == counterThresh) {
        // std::cout << value << " ";
        return 1;
    }

    std::string num = std::to_string(value);
    if (num.size() == 1) {  // 1 digit
        if (counter + numSteps[value] <= counterThresh) {
            counter += numSteps[value];
            auto vec = baseMappings[value];
            // Recursively call each element in vec, concatenate to temp and return temp
            uint64_t cnt{0};
            for (uint64_t val : vec) {
                cnt += getVector(val, counter);
            }
            return cnt;
        } else {
            ++counter;
            if (value == 0) {
                return getVector(value + 1, counter);
            } else if (num.size() % 2 == 0) {
                if (num == "08") {
                    ++counter;
                    --counter;
                }
                uint64_t val1 = std::stoull(num.substr(0, num.size() / 2));
                uint64_t val2 = std::stoull(num.substr(num.size() / 2, num.size() / 2));
                if (val1 != 0)
                    return getVector(val1, counter) + getVector(val2, counter);
                else
                    return getVector(val2, counter);

            } else {
                return getVector(value * 2024, counter);
            }
        }
    } else if (num.size() % 2 == 0) {
        ++counter;
        if (num == "08") {
            ++counter;
            --counter;
        }

        std::vector<uint64_t> temp{std::stoull(num.substr(0, num.size() / 2)),
                                   std::stoull(num.substr(num.size() / 2, num.size() / 2))};
        uint64_t cnt1 = 0;
        if (temp[0] != 0) cnt1 = getVector(temp[0], counter);
        uint64_t cnt2 = getVector(temp[1], counter);
        return cnt1 + cnt2;
    } else {
        ++counter;
        return getVector(value * 2024, counter);
    }
}

// Need some way to speed it up
void part2(std::vector<uint64_t> data) {
    // May need a table of partial mappings
    uint64_t sum{0};
    for (int i{0}; i != data.size(); ++i) {
        int stepCounter{0};
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
    part2(data);

    return 0;
}
