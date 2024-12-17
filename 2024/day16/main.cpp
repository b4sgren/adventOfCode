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
    std::map<std::vector<size_t>, int> costs{};
    for (size_t i{0}; i != map.size(); ++i)
        for (size_t j{0}; j != map[i].size(); ++j)
            for (size_t k{0}; k != 4; ++k)
                costs.insert({std::vector<size_t>{i, j, k}, 100000000});

    costs[std::vector<size_t>{row, col, 1}] = 0;
    size_t cost{0};
    size_t dir{1};
    std::priority_queue<std::vector<size_t>, std::vector<std::vector<size_t>>, std::greater<std::vector<size_t>>> minHeap;
    minHeap.push({cost, row, col, dir});
    while (map[row][col] != 'E') {
        auto vertex = minHeap.top();
        minHeap.pop();
        cost = vertex[0];
        row = vertex[1];
        col = vertex[2];
        dir = vertex[3];
        std::vector<size_t> key{row, col, dir};

        if (cost > costs[key]) {  // Don't keep looking if cost is greater
            continue;
        }
        if (map[row][col] == 'E') {
            break;
        }
        costs[key] = cost;

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

        // SLIGHT ISSUE HERE. LIMIT THINGS I"VE ADDED TO QUEUE BEFORE
        size_t nextR{row + rowDir}, nextC{col + colDir};
        std::vector<size_t> nextKey{nextR, nextC, dir};
        if (map[nextR][nextC] != '#') {
            if (cost + 1 < costs[nextKey])
                minHeap.push({cost + 1, nextR, nextC, dir});
        }
        // Push turning left and right
        size_t nextDir = (dir + 1) % 4;
        key[2] = nextDir;
        if (cost + 1000 < costs[key])
            minHeap.push({cost + 1000, row, col, nextDir});
        nextDir = dir == 0 ? 3 : dir - 1;
        key[2] = nextDir;
        if (cost + 1000 < costs[key])
            minHeap.push({cost + 1000, row, col, nextDir});
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
