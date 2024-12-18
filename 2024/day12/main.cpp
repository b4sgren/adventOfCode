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

void parseData(const std::string &file, std::vector<std::string> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        data.push_back(line);
    }
}

char findRegion(const std::vector<std::string> &data, const std::vector<std::vector<bool>> &visited, size_t &row, size_t &col) {
    for (; row < data.size(); ++row) {
        for (col = 0; col < data[row].size(); ++col) {
            if (!visited[row][col]) {
                return data[row][col];
            }
        }
    }

    return '.';
}

int fillArea(const std::vector<std::string> &data, size_t row, size_t col, char plant, std::vector<std::vector<bool>> &visited) {
    int numVisited{0};
    int perimeter{0};

    std::stack<std::pair<size_t, size_t>> stack{};
    stack.push(std::make_pair(row, col));
    // BFS
    while (!stack.empty()) {
        auto pos = stack.top();
        stack.pop();
        const size_t r = pos.first;
        const size_t c = pos.second;

        if (!visited[pos.first][pos.second]) {
            ++numVisited;
            // Find sides that need to be fenced
            if (r == 0 || r == data.size() - 1)
                ++perimeter;
            if (c == 0 || c == data[0].size() - 1)
                ++perimeter;
            if (r < data.size() - 1 && data[r + 1][c] != plant)
                ++perimeter;
            if (r > 0 && data[r - 1][c] != plant)
                ++perimeter;
            if (c < data[0].size() - 1 && data[r][c + 1] != plant)
                ++perimeter;
            if (c > 0 && data[r][c - 1] != plant)
                ++perimeter;
        }
        visited[pos.first][pos.second] = true;

        // Check neighbors and push onto stack
        if (r > 0 && data[r - 1][c] == plant && !visited[r - 1][c]) {
            stack.push(std::make_pair(r - 1, c));
        }
        if (r < data.size() - 1 && data[r + 1][c] == plant && !visited[r + 1][c]) {
            stack.push(std::make_pair(r + 1, c));
        }
        if (c > 0 && data[r][c - 1] == plant && !visited[r][c - 1]) {
            stack.push(std::make_pair(r, c - 1));
        }
        if (c < data[r].size() - 1 && data[r][c + 1] == plant && !visited[r][c + 1]) {
            stack.push(std::make_pair(r, c + 1));
        }
    }

    return numVisited * perimeter;
}

void part1(std::vector<std::string> data) {
    int cost{0};
    std::vector<std::vector<bool>> visited(data.size(), std::vector<bool>(data[0].size(), false));

    size_t row{0}, col{0};
    while (row < data.size()) {
        // Identify a new region
        char plant = findRegion(data, visited, row, col);
        if (plant == '.') break;

        // BFS to find area
        cost += fillArea(data, row, col, plant, visited);
    }

    std::cout << "Part 1: " << cost << std::endl;
}

int fillArea2(const std::vector<std::string> &data, size_t row, size_t col, char plant, std::vector<std::vector<bool>> &visited, std::set<std::pair<size_t, size_t>> &idInArea) {
    int numVisited{0};

    std::stack<std::pair<size_t, size_t>> stack{};
    stack.push(std::make_pair(row, col));
    // BFS
    while (!stack.empty()) {
        auto pos = stack.top();
        stack.pop();
        const size_t r = pos.first;
        const size_t c = pos.second;
        idInArea.insert(pos);

        if (!visited[pos.first][pos.second]) {
            ++numVisited;
        }
        visited[pos.first][pos.second] = true;

        // Check neighbors and push onto stack
        if (r > 0 && data[r - 1][c] == plant && !visited[r - 1][c]) {
            stack.push(std::make_pair(r - 1, c));
        }
        if (r < data.size() - 1 && data[r + 1][c] == plant && !visited[r + 1][c]) {
            stack.push(std::make_pair(r + 1, c));
        }
        if (c > 0 && data[r][c - 1] == plant && !visited[r][c - 1]) {
            stack.push(std::make_pair(r, c - 1));
        }
        if (c < data[r].size() - 1 && data[r][c + 1] == plant && !visited[r][c + 1]) {
            stack.push(std::make_pair(r, c + 1));
        }
    }

    return numVisited;
}

int findPerimeter(const std::vector<std::string> &data, char plant, const std::set<std::pair<size_t, size_t>> &idInArea) {
    size_t maxR{data.size() - 1}, maxC{data[0].size() - 1};
    int numCorners{0};
    for (auto pair : idInArea) {
        const size_t r{pair.first}, c{pair.second};

        // Special case if on an edge

        std::vector<int> diffs(4, 0);
        if (data[r + 1][c] != plant) diffs[0] = 1;
        if (data[r - 1][c] != plant) diffs[1] = 1;
        if (data[r][c + 1] != plant) diffs[2] = 1;
        if (data[r][c - 1] != plant) diffs[3] = 1;

        // if (data[r + 1][c] != plant) ++numDiff;
        // if (data[r - 1][c] != plant) ++numDiff;
        // if (data[r][c + 1] != plant) ++numDiff;
        // if (data[r][c - 1] != plant) ++numDiff;
        // if (data[r + 1][c - 1] != plant) ++numDiff;
        // if (data[r - 1][c - 1] != plant) ++numDiff;
        // if (data[r + 1][c + 1] != plant) ++numDiff;
        // if (data[r + 1][c - 1] != plant) ++numDiff;

        if (diffs == std::vector<int>{1, 1, 1, 1}) {
            numCorners += 3;
        } else if (diffs == std::vector<int>{1, 1, 1, 0} || diffs == std::vector<int>{1, 1, 0, 1} || diffs == std::vector<int>{1, 0, 1, 1} || diffs == std::vector<int>{0, 1, 1, 1}) {
            numCorners += 3;
        }

        if ((r == 0 && c == 0) || (r == 0 && c == maxC) || (r == maxR && c == 0) || (r == maxR && c == maxC)) {
            ++numCorners;
            // TODO: Check if another corner that is not the edge of the garden
        } else if (data[r][c + 1] != plant && data[r][c - 1] != plant && data[r - 1][c] != plant && data[r + 1][c] != plant) {
            numCorners += 4;  // Surrounded by other plants
        }
        if (data[r][c] == plant && data[r][c + 1] != plant && plant && data[r - 1][c] != plant) {
            ++numCorners;
        }
    }

    return numCorners;
}

void part2(std::vector<std::string> data) {
    int cost{0};
    std::vector<std::vector<bool>> visited(data.size(), std::vector<bool>(data[0].size(), false));

    size_t row{0}, col{0};
    while (row < data.size()) {
        // Identify a new region
        char plant = findRegion(data, visited, row, col);
        if (plant == '.') break;

        // BFS to find area
        std::set<std::pair<size_t, size_t>> idInArea{};
        auto area = fillArea2(data, row, col, plant, visited, idInArea);
        auto perimeter = findPerimeter(data, plant, idInArea);

        cost += area * perimeter;
    }

    std::cout << "Part 2: " << cost << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<std::string> data;
    parseData(input_file, data);

    part1(data);
    part2(data);

    return 0;
}
