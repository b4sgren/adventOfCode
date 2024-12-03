#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

void parseData(const std::string &file, std::vector<std::vector<int>> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        std::stringstream sstream{line};
        std::string val;
        std::vector<int> vals{};
        while (std::getline(sstream, val, ' ')) {
            vals.push_back(std::stoi(val));
        }
        data.push_back(vals);
    }
}

void part1(const std::vector<std::vector<int>> &data) {
    int numSafe{0};

    for (int i{0}; i != data.size(); ++i) {
        if (data[i].size() < 2) {
            std::cout << "1 Level" << std::endl;
            continue;
        }
        int sign = (data[i][1] - data[i][0]) >= 0 ? 1 : -1;
        bool isSafe = true;
        for (int j{0}; j != data[i].size() - 1; ++j) {
            const int diff = data[i][j + 1] - data[i][j];
            if (diff * sign <= 0 || abs(diff) > 3 || abs(diff) < 1) {
                isSafe = false;
                break;
            }
        }

        if (isSafe) ++numSafe;
    }

    std::cout << "Part 1: " << numSafe << std::endl;
}

// bool isSafe(const std::vector<int> &data, bool diveDeeper = true) {
//     // Return the index to remove to try and make safe
//     bool isIncreasing = true;

//     for (int i{1}; i != data.size(); ++i) {
//         if (data[i - 1] < data[i]) {
//             if (isIncreasing) {
//                 if (abs(data[i] - data[i - 1]) > 3) {
//                     std::vector<int> data2 = data;
//                     std::vector<int> data3 = data;
//                     data2.erase(data2.begin() + i - 1);
//                     data3.erase(data3.begin() + i);
//                     if (diveDeeper && (isSafe(data2, false) || isSafe(data3, false))) {
//                         return true;
//                     } else {
//                         return false;
//                     }
//                 }
//             } else {
//                 std::vector<int> data2 = data;
//                 std::vector<int> data3 = data;
//                 data2.erase(data2.begin() + i - 1);
//                 data3.erase(data3.begin() + i);
//                 if (diveDeeper && (isSafe(data2, false) || isSafe(data3, false))) {
//                     return true;
//                 } else {
//                     return false;
//                 }
//             }
//         } else if (data[i - 1] > data[i]) {
//             isIncreasing = false;
//             if (abs(data[i] - data[i - 1]) > 3) {
//                 std::vector<int> data2 = data;
//                 std::vector<int> data3 = data;
//                 data2.erase(data2.begin() + i - 1);
//                 data3.erase(data3.begin() + i);
//                 if (diveDeeper && (isSafe(data2, false) || isSafe(data3, false))) {
//                     return true;
//                 } else {
//                     return false;
//                 }
//             }
//         } else if (data[i] == data[i - 1]) {
//             std::vector<int> data2 = data;
//             data2.erase(data2.begin() + i);
//             if (diveDeeper)
//                 return isSafe(data2, false);
//             else
//                 return false;
//         }
//     }

//     return true;
// }

bool isSafe(const std::vector<int> &data, bool diveDeeper = true) {
    // Return the index to remove to try and make safe
    bool isIncreasing = true;

    for (int i{2}; i < data.size(); ++i) {
        if (data[i - 2] < data[i - 1] && data[i - 1] < data[i]) {  // case for increasing
            if (abs(data[i - 2] - data[i - 1]) > 3 || abs(data[i - 1] - data[i]) > 3) {
                if (!diveDeeper) return false;
                auto data2 = data;
                data2.erase(data2.begin() + i);
                bool b1 = isSafe(data2, false);
                auto data3 = data;
                data3.erase(data3.begin() + i - 1);
                bool b2 = isSafe(data3, false);
                auto data4 = data;
                bool b3 = isSafe(data4, false);
                data4.erase(data4.begin() + i - 2);
                if (isSafe(data2, false) || isSafe(data3, false) || isSafe(data4, false)) {
                    return true;
                } else {
                    return false;
                }
            }
        } else if (data[i - 2] > data[i - 1] && data[i - 1] > data[i]) {  // case for decreasing
            isIncreasing = false;
            if (abs(data[i - 2] - data[i - 1]) > 3 || abs(data[i - 1] - data[i]) > 3) {
                if (!diveDeeper) return false;
                auto data2 = data;
                data2.erase(data2.begin() + i);
                bool b1 = isSafe(data2, false);
                auto data3 = data;
                data3.erase(data3.begin() + i - 1);
                bool b2 = isSafe(data3, false);
                auto data4 = data;
                bool b3 = isSafe(data4, false);
                data4.erase(data4.begin() + i - 2);
                if (isSafe(data2, false) || isSafe(data3, false) || isSafe(data4, false)) {
                    return true;
                } else {
                    return false;
                }
            }
        } else if (data[i] == data[i - 1] || data[i - 1] == data[i]) {  // case for equal
            if (!diveDeeper) return false;
            auto data2 = data;
            data2.erase(data2.begin() + i);
            auto data3 = data;
            data3.erase(data3.begin() + i - 1);
            auto data4 = data;
            data4.erase(data4.begin() + i - 2);
            if (isSafe(data2, false) || isSafe(data3, false) || isSafe(data4, false)) {
                return true;
            } else {
                return false;
            }
        } else {  // There is a switch here. Call again with removing different elements
            if (!diveDeeper) return false;
            auto data2 = data;
            data2.erase(data2.begin() + i);
            bool b1 = isSafe(data2, false);
            auto data3 = data;
            data3.erase(data3.begin() + i - 1);
            bool b2 = isSafe(data3, false);
            auto data4 = data;
            bool b3 = isSafe(data4, false);
            data4.erase(data4.begin() + i - 2);
            if (isSafe(data2, false) || isSafe(data3, false) || isSafe(data4, false)) {
                return true;
            } else {
                return false;
            }
        }
    }

    return true;
}

void part2(const std::vector<std::vector<int>> &data) {
    int numSafe{0};

    for (int i{0}; i != data.size(); ++i) {
        if (isSafe(data[i]))
            ++numSafe;
        // else {
        //     for (int j : data[i])
        //         std::cout << j << " ";
        //     std::cout << std::endl;
        // }
    }

    std::cout << "Part 2: " << numSafe << std::endl;
}

int main(int argc, char *argv[]) {
    // if (argc != 2) {
    //     std::cout << "Input the path to the input file" << std::endl;
    //     return 0;
    // }

    // std::string input_file = std::string(argv[1]);
    std::string input_file = "../input.txt";
    std::vector<std::vector<int>> data;
    parseData(input_file, data);

    part1(data);  // 359
    part2(data);  // 462 was too high, 395 was too low

    return 0;
}
