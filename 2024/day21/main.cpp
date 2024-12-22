#include <algorithm>
#include <cmath>
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

// If a path takes me onto a ' ' key, switch that direction with the one after it
// Need the least turns

class NumericKeypad {
   public:
    NumericKeypad() : keypad_{}, row_{3}, col_{2} {
        std::vector<char> row1{'7', '8', '9'};
        std::vector<char> row2{'4', '5', '6'};
        std::vector<char> row3{'1', '2', '3'};
        std::vector<char> row4{' ', '0', 'A'};

        keypad_.push_back(row1);
        keypad_.push_back(row2);
        keypad_.push_back(row3);
        keypad_.push_back(row4);
    }

    std::vector<std::vector<char>> getMapping(char target) {
        char currentKey = keypad_[row_][col_];

        // Find target row/col
        int targetR{0}, targetC{0};
        for (; targetR != keypad_.size(); ++targetR) {
            targetC = 0;
            for (; targetC != keypad_[0].size(); ++targetC)
                if (target == keypad_[targetR][targetC]) {
                    auto vec = generateMappings(targetR, targetC);
                    row_ = targetR;
                    col_ = targetC;
                    return vec;
                }
        }

        std::cout << "ERROR: SHOULDN'T GET HERE" << std::endl;
        return std::vector<std::vector<char>>{};
    }

   private:
    std::vector<std::vector<char>> keypad_;
    int row_;
    int col_;

    std::vector<std::vector<char>> generateMappings(int targetR, int targetC) {
        // Need to make sure that I do not pass through the empty keyspace
        int deltaR{targetR}, deltaC{targetC};

        // Special case
        if ((row_ == 3 && targetC == 0) || (col_ == 0 && targetR == 3)) {
            if (row_ == 3) {
                // up then over
                int dir{sign(deltaR)};
                char symbol = dir >= 0 ? 'v' : '^';
                std::vector<char> vec1(abs(deltaR), symbol);

                dir = sign(deltaC);
                symbol = dir >= 0 ? '>' : '<';
                for (int i{0}; i != deltaC; i += dir) {
                    vec1.push_back(symbol);
                }
                vec1.push_back('A');

                return std::vector<std::vector<char>>{vec1};

            } else if (col_ == 0) {
                // over then down
                int dir{sign(deltaC)};
                char symbol = dir >= 0 ? '>' : '<';
                std::vector<char> vec1(abs(deltaC), symbol);

                dir = sign(deltaR);
                symbol = dir >= 0 ? 'v' : '^';
                for (int i{0}; i != deltaR; i += dir) {
                    vec1.push_back(symbol);
                }
                vec1.push_back('A');

                return std::vector<std::vector<char>>{vec1};

            } else {
                std::cout << "NUM MAPPING ERROR: SHOULDNT GET HERE" << std::endl;
                return std::vector<std::vector<char>>{};
            }
        } else {
            // 2 cases (2 edges of the rectangle)
            int dir{sign(deltaR)};
            char symbol = dir >= 0 ? 'v' : '^';
            std::vector<char> vec1(abs(deltaR), symbol);

            dir = sign(deltaC);
            symbol = dir >= 0 ? '>' : '<';
            std::vector<char> vec2{};
            for (int i{0}; i != deltaC; i += dir) {
                vec1.push_back(symbol);
                vec2.push_back(symbol);
            }

            dir = sign(deltaR);
            symbol = dir >= 0 ? 'v' : '^';
            for (int i{0}; i != deltaR; i += dir)
                vec2.push_back(symbol);
            vec1.push_back('A');
            vec2.push_back('A');

            return std::vector<std::vector<char>>{vec1, vec2};
        }
    }

    int sign(int val) {
        if (val >= 0)
            return 1;
        else
            return -1;
    }
};

class DirectionKeypad {
   public:
    DirectionKeypad() : keypad_{}, row_{0}, col_{2} {
        std::vector<char> row1{' ', '^', 'A'};
        std::vector<char> row2{'<', 'v', '>'};

        keypad_.push_back(row1);
        keypad_.push_back(row2);

        generateMappings();
    }

