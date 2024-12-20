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

constexpr int MINTIMESAVED = 50;
// constexpr int MINTIMESAVED = 100;

void parseData(const std::string &file, std::vector<std::string> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        data.push_back(line);
    }
}

struct Point {
    std::pair<size_t, size_t> start;
    std::pair<size_t, size_t> end;
};

bool savesTime(std::vector<std::string> data, Point pt) {
    auto start = pt.start;
    auto end = pt.end;

    // BFS but keep track of distance
    size_t row{start.first}, col{start.second}, cost{0};
    std::vector<std::vector<bool>> visited(data.size(), std::vector<bool>(data[0].size(), false));
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
        data[row][col] = 'X';

        // for (auto str : grid)
        //     std::cout << str << "\n";
        // std::cout << "============================\n"
        //           << std::endl;

        if (row == end.first && col == end.second) {  // Reached the end
            if (cost - 2 >= MINTIMESAVED)
                return true;
            else
                return false;
        }

        // Push new nodes onto the stack
        if (row > 0 && !visited[row - 1][col] && data[row - 1][col] != '#') {
            stack.push({cost + 1, row - 1, col});
        }
        if (row < data.size() - 1 && !visited[row + 1][col] && data[row + 1][col] != '#') {
            stack.push({cost + 1, row + 1, col});
        }
        if (col > 0 && !visited[row][col - 1] && data[row][col - 1] != '#') {
            stack.push({cost + 1, row, col - 1});
        }
        if (col < data[0].size() - 1 && !visited[row][col + 1] && data[row][col + 1] != '#') {
            stack.push({cost + 1, row, col + 1});
        }
    }

    // Paths didn't meet up
    return false;
}

void part1(const std::vector<std::string> &data) {
    // Find all # that have a . on either left/right or up/down
    // Count the path len from the start . to the end .

    // No need to check first/last row, col
    std::vector<Point> cheatPoints{};
    for (size_t i{1}; i != data.size() - 1; ++i) {
        for (size_t j{1}; j != data[i].size() - 1; ++j) {
            if (data[i][j] == '#' && data[i][j + 1] != '#' && data[i][j - 1] != '#') {
                const Point pt{std::make_pair(i, j - 1), std::make_pair(i, j + 1)};
                if (savesTime(data, pt)) {
                    cheatPoints.push_back(pt);
                }
            } else if (data[i][j] == '#' && data[i + 1][j] != '#' && data[i - 1][j] != '#') {
                const Point pt{std::make_pair(i - 1, j), std::make_pair(i + 1, j)};
                if (savesTime(data, pt)) {
                    cheatPoints.push_back(pt);
                }
            }
        }
    }

    std::cout << "Part 1: " << cheatPoints.size() << std::endl;
}

std::vector<std::pair<size_t, size_t>> getClosePoints(size_t r, size_t c) {
    std::vector<std::pair<size_t, size_t>> pts{};
    for (size_t i{0}; i != 21; ++i) {
        for (size_t j{0}; j != 21; ++j) {
            if (i == r && j == c) continue;
            if (i + j > 20) continue;
            pts.emplace_back(i, j);
        }
    }

    return pts;
}

// Cheat time of 20 picoseconds
// Compute cost from start to every point on the original path
// COmpute cost between any two points
// COmpute savings by subtracting manhattan distance from cost
void part2(const std::vector<std::string> &data_) {
    size_t row, col;
    for (int i{0}; i != data_.size(); ++i) {
        auto idx = data_[i].find('S');
        if (idx != std::string::npos) {
            row = i;
            col = idx;
        }
    }

    // BFS but keep track of distance
    auto data = data_;
    size_t cost{0};
    std::vector<std::vector<bool>> visited(data.size(), std::vector<bool>(data[0].size(), false));
    std::map<std::pair<size_t, size_t>, int> costMap{};
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
        costMap.insert({std::make_pair(row, col), static_cast<int>(cost)});

        // for (auto str : grid)
        //     std::cout << str << "\n";
        // std::cout << "============================\n"
        //           << std::endl;

        if (data[row][col] == 'E') {  // Reached the end
            break;
        }
        data[row][col] = 'X';

        // Push new nodes onto the stack
        if (row > 0 && !visited[row - 1][col] && data[row - 1][col] != '#') {
            stack.push({cost + 1, row - 1, col});
        }
        if (row < data.size() - 1 && !visited[row + 1][col] && data[row + 1][col] != '#') {
            stack.push({cost + 1, row + 1, col});
        }
        if (col > 0 && !visited[row][col - 1] && data[row][col - 1] != '#') {
            stack.push({cost + 1, row, col - 1});
        }
        if (col < data[0].size() - 1 && !visited[row][col + 1] && data[row][col + 1] != '#') {
            stack.push({cost + 1, row, col + 1});
        }
    }

    std::vector<Point> cheatPoints{};
    for (size_t i{1}; i != data.size() - 1; ++i) {
        for (size_t j{1}; j != data[i].size() - 1; ++j) {
            if (data[i][j] != '.')
                continue;
            const auto closePoints = getClosePoints(i, j);
            for (auto pt : closePoints) {
                size_t r{pt.first}, c{pt.second};
                if (data_[r][c] == '#') continue;
                int shortcutDist = abs(static_cast<int>(i) - static_cast<int>(r)) + abs(static_cast<int>(j) - static_cast<int>(c));
                int dist1 = costMap[{i, j}];
                int dist2 = costMap[{r, c}];
                int dist = dist1 - dist2;

                if (dist - shortcutDist > MINTIMESAVED)
                    cheatPoints.push_back(Point{std::make_pair(i, j), std::make_pair(r, c)});
            }
        }
    }

    std::cout << "Part 2: " << cheatPoints.size() << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<std::string> data{};
    parseData(input_file, data);

    part1(data);
    part2(data);

    return 0;
}
