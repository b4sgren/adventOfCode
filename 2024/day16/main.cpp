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

void parseData(const std::string &file, std::vector<std::string> &map) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        if (line.empty()) break;
        map.push_back(line);
    }
}

void part1(std::vector<std::string> map) {
    // Find the start
    size_t row{0}, col;
    for (; row != map.size(); ++row) {
        col = map[row].find('S');
        if (col != std::string::npos) break;
    }

    // Now look for the shortest path
    std::vector<std::vector<int>> costs(map.size(), std::vector<int>(map[0].size(), 10000000));
    costs[row][col] = 0;
    size_t cost{0};
    size_t dir{0};
    std::priority_queue<std::vector<size_t>, std::vector<std::vector<size_t>>, std::greater<std::vector<size_t>>> minHeap;
    minHeap.push({cost, row, col, dir});
    minHeap.push({cost, row, col, 1});
    minHeap.push({cost, row, col, 2});
    minHeap.push({cost, row, col, 3});
    while (map[row][col] != 'E') {
        auto vertex = minHeap.top();
        minHeap.pop();
        cost = vertex[0];
        row = vertex[1];
        col = vertex[2];
        dir = vertex[3];

        if (cost > costs[row][col]) {  // Don't keep looking if cost is greater
            continue;
        }

        // map[row][col] = 'X';
        // std::cout << row << " " << col << " " << dir << " " << cost << std::endl;
        // for (std::string str : map)
        //     std::cout << str << std::endl;
        // std::cout << "\n========================================" << std::endl;

        int rowDir{0}, colDir{0};
        switch (dir) {
            case 0:
                rowDir = -1;
                break;
            case 1:
                colDir = 1;
                break;
            case 2:
                rowDir = 1;
                break;
            case 3:
                colDir = -1;
                break;
        }

        size_t nextR{row + rowDir}, nextC{col + colDir};
        if (map[nextR][nextC] != '#') {
            minHeap.push({cost + 1, nextR, nextC, dir});
        } else {
            // Push turning left and right
            size_t nextDir = (dir + 1) % 4;
            minHeap.push({cost + 1000, row, col, nextDir});
            nextDir = dir == 0 ? 3 : dir - 1;
            minHeap.push({cost + 1000, row, col, nextDir});
        }
    }

    std::cout << "Part 1: " << cost << std::endl;
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

    return 0;
}
