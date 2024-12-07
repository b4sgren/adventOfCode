#include <algorithm>
#include <fstream>
#include <iostream>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

void parseData(const std::string &file, std::vector<int64_t> &results, std::vector<std::vector<int64_t>> &values) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        std::stringstream ss(line);
        std::string temp;
        std::getline(ss, temp, ':');
        results.push_back(std::atol(temp.c_str()));

        std::vector<int64_t> vals{};
        while (std::getline(ss, temp, ' ')) {
            if (temp.size() == 0) continue;
            vals.push_back(std::atol(temp.c_str()));
        }
        values.push_back(vals);
    }
}

bool generateCombinations(int64_t result, const std::vector<int64_t> &values, size_t size, std::vector<char> current, int64_t sum, std::set<std::vector<char>> &failedCombs) {
    if (size == values.size() - 1 && sum == result) {
        return true;
    } else if (size == values.size() - 1 && sum != result) {
        failedCombs.insert(current);
        return false;
    } else if (sum > result) {
        failedCombs.insert(current);
        return false;
    }

    current.push_back('+');
    if (failedCombs.find(current) == failedCombs.end()) {  // If this combination hasn't failed already
        if (generateCombinations(result, values, size + 1, current, sum + values[size + 1], failedCombs)) return true;
    }
    current.back() = '*';
    if (failedCombs.find(current) == failedCombs.end()) {  // If this combination hasn't failed already
        if (generateCombinations(result, values, size + 1, current, sum * values[size + 1], failedCombs)) return true;
    }

    return false;
}

bool canCombine(int64_t result, std::vector<int64_t> values) {
    int64_t sum{values[0]};
    std::set<std::vector<char>> failedCombs{};
    std::vector<char> current{};
    return generateCombinations(result, values, 0, current, sum, failedCombs);
}

void part1(const std::vector<int64_t> &results, const std::vector<std::vector<int64_t>> &vals) {
    int64_t resultsSum{0};

    for (int i{0}; i != results.size(); ++i) {
        if (canCombine(results[i], vals[i])) {
            resultsSum += results[i];
        }
    }

    std::cout << "Part 1: " << resultsSum << std::endl;
}

bool generateCombinations2(int64_t result, const std::vector<int64_t> &values, size_t size, std::vector<char> current, int64_t sum, std::set<std::vector<char>> &failedCombs) {
    if (size == values.size() - 1 && sum == result) {
        return true;
    } else if (size == values.size() - 1 && sum != result) {
        failedCombs.insert(current);
        return false;
    } else if (sum > result) {
        failedCombs.insert(current);
        return false;
    }

    current.push_back('+');
    if (failedCombs.find(current) == failedCombs.end()) {  // If this combination hasn't failed already
        if (generateCombinations2(result, values, size + 1, current, sum + values[size + 1], failedCombs)) return true;
    }
    current.back() = '*';
    if (failedCombs.find(current) == failedCombs.end()) {  // If this combination hasn't failed already
        if (generateCombinations2(result, values, size + 1, current, sum * values[size + 1], failedCombs)) return true;
    }
    current.back() = '|';
    std::string temp = std::to_string(sum) + std::to_string(values[size + 1]);
    int64_t newSum = std::atol(temp.c_str());
    if (failedCombs.find(current) == failedCombs.end()) {  // If this combination hasn't failed already
        if (generateCombinations2(result, values, size + 1, current, newSum, failedCombs)) return true;
    }

    return false;
}

bool canCombine2(int64_t result, std::vector<int64_t> values) {
    int64_t sum{values[0]};
    std::set<std::vector<char>> failedCombs{};
    std::vector<char> current{};
    return generateCombinations2(result, values, 0, current, sum, failedCombs);
}

void part2(const std::vector<int64_t> &results, const std::vector<std::vector<int64_t>> &vals) {
    int64_t resultsSum{0};

    for (int i{0}; i != results.size(); ++i) {
        if (canCombine2(results[i], vals[i])) {
            resultsSum += results[i];
        }
    }

    std::cout << "Part 2: " << resultsSum << std::endl;
}

int main(int argc, char *argv[]) {
    // if (argc != 2) {
    //     std::cout << "Input the path to the input file" << std::endl;
    //     return 0;
    // }

    // std::string input_file = std::string(argv[1]);
    std::string input_file = "../input.txt";
    std::vector<int64_t> results{};
    std::vector<std::vector<int64_t>> values{};
    parseData(input_file, results, values);

    part1(results, values);
    part2(results, values);

    return 0;
}
