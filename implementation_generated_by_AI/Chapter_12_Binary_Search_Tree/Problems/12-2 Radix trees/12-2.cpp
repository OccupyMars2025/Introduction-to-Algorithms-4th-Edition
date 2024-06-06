#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

class TrieNode {
public:
    std::map<char, TrieNode*> children;
    bool is_end_of_string;

    TrieNode() : is_end_of_string(false) {}
};

class RadixTree {
private:
    TrieNode* root;

    void pre_order_traversal(TrieNode* node, const std::string& prefix, std::vector<std::string>& result) {
        if (node->is_end_of_string) {
            result.push_back(prefix);
        }
        /*
        In C++, std::map inherently maintains its elements in ascending order by key. 
        Therefore, you don't need to sort the std::map when iterating over it; it will automatically be in ascending order. 
        */
        for (const auto& pair : node->children) {
            pre_order_traversal(pair.second, prefix + pair.first, result);
        }
    }

    void add_edges(TrieNode* node, const std::string& prefix, std::ofstream& dot) {
        for (const auto& pair : node->children) {
            TrieNode* child = pair.second;
            std::string child_prefix = prefix + pair.first;
            // add double quotes in case "prefix" is an empty string
            dot << "    \"" << prefix << "\" -> \"" << child_prefix << "\" [label=" << pair.first << "];\n";
            if (child->is_end_of_string) {
                dot << "    " << child_prefix << " [style=filled, fillcolor=lightgrey];\n";
            }
            add_edges(child, child_prefix, dot);
        }
    }

public:
    RadixTree() {
        root = new TrieNode();
    }

    void insert(const std::string& string) {
        TrieNode* node = root;
        for (char charac : string) {
            if (node->children.find(charac) == node->children.end()) {
                node->children[charac] = new TrieNode();
            }
            node = node->children[charac];
        }
        node->is_end_of_string = true;
    }

    std::vector<std::string> lexicographic_sort() {
        std::vector<std::string> result;
        pre_order_traversal(root, "", result);
        return result;
    }

    void visualize(const std::string& filename) {
        std::ofstream dot(filename);
        dot << "digraph RadixTree {\n";
        dot << "    node [shape=circle];\n";
        add_edges(root, "", dot);
        dot << "}\n";
        dot.close();

        std::string command = "dot -Tpng " + filename + " -o " + filename + ".png";
        system(command.c_str());

        // display the image
        command = "xdg-open " + filename + ".png";
        system(command.c_str());
    }
};

// Example usage
int main() {
    std::vector<std::string> bit_strings = {"1011", "10", "011", "100", "0"};
    RadixTree radix_tree;

    for (const auto& bit_string : bit_strings) {
        radix_tree.insert(bit_string);
    }

    std::vector<std::string> sorted_strings = radix_tree.lexicographic_sort();
    for (const auto& str : sorted_strings) {
        std::cout << str << ", ";
    }
    std::cout << std::endl;

    // Visualize the radix tree
    radix_tree.visualize("./graphviz/radix_tree.dot");

    return 0;
}
