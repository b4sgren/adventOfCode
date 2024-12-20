#include <algorithm>
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

void moveRobot2(std::vector<std::string> &map, size_t &row, size_t &col, char direction) {
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

    // Edits
    //  Shift the whole string not just the last bit
    //  Special case for vertical moving. Possibly need to check lots of columns
    //    @
    //   []
    //  [][]
    // [][][]
    //[]    []
    //            Can move (unless one is blocked by a wall)

    // Determine if a move is possible
    size_t counterR{row}, counterC{col};
    std::vector<std::string> mapCopy = map;
    while (map[counterR][counterC] != '#') {
        counterR += rowDir;
        counterC += colDir;
        if (direction == '<' || direction == '>') {
            if (map[counterR][counterC] == '.') {
                // Shift boxes
                while (counterC != col) {
                    mapCopy[counterR][counterC] = map[counterR - rowDir][counterC - colDir];
                    counterR -= rowDir;
                    counterC -= colDir;
                }
                mapCopy[row][col] = '.';
                row = nextR;
                col = nextC;
                map = mapCopy;
                return;
            }
        } else {
            // Special checks for vertical
            std::queue<std::pair<size_t, size_t>> queue{};
            queue.push({counterR, counterC});
            mapCopy[counterR][counterC] = '.';
            if (map[counterR][counterC] == '[') {
                queue.push({counterR, counterC + 1});
                mapCopy[counterR][counterC + 1] = '.';
            } else if (map[counterR][counterC] == ']') {
                queue.push({counterR, counterC - 1});
                mapCopy[counterR][counterC - 1] = '.';
            } else if (map[counterR][counterC] == '.') {
                map[counterR][counterC] = '@';
                map[row][col] = '.';
                row = nextR;
                col = nextC;
                return;
            }

            // I get to a . and i still add nodes
            std::set<std::pair<size_t, size_t>> visited{};
            while (!queue.empty()) {
                auto pair = queue.front();
                queue.pop();
                size_t r{pair.first}, c{pair.second};
                if (map[r + rowDir][c] == '#') {
                    return;
                }

                if (visited.count(pair)) continue;
                visited.insert(pair);

                queue.push({r + rowDir, c});
                // Add the partner block
                if (map[r + rowDir][c] == '[' && visited.count({r + rowDir, c + 1}) == 0)
                    queue.push({row + rowDir, c + 1});
                else if (map[r + rowDir][c] == ']' && visited.count({r + rowDir, c - 1}) == 0)
                    queue.push({row + rowDir, c - 1});

                // Shift on the copy map
                mapCopy[r + rowDir][c] = map[r][c];
            }

            map = mapCopy;
            return;
        }
    }
    map[nextR, nextC] = '@';
    map[row, col] = '.';
}

void part2(std::vector<std::string> map, const std::string &directions) {
    // Update the map
    std::vector<std::string> newMap{};
    for (std::string str : map) {
        std::string temp{""};
        for (char c : str) {
            if (c == '#' || c == '.') {
                temp += c;
                temp += c;
            } else if (c == '@') {
                temp += c;
                temp += ".";
            } else {
                temp += "[]";
            }
        }
        newMap.push_back(temp);
    }

    // FInd starting point
    size_t row, col;
    for (size_t i{0}; i != newMap.size(); ++i) {
        size_t pos = newMap[i].find('@');
        if (pos != std::string::npos) {
            row = i;
            col = pos;
        }
    }

    for (std::string str : newMap)
        std::cout << str << std::endl;
    std::cout << "==========================\n";

    for (char dir : directions) {
        moveRobot2(newMap, row, col, dir);
        std::cout << dir << std::endl;
        for (std::string str : newMap)
            std::cout << str << std::endl;
        std::cout << "==========================\n";
    }

    size_t sum{0};
    for (size_t i{0}; i != newMap.size(); ++i) {
        for (size_t j{0}; j != map[i].size(); ++j) {
            if (map[i][j] == 'O')
                sum += 100 * i + j;
        }
    }

    std::cout << "Part 2: " << sum << std::endl;
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
    part2(data, directions);

    return 0;
}
