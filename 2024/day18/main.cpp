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

// constexpr size_t MAXR{7};
// constexpr size_t MAXC{7};
// constexpr size_t MAXITER{12};

constexpr size_t MAXR{71};
constexpr size_t MAXC{71};
constexpr size_t MAXITER{1024};

void parseData(const std::string &file, std::vector<std::pair<size_t, size_t>> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        std::stringstream ss{line};
        std::string temp;
        std::getline(ss, temp, ',');
        size_t col = std::stoull(temp);
        std::getline(ss, temp, ',');
        size_t row = std::stoull(temp);
        data.emplace_back(row, col);
    }
}

void part1(const std::vector<std::pair<size_t, size_t>> &data) {
    std::vector<std::string> grid{};
    for (size_t i{0}; i != MAXR; ++i) {
        std::string temp = "";
        for (size_t j{0}; j != MAXC; ++j)
            temp += '.';
        grid.push_back(temp);
    }

    for (size_t i{0}; i != MAXITER; ++i) {
        auto pair = data[i];
        grid[pair.first][pair.second] = '#';
    }

    // TODO: Track the cost (dist) and switch to a priority queue
    size_t row{0}, col{0}, cost{0};
    std::vector<std::vector<bool>> visited(MAXR, std::vector<bool>(MAXC, false));
    // std::stack<std::pair<size_t, size_t>> stack{};
    std::priority_queue<std::tuple<size_t, size_t, size_t>, std::vector<std::tuple<size_t, size_t, size_t>>, std::greater<std::tuple<size_t, size_t, size_t>>> stack{};
    std::map<std::pair<size_t, size_t>, std::pair<size_t, size_t>> parent{};
    stack.push({0, row, col});
    while (!stack.empty()) {
        auto pair = stack.top();
        stack.pop();
        cost = std::get<0>(pair);
        row = std::get<1>(pair);
        col = std::get<2>(pair);

        if (visited[row][col]) continue;
        visited[row][col] = true;
        grid[row][col] = 'X';

        // for (auto str : grid)
        //     std::cout << str << "\n";
        // std::cout << "============================\n"
        //           << std::endl;

        if (row == MAXR - 1 && col == MAXC - 1)  // Reached the end
            break;

        // Push new nodes onto the stack
        if (row > 0 && !visited[row - 1][col] && grid[row - 1][col] != '#') {
            stack.push({cost + 1, row - 1, col});
            if (parent.count({row - 1, col}) == 0)
                parent.insert({{row - 1, col}, {row, col}});
        }
        if (row < MAXR - 1 && !visited[row + 1][col] && grid[row + 1][col] != '#') {
            stack.push({cost + 1, row + 1, col});
            if (parent.count({row + 1, col}) == 0)
                parent.insert({{row + 1, col}, {row, col}});
        }
        if (col > 0 && !visited[row][col - 1] && grid[row][col - 1] != '#') {
            stack.push({cost + 1, row, col - 1});
            if (parent.count({row, col - 1}) == 0)
                parent.insert({{row, col - 1}, {row, col}});
        }
        if (col < MAXC - 1 && !visited[row][col + 1] && grid[row][col + 1] != '#') {
            stack.push({cost + 1, row, col + 1});
            if (parent.count({row, col + 1}) == 0)
                parent.insert({{row, col + 1}, {row, col}});
        }
    }

    size_t numSteps{0};
    std::pair<size_t, size_t> pair{MAXR - 1, MAXC - 1};
    while (parent.count(pair) != 0) {
        ++numSteps;
        pair = parent[pair];
    }

    // std::cout << "Part 1: " << numSteps << std::endl;
    std::cout << "Part 1: " << cost << std::endl;
}

void part2(const std::vector<std::pair<size_t, size_t>> &data) {
    // Easy way is to brute force it
    // Smater way would be to do a binary search to narrow in on it
    for (size_t i{MAXITER}; i != data.size(); ++i) {
        bool foundBlock = true;
        std::vector<std::string> grid{};
        for (size_t i{0}; i != MAXR; ++i) {
            std::string temp = "";
            for (size_t j{0}; j != MAXC; ++j)
                temp += '.';
            grid.push_back(temp);
        }

        // I know that I can start here
        for (size_t j{0}; j != i + 1; ++j) {
            auto pair = data[j];
            grid[pair.first][pair.second] = '#';
        }

        // std::cout << data[i].first << "," << data[i].second << std::endl;
        // for (auto str : grid)
        //     std::cout << str << "\n";
        // std::cout << "============================\n"
        //           << std::endl;

        size_t row{0}, col{0}, cost{0};
        std::vector<std::vector<bool>> visited(MAXR, std::vector<bool>(MAXC, false));
        // std::stack<std::pair<size_t, size_t>> stack{};
        std::priority_queue<std::tuple<size_t, size_t, size_t>, std::vector<std::tuple<size_t, size_t, size_t>>, std::greater<std::tuple<size_t, size_t, size_t>>> stack{};
        stack.push({0, row, col});
        while (!stack.empty()) {
            auto pair = stack.top();
            stack.pop();
            cost = std::get<0>(pair);
            row = std::get<1>(pair);
            col = std::get<2>(pair);

            if (visited[row][col]) continue;
            visited[row][col] = true;
            grid[row][col] = 'X';

            // for (auto str : grid)
            //     std::cout << str << "\n";
            // std::cout << "============================\n"
            //           << std::endl;

            if (row == MAXR - 1 && col == MAXC - 1) {  // Reached the end
                foundBlock = false;
                break;
            }

            // Push new nodes onto the stack
            if (row > 0 && !visited[row - 1][col] && grid[row - 1][col] != '#') {
                stack.push({cost + 1, row - 1, col});
            }
            if (row < MAXR - 1 && !visited[row + 1][col] && grid[row + 1][col] != '#') {
                stack.push({cost + 1, row + 1, col});
            }
            if (col > 0 && !visited[row][col - 1] && grid[row][col - 1] != '#') {
                stack.push({cost + 1, row, col - 1});
            }
            if (col < MAXC - 1 && !visited[row][col + 1] && grid[row][col + 1] != '#') {
                stack.push({cost + 1, row, col + 1});
            }
        }

        if (foundBlock) {
            std::cout << "Part 2: " << data[i].second << "," << data[i].first << std::endl;
            return;
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<std::pair<size_t, size_t>> data{};
    parseData(input_file, data);

    part1(data);
    part2(data);

    return 0;
}
