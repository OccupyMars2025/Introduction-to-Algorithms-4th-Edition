/*
-lpthread:

This option links the pthread (POSIX threads) library. 
It is necessary because the code uses std::this_thread::sleep_for which relies on threading functionality provided by the pthread library.
 By linking this library, you ensure that the program can use multithreading features correctly.

Link against the pthread library (-lpthread) to support threading functionality used in the program.

*/


#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <sstream>
#include <thread>
#include <algorithm>
#include <iomanip> // For std::setfill and std::setw

class TreeNode {
public:
    int key;
    TreeNode* left;
    TreeNode* right;
    TreeNode* parent;

    TreeNode(int key) : key(key), left(nullptr), right(nullptr), parent(nullptr) {}
};

class BinarySearchTree {
public:
    TreeNode* root;

    BinarySearchTree() : root(nullptr) {}

    void transplant(TreeNode* u, TreeNode* v) {
        if (u->parent == nullptr) {
            root = v;
        } else if (u == u->parent->left) {
            u->parent->left = v;
        } else {
            u->parent->right = v;
        }
        if (v != nullptr) {
            v->parent = u->parent;
        }
    }

    TreeNode* tree_minimum(TreeNode* x) {
        while (x->left != nullptr) {
            x = x->left;
        }
        return x;
    }

    void tree_delete(TreeNode* z) {
        if (z->left == nullptr) {
            transplant(z, z->right);
        } else if (z->right == nullptr) {
            transplant(z, z->left);
        } else {
            TreeNode* y = tree_minimum(z->right);
            if (y->parent != z) {
                transplant(y, y->right);
                y->right = z->right;
                y->right->parent = y;
            }
            transplant(z, y);
            y->left = z->left;
            y->left->parent = y;
        }
        delete z;
    }

    void insert(int key) {
        TreeNode* z = new TreeNode(key);
        TreeNode* y = nullptr;
        TreeNode* x = root;

        while (x != nullptr) {
            y = x;
            if (z->key < x->key) {
                x = x->left;
            } else {
                x = x->right;
            }
        }

        z->parent = y;
        if (y == nullptr) {
            root = z;
        } else if (z->key < y->key) {
            y->left = z;
        } else {
            y->right = z;
        }
    }

    void inorder(TreeNode* node, std::vector<TreeNode*>& inorder_list) {
        if (node != nullptr) {
            inorder(node->left, inorder_list);
            std::cout << node->key << " ";
            inorder_list.push_back(node);
            inorder(node->right, inorder_list);
        }
    }

    void generate_random_bst(int n, std::pair<int, int> key_range) {
        std::vector<int> keys;
        for (int i = key_range.first; i <= key_range.second; ++i) {
            keys.push_back(i);
        }

        std::random_shuffle(keys.begin(), keys.end());

        for (int i = 0; i < n; ++i) {
            insert(keys[i]);
        }
    }

    void visualize(int picture_id, const std::string& comment) {
        std::ofstream file;

        // Format the picture ID with leading zeros to have a width of 3
        std::ostringstream filename;
        filename << "./graphviz/bst_" << std::setfill('0') << std::setw(3) << picture_id << ".dot";
        
        file.open(filename.str());
        file << "digraph BinarySearchTree {\n";
        file << "   labelloc=\"t\";\n";
        file << "   label=\"" << comment << "\";\n";
        file << "   node [shape=circle];\n";

        visualize_node(file, root);

        file << "}\n";
        file.close();

        std::string command = "dot -Tpng " + filename.str() + " -o " + filename.str().substr(0, filename.str().find_last_of('.')) + ".png";
        system(command.c_str());
    }

private:
    void visualize_node(std::ofstream& file, TreeNode* node) {
        if (node != nullptr) {
            if (node->left != nullptr) {
                file << "   " << node->key << " -> " << node->left->key << " [label=\"L\"];\n";
                visualize_node(file, node->left);
            }
            if (node->right != nullptr) {
                file << "   " << node->key << " -> " << node->right->key << " [label=\"R\"];\n";
                visualize_node(file, node->right);
            }
        }
    }
};

void test() {
    BinarySearchTree bst;

    // Generate a random BST with 15 nodes and keys in the range 1 to 100
    bst.generate_random_bst(15, std::make_pair(1, 100));

    std::cout << "Inorder traversal of the random BST:\n";
    std::vector<TreeNode*> inorder_list;
    bst.inorder(bst.root, inorder_list);
    std::cout << "\n";
    for (auto node : inorder_list) {
        std::cout << node->key << " ";
    }
    std::cout << "\n";

    // Visualize the BST
    bst.visualize(0, "Original BST");

    int picture_id = 1;
    while (!inorder_list.empty()) {
        // Pop the node from the inorder list randomly
        int index = rand() % inorder_list.size();
        TreeNode* node = inorder_list[index];
        inorder_list.erase(inorder_list.begin() + index);
        std::cout << "Deleting node with key " << node->key << "\n";
        bst.tree_delete(node);

        // Sleep a bit to see the visualization
        std::this_thread::sleep_for(std::chrono::seconds(1));
        bst.visualize(picture_id, "After deleting " + std::to_string(node->key));
        picture_id++;
    }
}

int main() {
    srand(static_cast<unsigned int>(time(0)));
    test();
    return 0;
}
