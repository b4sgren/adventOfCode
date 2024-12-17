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

int64_t RegA = 0;
int64_t RegB = 0;
int64_t RegC = 0;

void parseData(const std::string &file, std::vector<int64_t> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    std::getline(fin, line);
    size_t idx = line.find(':');
    RegA = std::stoll(line.substr(idx + 2));

    std::getline(fin, line);
    idx = line.find(':');
    RegB = std::stoll(line.substr(idx + 2));

    std::getline(fin, line);
    idx = line.find(':');
    RegC = std::stoll(line.substr(idx + 2));

    std::getline(fin, line);
    std::getline(fin, line);
    idx = line.find(':');
    std::stringstream ss{line.substr(idx + 2)};
    while (std::getline(ss, line, ',')) {
        if (line.empty()) break;
        data.push_back(std::stoll(line));
    }
}

int64_t getCombo(const int64_t &operand) {
    if (operand <= 3) {
        return operand;
    } else if (operand == 4) {
        return RegA;
    } else if (operand == 5) {
        return RegB;
    } else if (operand == 6) {
        return RegC;
    } else {
        return -1;
    }
}

void part1(const std::vector<int64_t> &data) {
    std::string temp_output{""};
    for (int64_t i{0}; i < data.size(); i += 2) {
        if (i + 1 >= data.size()) break;
        const int64_t instruction = data[i];
        const int64_t operand = data[i + 1];

        switch (instruction) {
            case 0: {
                const int64_t num = RegA;
                const int64_t den = pow(2, getCombo(operand));
                RegA = num / den;
                break;
            }
            case 1: {
                RegB = RegB ^ operand;
                break;
            }
            case 2: {
                RegB = getCombo(operand) % 8;
                break;
            }
            case 3: {
                if (RegA != 0) {
                    i = operand - 2;
                }
                break;
            }
            case 4: {
                RegB = RegB ^ RegC;
                break;
            }
            case 5: {
                const int64_t val = getCombo(operand) % 8;
                temp_output += std::to_string(val);
                break;
            }
            case 6: {
                const int64_t num = RegA;
                const int64_t den = pow(2, getCombo(operand));
                RegB = num / den;
                break;
            }
            case 7: {
                const int64_t num = RegA;
                const int64_t den = pow(2, getCombo(operand));
                RegC = num / den;
                break;
            }
        }
    }

    std::string output{""};
    for (char c : temp_output) {
        output += c;
        output += ",";
    }

    std::cout << "Part 1: " << output << std::endl;
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
