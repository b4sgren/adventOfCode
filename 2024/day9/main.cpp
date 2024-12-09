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
    std::string fileString{""};

    for (int i{0}; i != data.size(); ++i) {
        int val = data[i] - '0';

        for (int j{0}; j != val; ++j) {
            if (i % 2 == 0) {
                fileString += std::to_string(fileId);
            } else {  // Free space
                fileString += '.';
            }
        }

        // Increment even if this field in 0 in data??
        if (i % 2 == 0) ++fileId;
    }

    // Sort string so free space is at the end
    int front{0}, back{fileString.size() - 1};
    while (front < back) {
        if (fileString[front] == '.') {
            std::swap(fileString[front], fileString[back]);
            --back;
            while (fileString[back] == '.')
                --back;
        }
        ++front;
    }

    // Compute checksum
    size_t checksum{0};
    for (size_t i{0}; i != fileString.size(); ++i) {
        if (fileString[i] == '.')
            break;
        int val = fileString[i] - '0';

        checksum += i * static_cast<size_t>(val);
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

    part1(data);  // 89403351449 is to low

    return 0;
}