    std::vector<std::vector<char>> generateMappings(const std::vector<std::vector<char>> &routes) {
        // Analyze the number of turns to pick the best one
        // Which routes require the least turns
        std::map<int, std::vector<int>> bestRoutes{};
        char prevKey;
        int idx{0}, minTurns{100000};
        for (auto route : routes) {
            prevKey = 'A';
            int numTurns{0};
            for (char dir : route) {
                numTurns += mappings[{prevKey, dir}];
                prevKey = dir;
            }
            bestRoutes[numTurns].push_back(idx);
            if (numTurns < minTurns)
                minTurns = numTurns;

            ++idx;
        }

        // Get the routes for the robot
        std::vector<std::vector<char>> nextRoutes{};
        for (int id : bestRoutes[minTurns]) {
            char prevKey = 'A';
            std::vector<char> temp{};
            for (char dir : routes[id]) {
                if ((dir == '<' && (prevKey == 'A' || prevKey == '^')) || (prevKey == '<' && (dir == '^' || dir == 'A'))) {
                    // One route
                } else {
                    int targetR{0}, targetC{0};
                    for (; targetR != keypad_.size(); ++targetR) {
                        targetC = 0;
                        for (; targetC != keypad_[0].size(); ++targetC)
                            if (dir == keypad_[targetR][targetC]) {
                                auto vec = generateMappings(targetR, targetC);
                                // std::move(vec.begin(), vec.end())
                                row_ = targetR;
                                col_ = targetC;
                            }
                    }
                }
            }
        }
        return nextRoutes;
    }

   private:
    std::vector<std::vector<char>> keypad_;
    std::map<std::pair<char, char>, int> mappings{};
    int row_;
    int col_;

    void generateMappings() {
        mappings[{'A', 'A'}] = 0;
        mappings[{'A', '^'}] = 1;
        mappings[{'A', '>'}] = 1;
        mappings[{'A', 'v'}] = 2;
        mappings[{'A', '<'}] = 2;

        mappings[{'^', 'A'}] = 1;
        mappings[{'^', '^'}] = 0;
        mappings[{'^', '>'}] = 2;
        mappings[{'^', 'v'}] = 1;
        mappings[{'^', '<'}] = 2;

        mappings[{'>', 'A'}] = 1;
        mappings[{'>', '^'}] = 2;
        mappings[{'>', '>'}] = 0;
        mappings[{'>', 'v'}] = 1;
        mappings[{'>', '<'}] = 1;

        mappings[{'v', 'A'}] = 2;
        mappings[{'v', '^'}] = 1;
        mappings[{'v', '>'}] = 1;
        mappings[{'v', 'v'}] = 0;
        mappings[{'v', '<'}] = 1;

        mappings[{'<', 'A'}] = 2;
        mappings[{'<', '^'}] = 2;
        mappings[{'<', '>'}] = 1;
        mappings[{'<', 'v'}] = 1;
        mappings[{'<', '<'}] = 0;
    }
};

void parseData(const std::string &file, std::vector<std::string> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        data.push_back(line);
    }
}

void part1(const std::vector<std::string> &data) {
    NumericKeypad numKeypad;
    DirectionKeypad dirKeypad1;
    DirectionKeypad dirKeypad2;
    DirectionKeypad dirKeypad3;

    int64_t complexity{0};
    for (std::string code : data) {
        std::vector<char> keyPresses{};
        for (char c : code) {
            std::vector<char> vec = numKeypad.getMapping(c);
            for (char c2 : vec) {
                auto vec2 = dirKeypad1.getMapping(c2);
                for (char c3 : vec2) {
                    auto vec3 = dirKeypad2.getMapping(c3);
                    std::move(vec3.begin(), vec3.end(), std::back_inserter(keyPresses));
                }
            }
        }
        std::cout << code << " " << keyPresses.size() << ": ";
        for (char c : keyPresses)
            std::cout << c;
        std::cout << std::endl;
        complexity += std::stoi(code.substr(0, 3)) * keyPresses.size();
    }

    std::cout << "Part 1: " << complexity << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<std::string> data{};
    parseData(input_file, data);

    part1(data);  // 153516  is to low, 159436 is to high. Paths need to be dynamic...

    return 0;
}
