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

void parseData(const std::string &file, std::map<std::string, int> &wireMap, std::vector<std::string> &gateMap) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        if (line.empty()) break;
        size_t idx = line.find(':');
        std::string wire = line.substr(0, idx);
        int val = line.back() - '0';

        wireMap[wire] = val;
    }

    while (std::getline(fin, line))
        gateMap.push_back(line);
}

void part1(std::map<std::string, int> wireMap, const std::vector<std::string> &gateMap) {
    std::vector<bool> flags(gateMap.size(), false);
    while (std::find(flags.begin(), flags.end(), false) != flags.end()) {
        size_t cnt{0};
        for (std::string str : gateMap) {
            // Already performed this operation
            if (flags[cnt]) {
                ++cnt;
                continue;
            }
            std::stringstream ss{str};
            std::string wire1, wire2, wireOut, gate, temp;
            std::getline(ss, wire1, ' ');
            std::getline(ss, gate, ' ');
            std::getline(ss, wire2, ' ');
            std::getline(ss, temp, ' ');
            std::getline(ss, wireOut, ' ');

            // Can't do this one yet
            if (wireMap.count(wire1) == 0 || wireMap.count(wire2) == 0) {
                ++cnt;
                continue;
            }

            if (gate == "AND") {
                wireMap[wireOut] = (wireMap[wire1] == wireMap[wire2] && wireMap[wire1] == 1) ? 1 : 0;
            } else if (gate == "OR") {
                wireMap[wireOut] = (wireMap[wire1] == 1 || wireMap[wire2] == 1) ? 1 : 0;
            } else if (gate == "XOR") {
                wireMap[wireOut] = (wireMap[wire1] != wireMap[wire2]) ? 1 : 0;
            } else {
                std::cout << "ERROR: SHOULDN'T BE HERE" << std::endl;
            }
            flags[cnt] = true;
            ++cnt;
        }
    }

    // Compile the number
    int64_t num{0};
    for (auto it{wireMap.rbegin()}; it != wireMap.rend(); ++it) {
        // std::cout << it->first << " " << it->second << std::endl;
        if (it->first[0] != 'z') continue;
        num = (num << 1) + it->second;
    }

    std::cout << "Part 1: " << num << std::endl;
}

