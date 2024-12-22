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

void parseData(const std::string &file, std::vector<int64_t> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        data.push_back(std::stoll(line));
    }
}

void part1(const std::vector<int64_t> &data) {
    int64_t sum{0};

    for (int64_t secretNum : data) {
        for (int i{0}; i != 2000; ++i) {
            // multiply, mix, prune
            secretNum = ((secretNum * 64) ^ secretNum) % MODULO;
            // divide, mix, prune
            secretNum = ((secretNum / 32) ^ secretNum) % MODULO;
            // multiply, mix, prune
            secretNum = ((secretNum * 2048) ^ secretNum) % MODULO;

            // std::cout << secretNum << std::endl;
        }

        sum += secretNum;
    }

    std::cout << "Part 1: " << sum << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<int64_t> data{};
    parseData(input_file, data);

    part1(data);

    return 0;
}
