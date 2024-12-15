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

// constexpr int MAX_GRID_ROWS = 7;
// constexpr int MAX_GRID_COLS = 11;

constexpr int MAX_GRID_ROWS = 103;
constexpr int MAX_GRID_COLS = 101;

const int MAX_TIME = 100;
std::ofstream fout{"tree.txt"};

class Robot {
   public:
    Robot() : r{0}, c{0}, vr{0}, vc{0} {}
    Robot(int r_, int c_, int vr_, int vc_) : r{r_}, c{c_}, vr{vr_}, vc{vc_} {}

    void move(int dt) {
        r += vr * dt;
        c += vc * dt;

        if (r >= MAX_GRID_ROWS) {
            r %= MAX_GRID_ROWS;
        } else if (r < 0) {
            r += MAX_GRID_ROWS;
        }

        if (c >= MAX_GRID_COLS) {
            c %= MAX_GRID_COLS;
        } else if (c < 0) {
            c += MAX_GRID_COLS;
        }
    }

    std::pair<int, int> getPosition() { return std::make_pair(r, c); }

   private:
    int r;
    int c;
    int vr;
    int vc;
};

void parseData(const std::string &file, std::vector<Robot> &robots) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        if (line.empty()) continue;
        size_t idx = line.find(' ');
        size_t size = line.size();

        std::string posStr = line.substr(0, idx);
        std::string velStr = line.substr(idx + 1, size - idx + 1);

        idx = posStr.find(',');
        int x = std::stoi(posStr.substr(2, idx - 2));
        int y = std::stoi(posStr.substr(idx + 1, posStr.size() - idx - 1));
        idx = velStr.find(',');
        int vx = std::stoi(velStr.substr(2, idx - 2));
        int vy = std::stoi(velStr.substr(idx + 1, velStr.size() - idx - 1));

        robots.emplace_back(y, x, vy, vx);
    }
}

void part1(std::vector<Robot> robots) {
    int quad1{0}, quad2{0}, quad3{0}, quad4{0};

    int temp{0};
    int midR = MAX_GRID_ROWS / 2;
    int midC = MAX_GRID_COLS / 2;
    std::vector<std::pair<int, int>> positions{};
    for (Robot &robot : robots) {
        for (int i{0}; i != MAX_TIME; ++i)
            robot.move(1);
        auto pos = robot.getPosition();
        positions.push_back(pos);
        const int r{pos.first};
        const int c{pos.second};

        if (r < 0 || c < 0 || r >= MAX_GRID_ROWS || c >= MAX_GRID_COLS)
            ++temp;

        if (r < midR && c < midC)
            ++quad1;
        else if (r < midR && c > midC)
            ++quad2;
        else if (r > midR && c < midC)
            ++quad3;
        else if (r > midR && c > midC)
            ++quad4;
    }

    std::cout << "Part 1: " << quad1 * quad2 * quad3 * quad4 << std::endl;
}

bool formsLoop(std::vector<std::pair<int, int>> positions) {
    std::vector<std::vector<int>> grid(MAX_GRID_ROWS, std::vector<int>(MAX_GRID_COLS, -1));
    for (auto pos : positions) {
        grid[pos.first][pos.second] = 1;
    }

    for (std::vector<int> vec : grid) {
        for (int v : vec) {
            if (v < 0) {
                fout << ".";
            } else {
                fout << "x";
            }
        }
        fout << "\n";
    }
    fout << "\n=================================================\n";
    // // return false;

    std::vector<std::vector<bool>>
        visited(MAX_GRID_ROWS, std::vector<bool>(MAX_GRID_COLS, false));
    std::stack<std::pair<int, int>> stack{};
    std::stack<std::pair<int, int>> parent{};
    stack.push(positions[0]);
    parent.push(positions[0]);
    int numVisited{0};
    while (!stack.empty()) {
        auto pos = stack.top();
        stack.pop();
        auto prev = parent.top();
        parent.pop();
        // If visited then skip
        if (visited[pos.first][pos.second])
            continue;

        visited[pos.first][pos.second] = true;
        ++numVisited;

        // Check surrounding tiles
        const int r{pos.first}, c{pos.second};
        if (r > 0 && grid[r - 1][c] == 1 && !visited[r - 1][c]) {
            stack.push(std::make_pair(r - 1, c));
            parent.push(pos);
        } else if (r > 0 && grid[r - 1][c] == 1 && visited[r - 1][c] && prev != std::make_pair(r - 1, c)) {
            if (numVisited == positions.size())
                return true;
            else
                return false;
        }

        if (r < grid.size() - 1 && grid[r + 1][c] == 1 && !visited[r + 1][c]) {
            stack.push(std::make_pair(r + 1, c));
            parent.push(pos);
        } else if (r < grid.size() - 1 && grid[r + 1][c] == 1 && visited[r + 1][c] && prev != std::make_pair(r + 1, c)) {
            if (numVisited == positions.size())
                return true;
            else
                return false;
        }

        if (c > 0 && grid[r][c - 1] == 1 && !visited[r][c - 1]) {
            stack.push(std::make_pair(r, c - 1));
            parent.push(pos);
        } else if (c > 0 && grid[r][c - 1] == 1 && visited[r][c - 1] && prev != std::make_pair(r, c - 1)) {
            if (numVisited == positions.size())
                return true;
            else
                return false;
        }

        if (c < grid[r].size() - 1 && grid[r][c + 1] == 1 && !visited[r][c + 1]) {
            stack.push(std::make_pair(r, c + 1));
            parent.push(pos);
        } else if (c < grid[r].size() - 1 && grid[r][c + 1] == 1 && visited[r][c + 1] && prev != std::make_pair(r, c + 1)) {
            if (numVisited == positions.size())
                return true;
            else
                return false;
        }
    }
    return false;
}

void part2(std::vector<Robot> robots) {
    int counter{0};
    // while (true) {
    for (int i{0}; i != 20000; ++i) {
        fout << counter << "\n";
        ++counter;
        std::vector<std::pair<int, int>> positions{};
        for (Robot &robot : robots) {
            robot.move(1);
            positions.push_back(robot.getPosition());
        }

        if (formsLoop(positions))
            break;
    }

    std::cout << "Part 2: " << counter << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<Robot> robots{};
    parseData(input_file, robots);

    part1(robots);
    part2(robots);  // 653 is too low

    return 0;
}
