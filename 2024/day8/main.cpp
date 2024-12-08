#include <algorithm>
#include <fstream>
#include <iostream>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

void parseData(const std::string &file, std::vector<std::string> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        data.push_back(line);
    }
}

void calcAntiNodeLocations(std::pair<int, int> ant1, std::pair<int, int> ant2, int maxR, int maxC, std::set<std::pair<int, int>> &locs) {
    // Locations need to be x spaces from 1 and 2x spaces from the other
    // Also in line with the 2 antennas

    int rowSlope = static_cast<int>(ant2.first) - static_cast<int>(ant1.first);
    int colSlope = static_cast<int>(ant2.second) - static_cast<int>(ant1.second);

    // At most 2 locations
    int locR1 = ant2.first + rowSlope;
    int locC1 = ant2.second + colSlope;
    // Check if in bounds and double distance
    if (locR1 >= 0 && locC1 >= 0 && locR1 < maxR && locC1 < maxC && locR1 == ant1.first + 2 * rowSlope && locC1 == ant1.second + 2 * colSlope) {
        locs.insert({locR1, locC1});
    }

    int locR2 = ant1.first - rowSlope;
    int locC2 = ant1.second - colSlope;
    if (locR2 >= 0 && locC2 >= 0 && locR2 < maxR && locC2 < maxC && locR2 == ant2.first - 2 * rowSlope && locC2 == ant2.second - 2 * colSlope) {
        locs.insert({locR2, locC2});
    }
}

void part1(const std::vector<std::string> &data) {
    std::map<std::string, std::vector<std::pair<int, int>>> antennas{};  // Different types of antennas

    std::regex regexPattern("[^.#]");  // Anything except . and #
    for (int i{0}; i != data.size(); ++i) {
        auto it = std::sregex_iterator(data[i].begin(), data[i].end(), regexPattern);
        auto end = std::sregex_iterator();
        for (; it != end; ++it) {
            const std::string str = it->str();
            const int col = static_cast<int>(it->position());
            if (antennas.count(str) == 0)
                antennas.insert({str, {}});
            antennas[str].emplace_back(i, col);
        }
    }

    // Identify antinode locations. Must be less than the following and greater than 0
    int maxRows = data.size();
    int maxCols = data[0].size();
    std::set<std::pair<int, int>> anitNodeLocations{};
    for (auto pair : antennas) {
        for (int i{0}; i != pair.second.size() - 1; ++i) {
            for (int j{i + 1}; j != pair.second.size(); ++j) {
                calcAntiNodeLocations(pair.second[i], pair.second[j], maxRows, maxCols, anitNodeLocations);
            }
        }
    }

    std::cout << "Part 1: " << anitNodeLocations.size();
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    // std::string input_file = "../input.txt";
    std::vector<std::string> data{};
    parseData(input_file, data);

    part1(data);

    return 0;
}
