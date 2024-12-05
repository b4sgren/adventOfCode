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
    std::regex regexPattern("mul\\(\\d{1,3},\\d{1,3}\\)");

    for (std::string line : data) {
        auto it = std::sregex_iterator(line.begin(), line.end(), regexPattern);
        auto end = std::sregex_iterator();
        for (; it != end; ++it) {
            std::string str = it->str();

            size_t commaId = str.find(',');
            const size_t firstDigitId = 4;
            const size_t lastDigitId = str.size() - 2;

            int num1 = std::stoi(str.substr(firstDigitId, commaId - firstDigitId));
            int num2 = std::stoi(str.substr(commaId + 1, lastDigitId - commaId));
            sum += num1 * num2;
        }
    }

    std::cout << "Part1: " << sum << std::endl;
}

void part2(const std::vector<std::string> &data) {
    int sum{0};
    std::regex regexPattern("mul\\(\\d{1,3},\\d{1,3}\\)");

    for (std::string line : data) {
        // Find indices of do
        std::regex doPattern("do\\(\\)");
        auto it_do = std::sregex_iterator(line.begin(), line.end(), doPattern);
        std::vector<size_t> do_idx_{0};
        for (; it_do != std::sregex_iterator(); ++it_do)
            do_idx_.push_back(it_do->position());

        // FInd indices of dont
        std::regex dontPattern("don't\\(\\)");
        auto it_dont = std::sregex_iterator(line.begin(), line.end(), dontPattern);
        std::vector<size_t> dont_idx_{};
        for (; it_dont != std::sregex_iterator(); ++it_dont)
            dont_idx_.push_back(it_dont->position());
        dont_idx_.push_back(1e9);  // to make sure there is an end

        // Be sure to handle cases where multiple dos and don'ts appear in a row
        // Remove extra ones here
        auto it1 = do_idx_.begin();
        auto it2 = dont_idx_.begin();
        std::vector<size_t> do_idx{0}, dont_idx{};
        while (it1 != do_idx_.end() && it2 != dont_idx_.end()) {
            while (it2 != dont_idx_.end() && *it2 < do_idx.back()) {
                ++it2;
            }
            if (it2 != dont_idx_.end())
                dont_idx.push_back(*it2);

            while (it1 != do_idx_.end() && *it1 < dont_idx.back()) {
                ++it1;
            }
            if (it1 != do_idx_.end())
                do_idx.push_back(*it1);
        }

        for (int i{0}; i != do_idx.size(); ++i) {
            // Only Search between a do and a don't
            // Make sure I don't go past the end of a line
            int max_offset = dont_idx[i] > line.size() ? line.size() : dont_idx[i];
            auto it = std::sregex_iterator(line.begin() + do_idx[i], line.begin() + max_offset, regexPattern);
            auto end = std::sregex_iterator();

            for (; it != end; ++it) {
                std::string str = it->str();

                size_t commaId = str.find(',');
                const size_t firstDigitId = 4;
                const size_t lastDigitId = str.size() - 2;

                int num1 = std::stoi(str.substr(firstDigitId, commaId - firstDigitId));
                int num2 = std::stoi(str.substr(commaId + 1, lastDigitId - commaId));
                sum += num1 * num2;
            }
        }
    }

    std::cout << "Part2: " << sum << std::endl;
}

int main(int argc, char *argv[]) {
    // if (argc != 2) {
    //     std::cout << "Input the path to the input file" << std::endl;
    //     return 0;
    // }

    // std::string input_file = std::string(argv[1]);
    std::string input_file = "../input.txt";
    std::vector<std::string> data;
    parseData(input_file, data);

    part1(data);  // 161
    part2(data);  // Note: Need to make input all one line haha

    return 0;
}
