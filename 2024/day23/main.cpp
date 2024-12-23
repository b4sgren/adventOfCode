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

constexpr int64_t MODULO = 16777216;

void parseData(const std::string &file, std::map<std::string, std::vector<std::string>> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        const std::string com1 = line.substr(0, 2);
        const std::string com2 = line.substr(3, 2);

        data[com1].push_back(com2);
        data[com2].push_back(com1);
    }

    // Sort alphabetically
    for (auto &pair : data) {
        std::sort(pair.second.begin(), pair.second.end());
    }
}

void part1(std::map<std::string, std::vector<std::string>> data) {
    std::set<std::vector<std::string>> groups{};

    for (auto pair : data) {
        if (pair.first[0] != 't') continue;
        if (pair.second.size() < 2) continue;  // Can't for a clique of size 3

        for (size_t i{0}; i != pair.second.size() - 1; ++i) {
            std::string str1 = pair.second[i];
            for (size_t j{i + 1}; j != pair.second.size(); ++j) {
                std::string str2 = pair.second[j];
                auto it = std::find(data[str1].begin(), data[str1].end(), str2);
                if (it != data[str1].end()) {
                    std::vector<std::string> temp{pair.first, str1, str2};
                    std::sort(temp.begin(), temp.end());
                    groups.insert(temp);
                }
            }
        }
    }

    std::cout << "Part 1: " << groups.size() << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::map<std::string, std::vector<std::string>> data{};
    parseData(input_file, data);

    part1(data);

    return 0;
}
