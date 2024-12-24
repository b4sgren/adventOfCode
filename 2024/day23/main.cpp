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

constexpr int64_t MODULO = 16777216;

void parseData(const std::string &file, std::map<std::string, std::vector<std::string>> &data) {
    std::ifstream fin{file};
    if (!fin.is_open()) return;

    std::string line;
    while (std::getline(fin, line)) {
        const std::string com1 = line.substr(0, 2);
        const std::string com2 = line.substr(3, 2);

        data[com1].push_back(com2);
        data[com2].push_back(com1);
    }

    // Sort alphabetically
    for (auto &pair : data) {
        std::sort(pair.second.begin(), pair.second.end());
    }
}

void part1(std::map<std::string, std::vector<std::string>> data) {
    std::set<std::vector<std::string>> groups{};

    for (auto pair : data) {
        if (pair.first[0] != 't') continue;
        if (pair.second.size() < 2) continue;  // Can't for a clique of size 3

        for (size_t i{0}; i != pair.second.size() - 1; ++i) {
            std::string str1 = pair.second[i];
            for (size_t j{i + 1}; j != pair.second.size(); ++j) {
                std::string str2 = pair.second[j];
                auto it = std::find(data[str1].begin(), data[str1].end(), str2);
                if (it != data[str1].end()) {
                    std::vector<std::string> temp{pair.first, str1, str2};
                    std::sort(temp.begin(), temp.end());
                    groups.insert(temp);
                }
            }
        }
    }

    std::cout << "Part 1: " << groups.size() << std::endl;
}

std::vector<std::string> current_clique{};
std::vector<std::string> max_clique{};
void find_max_clique(const std::string &v, std::map<std::string, std::vector<std::string>> graph) {
    // Add the current vertex to the clique
    current_clique.push_back(v);

    // Check if the current clique is larger than the maximum clique
    if (current_clique.size() > max_clique.size()) {
        max_clique = current_clique;
    }

    // Try adding more vertices to the clique
    // for (int u = v + 1; u < n; u++) {
    for (std::string u : graph[v]) {
        bool is_adjacent = true;
        // for (std::string w : current_clique) {
        for (std::string w : current_clique) {
            auto it = std::find(graph[u].begin(), graph[u].end(), w);
            // if (!graph[u][w]) {
            if (it == graph[u].end()) {
                is_adjacent = false;
                break;
            }
        }
        if (is_adjacent) {
            find_max_clique(u, graph);
        }
    }

    // Remove the current vertex from the clique
    current_clique.pop_back();
}

// Modify to work. Should be much more efficient
std::vector<std::string> findMaxKCore(std::map<std::string, std::vector<std::string>> graph) {
    std::map<std::string, int> degree;
    std::set<std::string> visited;

    // Calculate the degree of each node
    for (const auto &[node, neighbors] : graph) {
        degree[node] = neighbors.size();
    }

    // Minimum priority queue to process nodes with the lowest degree first
    std::priority_queue<std::pair<int, std::string>, std::vector<std::pair<int, std::string>>, std::greater<>> pq;
    for (const auto &[node, deg] : degree) {
        pq.push({deg, node});
    }

    int maxK = 0;
    std::map<int, std::vector<std::string>> kCores;

    while (!pq.empty()) {
        auto [curDegree, node] = pq.top();
        pq.pop();

        if (visited.count(node)) continue;

        maxK = std::max(maxK, curDegree);
        visited.insert(node);

        // Remove the node from its neighbors
        for (std::string neighbor : graph.at(node)) {
            if (!visited.count(neighbor)) {
                degree[neighbor]--;
                pq.push({degree[neighbor], neighbor});
            }
        }

        kCores[maxK].push_back(node);
    }

    // The maximum k-core is represented by maxK
    return kCores[maxK];
}

void part2(std::map<std::string, std::vector<std::string>> data) {
    // // Find the maximum clique. takes to long
    // for (auto pair : data) {
    //     find_max_clique(pair.first, data);
    // }

    // Much faster max clique alg
    // Only because the each node only has 13 edges or so
    std::set<std::string> maxClique{};
    for (auto pair : data) {
        std::set<std::string> set{};
        set.insert(pair.first);

        for (std::string node : pair.second) {
            bool add_node{true};
            for (std::string u : set) {
                const auto it = std::find(data[u].begin(), data[u].end(), node);
                if (it == data[u].end()) {
                    add_node = false;
                    break;
                }
            }
            if (add_node) set.insert(node);
        }
        if (set.size() > maxClique.size()) maxClique = set;
    }

    std::vector<std::string> vec(maxClique.begin(), maxClique.end());
    std::sort(vec.begin(), vec.end());
    std::cout << "Part 2: ";
    for (std::string str : vec) std::cout << str << ",";
    std::cout << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Input the path to the input file" << std::endl;
        return 0;
    }

    std::string input_file = std::string(argv[1]);
    std::map<std::string, std::vector<std::string>> data{};
    parseData(input_file, data);

    part1(data);
    part2(data);

    return 0;
}
