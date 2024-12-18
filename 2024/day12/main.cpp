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
    // Verify that I'm on an edge

    std::set<std::pair<size_t, size_t>> visited{};
    int perimeter{0};
    for (auto pair : idInArea) {
        // Don't do twice
        if (visited.count(pair) != 0) continue;
        visited.insert(pair);
        size_t row{pair.first}, col{pair.second};

        // Determine if we are on an edge of a region
        bool onEdge = false;
        // On the edge of the garden
        if (row == 0 || row == data.size() - 1 || col == 0 || col == data[0].size() - 1) onEdge = true;
        // Check to make sure we are not surrounded by the same plant
        if (row > 0 && data[row - 1][col] != plant) onEdge = true;
        if (row < data.size() - 1 && data[row + 1][col] != plant) onEdge = true;
        if (col > 0 && data[row][col - 1] != plant) onEdge = true;
        if (col < data.size() - 1 && data[row][col + 1] != plant) onEdge = true;

        if (!onEdge) continue;  // No an edge tile

        // Which direction am I facing: 0: North, 1:East, 2:South, 3:West
        int direction{0};
        // Cases where we are on the edge
        if (row == 0)
            direction = 1;
        else if (row == data.size() - 1)
            direction = 3;
        else if (col == 0)
            direction = 0;
        else if (col == data.size() - 1)
            direction = 2;
        else if (row > 0 && data[row - 1][col] != plant)
            direction = 1;
        else if (row < data.size() - 1 && data[row + 1][col] != plant)
            direction = 3;
        else if (col > 0 && data[row][col - 1] != plant)
            direction = 0;
        else if (col < data[0].size() - 1 && data[row][col + 1] != plant)
            direction = 2;

        const size_t r0{row};
        const size_t c0{col};
        const int d0{direction};

        // Do wall following: Default to try and turn left, then go straight, then turn right
        // Edge case of an inside corner __|
        do {
            visited.insert(std::make_pair(row, col));
            if (direction == 0) {
                if (row == 0 || data[row - 1][col] != plant) {
                    ++perimeter;
                    ++direction;
                } else
                    --row;
            } else if (direction == 1) {
                if (col == data[row].size() - 1 || data[row][col + 1] != plant) {
                    ++direction;
                    ++perimeter;
                } else
                    ++col;
            } else if (direction == 2) {
                if (row == data.size() - 1 || data[row + 1][col] != plant) {
                    ++direction;
                    ++perimeter;
                } else
                    ++row;
            } else if (direction == 3) {
                if (col == 0 || data[row][col - 1] != plant) {
                    direction = 0;
                    ++perimeter;
                } else
                    --col;
            }

            // Check for special cases
            if (direction == 0 && col > 0 && data[row][col - 1] == plant) {
                --col;
                direction = 3;
                ++perimeter;
            } else if (direction == 1 && row > 0 && data[row - 1][col] == plant) {
                --row;
                direction = 0;
                ++perimeter;
            } else if (direction == 2 && col < data[row].size() - 1 && data[row][col + 1] == plant) {
                ++col;
                direction = 1;
                ++perimeter;
            } else if (direction == 3 && row < data.size() - 1 && data[row + 1][col] == plant) {
                ++row;
                direction = 2;
                ++perimeter;
            }
        } while (row != r0 || col != c0 || direction != d0);
    }
    // Error with this condition

    return perimeter;
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
