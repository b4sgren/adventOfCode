#include <algorithm>
#include <fstream>
#include <iostream>
#include <regex>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <vector>

void parseData(const std::string &file, std::vector<std::string> &map, std::string &directions) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        if (line.empty()) break;
        map.push_back(line);
    }
    std::getline(fin, directions);
}

void moveRobot(std::vector<std::string> &map, size_t &row, size_t &col, char direction) {
    size_t nextR{row}, nextC{col};
    int rowDir{0}, colDir{0};
    switch (direction) {
        case '^':
            rowDir = -1;
            break;
        case 'v':
            rowDir = 1;
            break;
        case '>':
            colDir = 1;
            break;
        case '<':
            colDir = -1;
            break;
    }

    nextR += rowDir;
    nextC += colDir;

    // Determine if a move is possible
    bool canMove = false;
    size_t counterR{row}, counterC{col};
    while (map[counterR][counterC] != '#') {
        counterR += rowDir;
        counterC += colDir;
        if (map[counterR][counterC] == '.') {
            // Shift stuff and return
            map[counterR][counterC] = map[counterR - rowDir][counterC - colDir];
            map[nextR][nextC] = '@';
            map[row][col] = '.';
            row = nextR;
            col = nextC;
            return;
        }
    }
}

void part1(std::vector<std::string> map, const std::string &directions) {
    // Find robot place
    size_t row, col;
    for (size_t i{0}; i != map.size(); ++i) {
        size_t pos = map[i].find('@');
        if (pos != std::string::npos) {
            row = i;
            col = pos;
        }
    }

    for (char dir : directions) {
        moveRobot(map, row, col, dir);
        std::cout << dir << std::endl;
        for (std::string str : map)
            std::cout << str << std::endl;
        std::cout << "==========================\n";
    }

    size_t sum{0};
    for (size_t i{0}; i != map.size(); ++i) {
        for (size_t j{0}; j != map[i].size(); ++j) {
            if (map[i][j] == 'O')
                sum += 100 * i + j;
        }
    }

    std::cout << "Part 1: " << sum << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<std::string> data{};
    std::string directions{""};
    parseData(input_file, data, directions);

    part1(data, directions);

    return 0;
}
