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

        // getMappings();
    }

    std::vector<char> getMapping(char target) {
        char currentKey = keypad_[row_][col_];

        // Find target row/col
        int targetR{0}, targetC{0};
        for (; targetR != keypad_.size(); ++targetR) {
            targetC = 0;
            for (; targetC != keypad_[0].size(); ++targetC)
                if (target == keypad_[targetR][targetC]) {
                    row_ = targetR;
                    col_ = targetC;
                    return mappings[{currentKey, keypad_[targetR][targetC]}];
                }
        }

        std::cout << "ERROR: SHOULDN'T GET HERE" << std::endl;
        return std::vector<char>{};
    }

   private:
    std::vector<std::vector<char>> keypad_;
    std::map<std::pair<char, char>, std::vector<char>> mappings{};
    int row_;
    int col_;

    // This path may travel through the blank space. Can just switch the offending step with the following step to fix
    void getMappings() {
        for (int i{0}; i != keypad_.size(); ++i) {
            for (int j{0}; j != keypad_[0].size(); ++j) {
                if (keypad_[i][j] == ' ') continue;

                for (int m{0}; m != keypad_.size(); ++m) {
                    for (int n{0}; n != keypad_[0].size(); ++n) {
                        if (keypad_[m][n] == ' ') continue;

                        const int rowDist = m - i;
                        const int colDist = n - j;

                        std::vector<char> temp{};
                        if (i != 3) {
                            int dir = sign(colDist);
                            for (int cnt{0}; cnt != colDist; cnt += dir) {
                                if (colDist > 0)
                                    temp.push_back('>');
                                else
                                    temp.push_back('<');
                            }

                            dir = sign(rowDist);
                            for (int cnt{0}; cnt != rowDist; cnt += dir) {
                                if (rowDist > 0)
                                    temp.push_back('v');
                                else
                                    temp.push_back('^');
                            }

                        } else {  // j == 0 : i.e. first col so move sideways first
                            int dir = sign(rowDist);
                            for (int cnt{0}; cnt != rowDist; cnt += dir) {
                                if (rowDist > 0)
                                    temp.push_back('v');
                                else
                                    temp.push_back('^');
                            }

                            dir = sign(colDist);
                            for (int cnt{0}; cnt != colDist; cnt += dir) {
                                if (colDist > 0)
                                    temp.push_back('>');
                                else
                                    temp.push_back('<');
                            }
                        }
                        temp.push_back('A');

                        mappings[{keypad_[i][j], keypad_[m][n]}] = temp;
                    }
                }
            }
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

        getMappings();
    }

    // find the target and update the position
    std::vector<char> getMapping(char target) {
        char currentKey = keypad_[row_][col_];

        // Find target row/col
        int targetR{0}, targetC{0};
        for (; targetR != keypad_.size(); ++targetR) {
            targetC = 0;
            for (; targetC != keypad_[0].size(); ++targetC)
                if (target == keypad_[targetR][targetC]) {
                    row_ = targetR;
                    col_ = targetC;
                    return mappings[{currentKey, keypad_[targetR][targetC]}];
                }
        }

        std::cout << "ERROR: SHOULDN'T GET HERE" << std::endl;
        return std::vector<char>{};
    }

   private:
    std::vector<std::vector<char>> keypad_;
    std::map<std::pair<char, char>, std::vector<char>> mappings{};
    int row_;
    int col_;

    void getMappings() {
        mappings[{'^', '^'}] = std::vector<char>{'A'};
        mappings[{'^', 'A'}] = std::vector<char>{'>', 'A'};
        mappings[{'^', '>'}] = std::vector<char>{'v', '>', 'A'};
        mappings[{'^', 'v'}] = std::vector<char>{'v', 'A'};
        mappings[{'^', '<'}] = std::vector<char>{'v', '<', 'A'};

        mappings[{'A', 'A'}] = std::vector<char>{'A'};
        mappings[{'A', '^'}] = std::vector<char>{'<', 'A'};
        mappings[{'A', '>'}] = std::vector<char>{'v', 'A'};
        mappings[{'A', 'v'}] = std::vector<char>{'v', '<', 'A'};
        mappings[{'A', '<'}] = std::vector<char>{'v', '<', '<', 'A'};

        mappings[{'>', 'A'}] = std::vector<char>{'^', 'A'};
        mappings[{'>', '^'}] = std::vector<char>{'<', '^', 'A'};
        mappings[{'>', '>'}] = std::vector<char>{'A'};
        mappings[{'>', 'v'}] = std::vector<char>{'<', 'A'};
        mappings[{'>', '<'}] = std::vector<char>{'<', '<', 'A'};

        mappings[{'v', 'A'}] = std::vector<char>{'^', '>', 'A'};
        mappings[{'v', '^'}] = std::vector<char>{'^', 'A'};
        mappings[{'v', '>'}] = std::vector<char>{'>', 'A'};
        mappings[{'v', 'v'}] = std::vector<char>{'A'};
        mappings[{'v', '<'}] = std::vector<char>{'<', 'A'};

        mappings[{'<', 'A'}] = std::vector<char>{'>', '>', '^', 'A'};
        mappings[{'<', '^'}] = std::vector<char>{'>', '^', 'A'};
        mappings[{'<', '>'}] = std::vector<char>{'>', '>', 'A'};
        mappings[{'<', 'v'}] = std::vector<char>{'>', 'A'};
        mappings[{'<', '<'}] = std::vector<char>{'A'};
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
