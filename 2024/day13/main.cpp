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

void parseData(const std::string &file, std::vector<std::pair<int, int>> &A, std::vector<std::pair<int, int>> &B, std::vector<std::pair<int, int>> &prize) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        if (line.empty()) continue;
        size_t idx = line.find(':');
        size_t size = line.size();
        std::string str = line.substr(idx, size - idx);
        size_t idx2 = str.find(',');
        size_t idxX = str.find('X');
        size_t idxY = str.find('Y');

        int X = std::stoi(str.substr(idxX + 2, idx2 - idxX - 2));
        int Y = std::stoi(str.substr(idxY + 2, size - idxY - 2));

        if (line[7] == 'A')
            A.emplace_back(X, Y);
        else if (line[7] == 'B')
            B.emplace_back(X, Y);
        else
            prize.emplace_back(X, Y);
    }
}

void part1(const std::vector<std::pair<int, int>> &A, const std::vector<std::pair<int, int>> &B, const std::vector<std::pair<int, int>> &prize) {
    int numTokensA{3}, numTokensB{1};
    int requiredTokens{0};

    // No solution, 1 solution, Many solutions
    // Many solutions will be the difficult one
    for (size_t i{0}; i != A.size(); ++i) {
        const int Ax = A[i].first;
        const int Ay = A[i].second;

        const int Bx = B[i].first;
        const int By = B[i].second;

        const int Px = prize[i].first;
        const int Py = prize[i].second;

        // n*Ax + m*Bx = Px
        // n*Ay + m*By = Py
        // n = (px-m*Bx)/Ax
        // (Px-m*Bx)*Ax/Ay + m*By = Py
        // Px/Ay - m*(Bx*Ax/Ay + By) = Py
        // m = (Py - Px/Ay)/(Bx*Ax/Ay + By)
        // n = (px-m*Bx)/Ax
        // OR
        // n*Ax*Ay + m*Bx*Ay = Px*Ay
        // -(n*Ay*Ax + m*By*Ax = Py*Ax)
        // m(Bx*Ay - By*Ax) = Px*Ay - Py*Ax
        // m = (Px*Ay - Py*Ax)/(Bx*Ay - By*Ax)
        // n = (Px-m*Bx)/Ax

        int n{0}, m{0};
        const int matrixDet{Ax * By - Ay * Bx};
        if (matrixDet == 0) {
            continue;  // May need to edit. Possibly no solution and possibly many solution
        } else {
            // m = (Py - Px / static_cast<double>(Ay)) / (Bx * Ax / static_cast<double>(Ay) + By);
            // n = (Px - m * Bx) / static_cast<double>(Ax);
            m = (Px * Ay - Py * Ax) / (Bx * Ay - By * Ax);
            n = (Px - m * Bx) / Ax;
        }
        if (m < 0 || n < 0)
            continue;
        if (n * Ax + m * Bx != Px || n * Ay + m * By != Py)
            continue;

        requiredTokens += n * numTokensA + m * numTokensB;
    }

    std::cout << "Part 1: " << requiredTokens << std::endl;
}

// Have to do the wall following
// Need a visited map to see which nodes I've checked
// Will need to check all nodes to see if they have an edge
// Increment when I get to a corner
void part2(const std::vector<std::pair<int, int>> &A, const std::vector<std::pair<int, int>> &B, const std::vector<std::pair<int, int>> &prize) {
    int numTokensA{3}, numTokensB{1};
    int64_t requiredTokens{0};
    int64_t offset{10000000000000};

    // No solution, 1 solution, Many solutions
    // Many solutions will be the difficult one
    for (size_t i{0}; i != A.size(); ++i) {
        const int64_t Ax = static_cast<int64_t>(A[i].first);
        const int64_t Ay = static_cast<int64_t>(A[i].second);

        const int64_t Bx = static_cast<int64_t>(B[i].first);
        const int64_t By = static_cast<int64_t>(B[i].second);

        const int64_t Px = static_cast<int64_t>(prize[i].first) + offset;
        const int64_t Py = static_cast<int64_t>(prize[i].second) + offset;

        // n*Ax + m*Bx = Px
        // n*Ay + m*By = Py
        // n = (px-m*Bx)/Ax
        // (Px-m*Bx)*Ax/Ay + m*By = Py
        // Px/Ay - m*(Bx*Ax/Ay + By) = Py
        // m = (Py - Px/Ay)/(Bx*Ax/Ay + By)
        // n = (px-m*Bx)/Ax
        // OR
        // n*Ax*Ay + m*Bx*Ay = Px*Ay
        // -(n*Ay*Ax + m*By*Ax = Py*Ax)
        // m(Bx*Ay - By*Ax) = Px*Ay - Py*Ax
        // m = (Px*Ay - Py*Ax)/(Bx*Ay - By*Ax)
        // n = (Px-m*Bx)/Ax

        int64_t n{0}, m{0};
        const int64_t matrixDet{Ax * By - Ay * Bx};
        if (matrixDet == 0) {
            continue;  // May need to edit. Possibly no solution and possibly many solution
        } else {
            // m = (Py - Px / static_cast<double>(Ay)) / (Bx * Ax / static_cast<double>(Ay) + By);
            // n = (Px - m * Bx) / static_cast<double>(Ax);
            m = (Px * Ay - Py * Ax) / (Bx * Ay - By * Ax);
            n = (Px - m * Bx) / Ax;
        }
        if (m < 0 || n < 0)
            continue;
        if (n * Ax + m * Bx != Px || n * Ay + m * By != Py)
            continue;

        requiredTokens += n * numTokensA + m * numTokensB;
    }

    std::cout << "Part 2: " << requiredTokens << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<std::pair<int, int>> A{}, B{}, prize{};
    parseData(input_file, A, B, prize);

    part1(A, B, prize);
    part2(A, B, prize);  // 875318608908 is to low

    return 0;
}
