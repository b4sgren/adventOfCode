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

std::vector<std::vector<int64_t>> getCombos() {
    std::vector<std::vector<int64_t>> combos{};
    combos.reserve(18 * 18 * 18 * 18);
    for (int64_t i{-9}; i != 10; ++i)
        for (int64_t j{-9}; i != 10; ++i)
            for (int64_t k{-9}; i != 10; ++i)
                for (int64_t m{-9}; i != 10; ++i)
                    combos.push_back(std::vector<int64_t>{i, j, k, m});

    return combos;
}

void part2(const std::vector<int64_t> &data) {
    std::vector<std::vector<int>> prices{}, changes{};
    for (int64_t secretNum : data) {
        int prevPrice = secretNum % 10;
        std::vector<int> price{}, change{};
        for (int i{0}; i != 2000; ++i) {
            // multiply, mix, prune
            secretNum = ((secretNum * 64) ^ secretNum) % MODULO;
            // divide, mix, prune
            secretNum = ((secretNum / 32) ^ secretNum) % MODULO;
            // multiply, mix, prune
            secretNum = ((secretNum * 2048) ^ secretNum) % MODULO;

            const int newPrice = secretNum % 10;
            price.push_back(newPrice);
            change.push_back(newPrice - prevPrice);
            prevPrice = newPrice;
        }

        prices.push_back(price);
        changes.push_back(change);
    }

    // FInd the optimal sequence of changes to result in the most bananas
    // Will require dynamic programming?? try brute force first lol
    std::vector<std::vector<int64_t>> combos = getCombos();
    int64_t maxNumBananas{0}, numBananas{0};
    for (auto combo : combos) {
        for (int j{0}; j != prices.size(); ++j) {
            auto change = changes[j];
            for (int i{0}; i != change.size() - 4; ++i) {
                if (change[i] != combo[0] || change[i + 1] != combo[1] || change[i + 2] != combo[2] || change[i + 3] != combo[3])
                    continue;
                numBananas += prices[j][i + 3];
                break;  // stop looking after the first
            }
        }
        if (numBananas > maxNumBananas) maxNumBananas = numBananas;
    }

    std::cout << "Part 2: " << maxNumBananas << std::endl;
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
    part2(data);

    return 0;
}
