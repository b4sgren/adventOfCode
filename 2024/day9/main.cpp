#include <algorithm>
#include <fstream>
#include <iostream>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

void parseData(const std::string &file, std::string &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        data = line;
    }
}

void part1(std::string data) {
    int fileId{0};

    std::vector<std::string> fileString{};
    for (int i{0}; i != data.size(); ++i) {
        int val = data[i] - '0';

        for (int j{0}; j != val; ++j) {
            if (i % 2 == 0) {
                fileString.push_back(std::to_string(fileId));
            } else {  // Free space
                fileString.push_back(".");
            }
        }

        // Increment even if this field in 0 in data??
        if (i % 2 == 0) ++fileId;
    }

    // Sort string so free space is at the end
    size_t front{0}, back{fileString.size() - 1};
    // Front and back no longer point to the correct spot...
    while (front < back) {
        if (fileString[front] == ".") {
            std::swap(fileString[front], fileString[back]);
            while (fileString[back] == ".")
                --back;
        }
        ++front;
    }

    for (std::string str : fileString)
        std::cout << str;
    std::cout << std::endl;

    // Compute checksum
    uint64_t checksum{0};
    for (uint64_t i{0}; i != fileString.size(); ++i) {
        if (fileString[i] == ".") continue;
        checksum += i * std::atoll(fileString[i].c_str());
    }

    std::cout << "Part 1: " << checksum << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    // std::string input_file = "../input.txt";
    std::string data{};
    parseData(input_file, data);

    part1(data);  // 89403351449 is to low, 2921528924398 is to low
    6258319840548

        return 0;
}