// Z should be an addition of x and y
// Get expected bits for Z and compare to actual bits for Z
// Which digits are off??
void part2(std::map<std::string, int> wireMap, const std::vector<std::string> &gateMap) {

    // Create a map for each operation to get the output
    std::map<std::vector<std::string>, std::string> operations{};
    std::map<std::string, std::vector<std::string>> reverseOperations{};
    for (std::string str : gateMap) {
        std::stringstream ss{str};
        std::string wire1, wire2, wireOut, gate, temp;
        std::getline(ss, wire1, ' ');
        std::getline(ss, gate, ' ');
        std::getline(ss, wire2, ' ');
        std::getline(ss, temp, ' ');
        std::getline(ss, wireOut, ' ');

        operations[{wire1, gate, wire2}] = wireOut;
        reverseOperations[wireOut] = std::vector<std::string>{wire1, gate, wire2};
    }


    std::string prevAND = "kng";  // For x02 AND y02
    std::string prevXOR = "phv";
    std::string prevCarryAND = "rkh";
    std::string prevCarryOR = "vnb";
    std::string currAND = "wfd";  // For x03 and y03
    std::string currXOR = "nhh";
    std::string currCarryAND = "";
    std::string currCarryOR = "";

    std::set<std::string> incorrectWires{};
    for (int i{3}; i != 46; ++i) {
        std::string num = std::to_string(i);
        std::string xi = "x" + std::string(2-num.size(), '0') + num;
        std::string yi = "y" + std::string(2-num.size(), '0') + num;
        std::string zi = "z" + std::string(2-num.size(), '0') + num;

        // What to do when I get it wrong... How do I get back on track?? (Flag output and Set it to be the input??)
        // consider the opposite order
        std::vector<std::string> ANDop1{xi, "AND", yi}, ANDop1_2{yi, "AND", xi};
        std::vector<std::string> XORop1{xi, "XOR", yi}, XORop1_2{yi, "XOR", xi};
        currAND = operations.count(ANDop1) != 0 ? operations[ANDop1] : operations[ANDop1_2];
        currXOR = operations.count(XORop1) != 0 ? operations[XORop1] : operations[XORop1_2];
        std::vector<std::string> ORop{prevAND, "OR", prevCarryAND}, ORop_2{prevCarryAND, "OR", prevAND};  // CHECK THAT THE INPUTS AND OUTPUTS MATCH
        // One will be the empty string...
        std::string temp = operations[ORop].size() != 0 ? operations[ORop] : operations[ORop_2];
        auto vec = reverseOperations[temp];
        if (ORop != reverseOperations[temp] && ORop_2 != reverseOperations[temp]) {
            // Problem exists with temp
            if (ORop[0] == vec[0] || ORop_2[0] == vec[0]) {  
                if (ORop[0] == vec[0]) {
                    incorrectWires.insert(prevCarryAND);
                    prevCarryAND = vec[2];
                } else {
                    incorrectWires.insert(prevAND);
                    prevAND = vec[0];
                }
            } else if (ORop[2] == vec[2] || ORop_2[2] == vec[2]) {  
                if (ORop[2] == vec[2]) {
                    incorrectWires.insert(prevAND);
                    prevAND = vec[0];
                } else {
                    incorrectWires.insert(prevCarryAND);
                    prevCarryAND = vec[2];
                }
            } else {  // Neither is correct
                // Is this the correct order??
                incorrectWires.insert(prevCarryAND);
                incorrectWires.insert(prevAND);
                prevCarryAND = vec[0];
                prevAND = vec[2];
            }
        } else {
            // Set currCarryOR
            currCarryOR = temp;
        }

        std::vector<std::string> ANDop2{currCarryOR, "AND", currXOR}, ANDop2_2{currXOR, "AND", currCarryOR};
        temp = operations[ANDop2].size() != 0 ? operations[ANDop2]: operations[ANDop2_2];
        vec = reverseOperations[temp];
        // IS THIS ONE REDUNDANT
        if (ANDop2 != vec && ANDop2_2 != vec) {
            // Problem exists. Could be any or all ...
            if (ANDop2[0] == vec[0] || ANDop2_2[0] == vec[0]) {
                if (ANDop2[0] == vec[0]) {
                    incorrectWires.insert(currXOR);
                    currXOR = vec[2];
                } else {
                    incorrectWires.insert(currCarryOR);
                    currCarryOR = vec[0];
                }
            } else if (ANDop2[2] == vec[2] || ANDop2_2[2] == vec[2]) {  
                if (ANDop2[2] == vec[2]) {
                    incorrectWires.insert(currCarryOR);
                    currCarryOR = vec[0];
                } else {
                    incorrectWires.insert(currXOR);
                    currXOR = vec[2];
                }
            } else {  // Neither is correct
                // Is this the correct order??
                incorrectWires.insert(currCarryOR);
                incorrectWires.insert(currXOR);
                currCarryOR = vec[0];
                currXOR = vec[2];
            }
        } else {
            // Set currCarryAND
            currCarryAND = temp;
            prevCarryAND = currCarryAND;
            prevCarryOR = currCarryOR;
            // set prev stuff??
        }

        std::vector<std::string> XORop2{currXOR, "XOR", currCarryOR}, XORop2_2{currCarryOR, "XOR", currXOR};
        temp = operations[XORop2].size() != 0 ? operations[XORop2] : operations[XORop2_2];
        vec = reverseOperations[temp];
        if (XORop2 != reverseOperations[temp] && XORop2_2 != reverseOperations[temp]) {
            // Problem exists
            // if none match then z is incorrect ...
            // Otherwise it is one of the
            if (XORop2[0] != vec[0] && XORop2[2] != vec[2] && XORop2_2[0] != vec[0] && XORop2_2[2] != vec[0]) {
                incorrectWires.insert(temp);
            } else if (XORop2[0] == vec[0] || XORop2_2[0] == vec[0]) {
                if (XORop2[0] == vec[0]) {
                    incorrectWires.insert(currCarryOR);
                    currCarryOR = vec[2];
                } else {
                    incorrectWires.insert(currXOR);
                    currXOR = vec[0];
                }
            } else if (XORop2[2] == vec[2] || XORop2_2[2] == vec[2]) {  // currCarryOR is good
                if (XORop2[2] == vec[2]) {
                    incorrectWires.insert(currXOR);
                    currXOR = vec[0];
                } else {
                    incorrectWires.insert(currCarryOR);
                    currCarryOR = vec[2];
                }
            } else {
                std::cout << "SUPER ERROR" << std::endl;
            }
        } else {
            // Eveything is good
        }

        prevAND = currAND;
        prevXOR = currXOR;
    }

    std::vector<std::string> temp(incorrectWires.begin(), incorrectWires.end());
    std::sort(temp.begin(), temp.end());
    std::cout << temp.size() << std::endl;
    std::cout << "Part 2: ";
    for (std::string str : temp) std::cout << str << ",";
    std::cout << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::map<std::string, int> wireMap{};
    std::vector<std::string> gateMap{};
    parseData(input_file, wireMap, gateMap);

    part1(wireMap, gateMap);
    part2(wireMap, gateMap);

    return 0;
}
