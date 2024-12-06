#include <fstream>
#include <iostream>
#include <map>
#include <regex>
#include <sstream>
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

void displayMap(const std::vector<std::string> &data) {
    for (std::string line : data) {
        std::cout << line << std::endl;
    }
    std::cout << "============================================\n"
              << std::endl;
}

bool getNextSpot(std::vector<std::string> &data, int &direction, size_t &rowId, size_t &colId) {
    int rowDiff{0}, colDiff{0};
    if (direction == 0) {  // North
        rowDiff = -1;
    } else if (direction == 1) {  // East
        colDiff = 1;
    } else if (direction == 2) {  // South
        rowDiff = 1;
    } else {  // West
        colDiff = -1;
    }

    // Left the map
    if (rowId + rowDiff < 0 || rowId + rowDiff >= data.size() || colId + colDiff < 0 || colId + colDiff >= data[0].size()) {
        rowId += rowDiff;
        colId += colDiff;
        return false;
    }

    // Need to turn: Handle case where turning into an obstacle
    auto temp = data[rowId + rowDiff][colId + colDiff];
    while (data[rowId + rowDiff][colId + colDiff] == '#') {
        direction = (direction + 1) % 4;
        rowDiff = 0;
        colDiff = 0;
        if (direction == 0) {  // North
            rowDiff = -1;
        } else if (direction == 1) {  // East
            colDiff = 1;
        } else if (direction == 2) {  // South
            rowDiff = 1;
        } else {  // West
            colDiff = -1;
        }
    }
    rowId += rowDiff;
    colId += colDiff;

    // Left the map
    if (rowId < 0 || rowId >= data.size() || colId < 0 || colId >= data[0].size())
        return false;

    return true;
}

void part1(std::vector<std::string> data) {
    int numPositions{1};  // For starting position

    // FInd starting position
    size_t rowId, colId;
    for (int i{0}; i != data.size(); ++i) {
        size_t idx = data[i].find('^');
        if (idx != std::string::npos) {
            rowId = i;
            colId = idx;
        }
    }

    int direction = 0;  // 1 is North, 2 is East, 3 is South, 4 is West
    bool onMap = true;
    while (onMap) {
        onMap = getNextSpot(data, direction, rowId, colId);

        if (onMap) {
            if (data[rowId][colId] == '.') {
                numPositions += 1;
            }
            data[rowId][colId] = 'X';
        }
        // displayMap(data);
    }

    std::cout << "Part 1: " << numPositions << std::endl;
}

int main(int argc, char *argv[]) {
    // if (argc != 2) {
    //     std::cout << "Input the path to the input file" << std::endl;
    //     return 0;
    // }

    // std::string input_file = std::string(argv[1]);
    std::string input_file = "../input.txt";
    std::vector<std::string> data{};
    parseData(input_file, data);

    part1(data);

    return 0;
}
