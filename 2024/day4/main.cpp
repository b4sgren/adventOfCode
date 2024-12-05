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

bool searchHorizontal(const std::string &line, size_t start, int dir) {
    if (start + dir * 3 >= line.size() || start + dir * 3 < 0)  // Not enough space
        return false;

    if (line[start] == 'X' && line[start + dir] == 'M' && line[start + dir * 2] == 'A' && line[start + dir * 3] == 'S')
        return true;

    return false;
}

bool searchVertical(const std::vector<std::string> &data, size_t startV, size_t horizId, int dir) {
    if (startV + dir * 3 >= data.size() || startV + dir * 3 < 0)  // Not enough space
        return false;

    if (data[startV][horizId] == 'X' && data[startV + dir][horizId] == 'M' && data[startV + dir * 2][horizId] == 'A' && data[startV + dir * 3][horizId] == 'S')
        return true;

    return false;
}

bool searchDiag(const std::vector<std::string> &data, size_t startV, size_t startH, int dirV, int dirH) {
    if (startV + dirV * 3 >= data.size() || startV + dirV * 3 < 0 || startH + dirH * 3 >= data[0].size() || startH + dirH * 3 < 0)  // Not enough space
        return false;

    if (data[startV][startH] == 'X' && data[startV + dirV][startH + dirH] == 'M' && data[startV + dirV * 2][startH + dirH * 2] == 'A' && data[startV + dirV * 3][startH + dirH * 3] == 'S')
        return true;

    return false;
}

void part1(const std::vector<std::string> &data) {
    int count{0};
    std::regex regexPattern("X");

    for (size_t i{0}; i != data.size(); ++i) {
        std::string line = data[i];
        // Search for all instances of X then begin searches
        auto it = std::sregex_iterator(line.begin(), line.end(), regexPattern);
        auto end = std::sregex_iterator();
        for (; it != end; ++it) {
            size_t idx = it->position();
            if (searchHorizontal(line, idx, 1)) ++count;
            if (searchHorizontal(line, idx, -1)) ++count;
            if (searchVertical(data, i, idx, 1)) ++count;
            if (searchVertical(data, i, idx, -1)) ++count;
            if (searchDiag(data, i, idx, 1, 1)) ++count;
            if (searchDiag(data, i, idx, 1, -1)) ++count;
            if (searchDiag(data, i, idx, -1, 1)) ++count;
            if (searchDiag(data, i, idx, -1, -1)) ++count;
        }
    }

    std::cout << "Part1: " << count << std::endl;
}

bool search(const std::vector<std::string> &data, size_t startV, size_t startH, std::pair<int, int> dirM1, std::pair<int, int> dirM2) {
    if (startV + 1 >= data.size() || startV - 1 < 0 || startH + 1 >= data[0].size() || startH - 1 < 0)  // Not enough space
        return false;

    if (data[startV][startH] == 'A' && data[startV + dirM1.second][startH + dirM1.first] == 'M' && data[startV - dirM1.second][startH - dirM1.first] == 'S' && data[startV + dirM2.second][startH + dirM2.first] == 'M' && data[startV - dirM2.second][startH - dirM2.first] == 'S')
        return true;

    return false;
}

void part2(const std::vector<std::string> &data) {
    int count{0};
    // Search for 'A' and then look for the cross
    std::regex regexPattern("A");

    for (size_t i{1}; i != data.size() - 1; ++i) {
        std::string line = data[i];
        // Search for all instances of X then begin searches
        auto it = std::sregex_iterator(line.begin(), line.end(), regexPattern);
        auto end = std::sregex_iterator();
        for (; it != end; ++it) {
            size_t idx = it->position();
            // Max in an X Shape
            // Pairs are horizontal steps, vertical steps
            if (search(data, i, idx, std::make_pair(-1, -1), std::make_pair(-1, 1))) ++count;
            if (search(data, i, idx, std::make_pair(-1, -1), std::make_pair(1, -1))) ++count;
            if (search(data, i, idx, std::make_pair(1, -1), std::make_pair(1, 1))) ++count;
            if (search(data, i, idx, std::make_pair(1, 1), std::make_pair(-1, 1))) ++count;
            // // Max in an + Shape
            // if (search(data, i, idx, std::make_pair(-1, 0), std::make_pair(0, -1))) ++count;
            // if (search(data, i, idx, std::make_pair(-1, 0), std::make_pair(0, 1))) ++count;
            // if (search(data, i, idx, std::make_pair(1, 0), std::make_pair(0, -1))) ++count;
            // if (search(data, i, idx, std::make_pair(1, 0), std::make_pair(0, 1))) ++count;
        }
    }

    std::cout << "Part2: " << count << std::endl;
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

    part1(data);  // 2718
    part2(data);  // 2074 is to high

    return 0;
}
