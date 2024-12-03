#include <algorithm>
#include <fstream>
#include <iostream>
#include <regex>
#include <string>
#include <vector>

void parseData(const std::string &file, std::vector<std::string> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        data.push_back(line);
    }
}

void part1(const std::vector<std::string> &data) {
    int sum{0};
    std::regex regexPattern("mul\(\d{1,3},\d{1,3}\)");

    for (std::string line : data) {
        auto it = std::sregex_iterator(line.begin(), line.end(), regexPattern);
        auto end = std::sregex_iterator();
        for (; it != end; ++it) {
            std::string str = it->str();

            std::cout << str << std::endl;

            // size_t commaId = str.find(',');
            // const size_t firstDigitId = 5;
            // const size_t lastDigitId = str.size() - 1;

            // int num1 = std::stoi(str.substr(firstDigitId, commaId - firstDigitId));
            // int num2 = std::stoi(str.substr(commaId + 1, lastDigitId - commaId));
            // sum += num1 * num2;
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<std::string> data;
    parseData(input_file, data);

    part1(data);  // 359

    return 0;
}
