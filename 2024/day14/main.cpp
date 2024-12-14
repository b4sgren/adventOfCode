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

constexpr int MAX_GRID_ROWS = 7;
constexpr int MAX_GRID_COLS = 11;

// constexpr int MAX_GRID_ROWS = 103;
// constexpr int MAX_GRID_COLS = 101;

const int MAX_TIME = 100;

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

        robots.emplace_back(x, y, vx, vy);
    }
}

void part1(std::vector<Robot> robots) {
    int quad1{0}, quad2{0}, quad3{0}, quad4{0};

    int temp{0};
    int midR = MAX_GRID_ROWS / 2;
    int midC = MAX_GRID_COLS / 2;
    for (Robot &robot : robots) {
        for (int i{0}; i != MAX_TIME; ++i)
            robot.move(1);
        auto pos = robot.getPosition();
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

    std::cout << "Part 1: " << quad1 * quad2 * quad3 * quad4;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<Robot> robots{};
    parseData(input_file, robots);

    part1(robots);  // 226935000 is to low

    return 0;
}
