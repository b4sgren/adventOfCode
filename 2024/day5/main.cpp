#include <fstream>
#include <iostream>
#include <map>
#include <regex>
#include <sstream>
#include <string>
#include <vector>

void parseData(const std::string &file, std::map<int, std::vector<int>> &pageOrders, std::vector<std::vector<int>> &updates) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        if (line.size() == 0) continue;
        size_t idx = line.find('|');
        if (idx != std::string::npos) {
            int num1 = std::stoi(line.substr(0, idx));
            int num2 = std::stoi(line.substr(idx + 1, line.size() - idx - 1));
            if (pageOrders.count(num1) == 0)
                pageOrders.insert({num1, {}});
            pageOrders[num1].push_back(num2);
        } else {
            std::stringstream sstream{line};
            std::string val;
            std::vector<int> vals{};
            while (std::getline(sstream, val, ',')) {
                vals.push_back(std::stoi(val));
            }
            updates.push_back(vals);
        }
    }
}

void part1(const std::map<int, std::vector<int>> &pageOrders, const std::vector<std::vector<int>> &updates) {
    int middleSum{0};

    for (auto vec : updates) {
        size_t middleId = vec.size() / 2;

        bool isCorrect = true;
        for (int i{0}; i != vec.size(); ++i) {
            if (!isCorrect) break;
            int val = vec[i];
            // Check every page before it
            for (int j{0}; j != i; ++j) {
                if (pageOrders.count(val) == 0) continue;  // Check for rule
                auto it = std::find(pageOrders.at(val).begin(), pageOrders.at(val).end(), vec[j]);
                if (it == pageOrders.at(val).end()) {  // Page not in this rule
                    continue;
                } else {
                    isCorrect = false;
                    break;
                }
            }
        }

        if (isCorrect) middleSum += vec[middleId];
    }

    std::cout << "Part 1: " << middleSum << std::endl;
}

void part2(const std::map<int, std::vector<int>> &pageOrders, const std::vector<std::vector<int>> &updates) {
    int middleSum{0};

    for (auto vec : updates) {
        size_t middleId = vec.size() / 2;

        bool isCorrect = true;
        for (int i{0}; i != vec.size(); ++i) {
            if (!isCorrect) break;
            int val = vec[i];
            // Check every page before it
            for (int j{0}; j != i; ++j) {
                if (pageOrders.count(val) == 0) continue;  // Check for rule
                auto it = std::find(pageOrders.at(val).begin(), pageOrders.at(val).end(), vec[j]);
                if (it == pageOrders.at(val).end()) {  // Page not in this rule
                    continue;
                } else {
                    isCorrect = false;
                    break;
                }
            }
        }

        if (!isCorrect) {  // Fix the vector. Needs to be able to handle multiple incorrect updates
            std::vector<int> newOrder = vec;
            while (!isCorrect) {
                bool restart = false;
                for (int i{0}; i != newOrder.size(); ++i) {
                    int val = newOrder[i];
                    for (int j{0}; j != i; ++j) {
                        if (pageOrders.count(val) == 0) continue;  // Check for rule
                        auto it = std::find(pageOrders.at(val).begin(), pageOrders.at(val).end(), newOrder[j]);
                        if (it != pageOrders.at(val).end()) {
                            std::swap(newOrder[i], newOrder[j]);
                            restart = true;
                            break;
                        }
                    }
                    if (restart) break;
                }
                if (!restart) isCorrect = true;
            }
            middleSum += newOrder[middleId];
        }
    }

    std::cout << "Part 1: " << middleSum << std::endl;
}

int main(int argc, char *argv[]) {
    // if (argc != 2) {
    //     std::cout << "Input the path to the input file" << std::endl;
    //     return 0;
    // }

    // std::string input_file = std::string(argv[1]);
    std::string input_file = "../input.txt";
    std::map<int, std::vector<int>> pageOrders{};
    std::vector<std::vector<int>> updates;
    parseData(input_file, pageOrders, updates);

    part1(pageOrders, updates);  // 4957
    part2(pageOrders, updates);

    return 0;
}
