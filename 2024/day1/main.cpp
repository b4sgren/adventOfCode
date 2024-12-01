#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

void parseData(const std::string &file, std::vector<int> &input1, std::vector<int> &input2) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string num1, num2;
    while (fin >> num1 >> num2) {
        input1.push_back(std::stoi(num1));
        input2.push_back(std::stoi(num2));
    }
}

void part1(std::vector<int> input1, std::vector<int> input2) {
    std::sort(input1.begin(), input1.end());
    std::sort(input2.begin(), input2.end());

    int sum{0};
    for (int i{0}; i != input1.size(); ++i) {
        sum += abs(input1[i] - input2[i]);
    }

    std::cout << "Part 1: " << sum << std::endl;
}

void part2(std::vector<int> input1, std::vector<int> input2) {
    std::sort(input1.begin(), input1.end());
    std::sort(input2.begin(), input2.end());

    int sum{0};
    for (int val : input1) {
        auto lowerBnd = std::lower_bound(input2.begin(), input2.end(), val);
        auto upperBnd = std::upper_bound(input2.begin(), input2.end(), val);
        const int count = std::distance(lowerBnd, upperBnd);
        if (count < 0) continue;

        sum += val * count;
    }

    std::cout << "Part 2: " << sum << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
    }

    std::string input_file = std::string(argv[1]);
    std::vector<int> input1, input2;
    parseData(input_file, input1, input2);

    part1(input1, input2);

    part2(input1, input2);

    return 0;
}
