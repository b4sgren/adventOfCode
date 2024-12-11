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

void parseData(const std::string &file, std::vector<std::vector<int>> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        std::vector<int> vals{};
        for (char c : line)
            vals.push_back(c - '0');
        data.push_back(vals);
    }
}

int findNumTrails(const std::vector<std::vector<int>> &data, size_t row, size_t col) {
    int numTrails{0};

    std::set<std::pair<size_t, size_t>> visited{};
    std::stack<std::pair<size_t, size_t>> stack{};
    stack.push(std::make_pair(row, col));
    // do BFS
    while (!stack.empty()) {
        auto pos = stack.top();
        stack.pop();

        const int val = data[pos.first][pos.second];
        if (val == 9 && visited.count(pos) == 0) {
            ++numTrails;
        }
        visited.insert(pos);

        // Check surrounding squares
        if (pos.first > 0 && data[pos.first - 1][pos.second] == val + 1 && visited.count(std::make_pair(pos.first - 1, pos.second)) == 0) {
            stack.push(std::make_pair(pos.first - 1, pos.second));
        }
        if (pos.first < data.size() - 1 && data[pos.first + 1][pos.second] == val + 1 && visited.count(std::make_pair(pos.first + 1, pos.second)) == 0) {
            stack.push(std::make_pair(pos.first + 1, pos.second));
        }
        if (pos.second > 0 && data[pos.first][pos.second - 1] == val + 1 && visited.count(std::make_pair(pos.first, pos.second - 1)) == 0) {
            stack.push(std::make_pair(pos.first, pos.second - 1));
        }
        if (pos.second < data[pos.first].size() && data[pos.first][pos.second + 1] == val + 1 && visited.count(std::make_pair(pos.first, pos.second + 1)) == 0) {
            stack.push(std::make_pair(pos.first, pos.second + 1));
        }
    }

    return numTrails;
}

void part1(std::vector<std::vector<int>> data) {
    int sum{0};
    for (size_t i{0}; i != data.size(); ++i) {
        int numZeros = std::count(data[i].begin(), data[i].end(), 0);
        auto it = data[i].begin();
        for (int j{0}; j != numZeros; ++j) {
            it = std::find(it, data[i].end(), 0);
            size_t col = std::distance(data[i].begin(), it);
            ++it;  // To not find the same one twice
            sum += findNumTrails(data, i, col);
        }
    }

    std::cout << "Part 1: " << sum << std::endl;
}

// Don't use a visited to keep track of all paths
int findNumTrails2(const std::vector<std::vector<int>> &data, size_t row, size_t col) {
    int numTrails{0};

    std::stack<std::pair<size_t, size_t>> stack{};
    stack.push(std::make_pair(row, col));
    // do DFS
    while (!stack.empty()) {
        auto pos = stack.top();
        stack.pop();

        const int val = data[pos.first][pos.second];
        if (val == 9) {
            ++numTrails;
        }

        if (pos.first > 0 && data[pos.first - 1][pos.second] == val + 1) {
            stack.push(std::make_pair(pos.first - 1, pos.second));
        }
        if (pos.first < data.size() - 1 && data[pos.first + 1][pos.second] == val + 1) {
            stack.push(std::make_pair(pos.first + 1, pos.second));
        }
        if (pos.second > 0 && data[pos.first][pos.second - 1] == val + 1) {
            stack.push(std::make_pair(pos.first, pos.second - 1));
        }
        if (pos.second < data[pos.first].size() && data[pos.first][pos.second + 1] == val + 1) {
            stack.push(std::make_pair(pos.first, pos.second + 1));
        }
    }

    return numTrails;
}

void part2(std::vector<std::vector<int>> data) {
    int sum{0};
    for (size_t i{0}; i != data.size(); ++i) {
        int numZeros = std::count(data[i].begin(), data[i].end(), 0);
        auto it = data[i].begin();
        for (int j{0}; j != numZeros; ++j) {
            it = std::find(it, data[i].end(), 0);
            size_t col = std::distance(data[i].begin(), it);
            ++it;  // To not find the same one twice
            sum += findNumTrails2(data, i, col);
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
    std::vector<std::vector<int>> data;
    parseData(input_file, data);

    part1(data);
    part2(data);

    return 0;
}
