#include <fstream>
#include <iostream>
#include <map>
#include <regex>
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

// spcial case where it is just a line??
bool isLoopPossible(std::vector<std::string> data, int direction, size_t rowId, size_t colId, std::pair<size_t, size_t> &obsPos) {
    bool onMap = true;
    int origDirection = direction;
    size_t target;
    int targetDirection;  // Need to be facing the right way also
    if (origDirection == 0 || origDirection == 2) {
        target = colId;  // targeting original column
        targetDirection = origDirection - 1;
    } else {
        target = rowId;  // targeting original row
        targetDirection = origDirection - 1;
    }
    if (targetDirection < 0) targetDirection += 4;

    while (onMap) {
        onMap = getNextSpot(data, direction, rowId, colId);

        if (origDirection == 0 || origDirection == 2) {
            if (colId == target && direction == targetDirection) {
                // TODO: Set the obstacle position. Call getNextSpot
                getNextSpot(data, direction, rowId, colId);
                obsPos = std::make_pair(rowId, colId);
                return true;
            }
        } else {
            if (rowId == target && direction == targetDirection) {
                // TODO: Set the obstacle position. Call getNextSpot
                getNextSpot(data, direction, rowId, colId);
                obsPos = std::make_pair(rowId, colId);
                return true;
            }
        }

        // displayMap(data);
    }

    return false;
}

void part2(std::vector<std::string> data) {
    int numPositions{0};

    // Travel along the path
    // For each obstacle he encounters: need previous direction
    // Determine if a loop is possible (i.e. he will get to the same column on a different row)
    // If so increment the counter and continue

    // FInd starting position
    size_t rowId, colId;
    for (int i{0}; i != data.size(); ++i) {
        size_t idx = data[i].find('^');
        if (idx != std::string::npos) {
            rowId = i;
            colId = idx;
        }
    }

    std::vector<std::pair<size_t, size_t>> newObstacles{};  // DO I need direction also?
    int direction = 0;                                      // 1 is North, 2 is East, 3 is South, 4 is West
    bool onMap = true;
    while (onMap) {
        size_t nextRowId = rowId;
        size_t nextColId = colId;
        int nextDirection = direction;
        onMap = getNextSpot(data, nextDirection, nextRowId, nextColId);

        std::pair<size_t, size_t> obsPos = std::make_pair(0, 0);
        if (nextDirection != direction) {
            if (isLoopPossible(data, direction, rowId, colId, obsPos)) {
                if (std::find(newObstacles.begin(), newObstacles.end(), obsPos) == newObstacles.end()) {
                    ++numPositions;
                    newObstacles.emplace_back(obsPos);
                }
            }
            // Check if  aloop is possible
            // i.e. do I get back to the current row/col depending on direction
            // if yex, then place an obstacle on the next square
        }

        rowId = nextRowId;
        colId = nextColId;
        direction = nextDirection;

        if (onMap) {
            // if (data[rowId][colId] == '.') {
            //     numPositions += 1;
            // }
            data[rowId][colId] = 'X';
        }
        displayMap(data);
    }

    std::cout << "Part 2: " << numPositions << std::endl;
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

    part1(data);  // 4977
    // part2(data);

    return 0;
}
