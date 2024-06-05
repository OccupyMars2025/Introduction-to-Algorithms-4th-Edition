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
    TreeNode* succ; // Pointer to the successor of the node

    TreeNode(int key) : key(key), left(nullptr), right(nullptr), succ(nullptr) {}
};

class BinarySearchTree {
public:
    TreeNode* root;

    BinarySearchTree() : root(nullptr) {}

    /*
    replace the subtree rooted at node u with the subtree rooted at node v.
    u cannot be nullptr. but v and u_parent can be nullptr.

    After the transplant operation, the subtree rooted at node u matains all its nodes' pointer fields unchanged and
    the whole tree rooted at "root" mantains its structue (i.e. can pass the test of test_structure() function)
    */
    void transplant(TreeNode *u_parent, TreeNode* u, TreeNode* v) {
        if (u_parent == nullptr) {
            root = v;
            if (v != nullptr) {
                tree_maximum(v)->succ = nullptr;
            }
            return;
        }

        // Now u_parent is not null 
        if (v == nullptr) {
            if (u_parent->left == u) {
                TreeNode *u_subtree_min_predecessor = predecessor(tree_minimum(u));
                u_parent->left = nullptr;
                if (u_subtree_min_predecessor != nullptr) {
                    u_subtree_min_predecessor->succ = u_parent;
                }
            } else {
                TreeNode *u_subtree_max = tree_maximum(u);
                u_parent->right = nullptr;
                u_parent->succ = u_subtree_max->succ;                
            }
            return;
        }

        // Now u_parent is not null and v is not null
        if (u_parent->left == u) {
            TreeNode *u_subtree_min_predecessor = predecessor(tree_minimum(u));
            u_parent->left = v;
            if(u_subtree_min_predecessor != nullptr) {
                u_subtree_min_predecessor->succ = tree_minimum(v);
            }
            tree_maximum(v)->succ = u_parent;
        } else {
            TreeNode *u_subtree_max_successor = tree_maximum(u)->succ;
            u_parent->right = v;
            u->succ = tree_minimum(v);
            tree_maximum(v)->succ = u_subtree_max_successor;
        }
    }

    TreeNode* tree_minimum(TreeNode* x) {
        while (x->left != nullptr) {
            x = x->left;
        }
        return x;
    }

    TreeNode* tree_maximum(TreeNode* x) {
        while (x->right != nullptr) {
            x = x->right;
        }
        return x;
    }

    TreeNode *get_parent(TreeNode *x) {
        if (x == root) {
            return nullptr;
        }
        TreeNode *current = root;
        while (current != nullptr) {
            if(current->left == x || current->right == x) {
                return current;
            }
            if (x->key < current->key) {
                current = current->left;
            } else {
                current = current->right;
            }
        }
        return nullptr;
    }

    /*
    Who's the genius that uses node->succ instead of node->parent?
    
    Make clear what transplant(u_parent, u, v) will do.
    */
    void tree_delete(TreeNode* z) {
        TreeNode *q = get_parent(z);
        if (z->left == nullptr) {
            transplant(q, z, z->right);
        } else if (z->right == nullptr) {
            transplant(q, z, z->left);
        } else {
            TreeNode *z_subtree_min = tree_minimum(z);
            TreeNode *z_subtree_min_predecessor = predecessor(z_subtree_min);

            TreeNode* y = tree_minimum(z->right);
            TreeNode *y_parent = get_parent(y);
            if (y_parent != z) {
                transplant(y_parent, y, y->right);
                y->right = z->right;
                // no need to modify anything in the subtree rooted at y
            }
            transplant(q, z, y);
            // Now predecessor(original z subtree).succ   is y, but actually it should remain unchanged
            y->left = z->left;
            tree_maximum(y->left)->succ = y;

            if (z_subtree_min_predecessor != nullptr) {
                z_subtree_min_predecessor->succ = z_subtree_min;
            }
        }
        delete z;
    }

    void insert(int key) {
        TreeNode* z = new TreeNode(key);
        if (root == nullptr) {
            root = z;
            return;
        }
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

        if (z->key < y->key) {
            // Caution: do not switch the order of the following two lines
            TreeNode* y_predecessor = predecessor(y);
            y->left = z;
            if (y_predecessor != nullptr) {
                y_predecessor->succ = z;
            }
            z->succ = y;
        } else {
            y->right = z;
            z->succ = y->succ;
            y->succ = z;
        }
    }

    TreeNode* predecessor(TreeNode* x) {
        if (x->left != nullptr) {
            return tree_maximum(x->left);
        } else {
            // Find the lowest ancestor of x whose right child is also an ancestor of x
            TreeNode* current = root;
            TreeNode* x_predecessor = nullptr;
            while (current != x) {
                if (x->key < current->key) {
                    current = current->left;
                } else {
                    x_predecessor = current;
                    current = current->right;
                }
            }
            return x_predecessor;
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

    void generate_random_bst_with_verbose_info(int n, std::pair<int, int> key_range) {
        std::vector<int> keys;
        for (int i = key_range.first; i <= key_range.second; ++i) {
            keys.push_back(i);
        }
        std::random_shuffle(keys.begin(), keys.end());

        int picture_id = 0;
        visualize(picture_id, "Empty BST", "insertion");
        for (int i = 0; i < n; ++i) {
            insert(keys[i]);
            std::string label = "After inserting " + std::to_string(keys[i]);
            std::cout << label << "\n";
            picture_id++;
            visualize(picture_id, label, "insertion");

            test_structure();
        }
    }

    void visualize(int picture_id, const std::string& label, const std::string& additional_info_to_path) {
        std::ofstream file;

        // Format the picture ID with leading zeros to have a width of 3
        std::ostringstream filename;
        filename << "./graphviz/bst_" << additional_info_to_path << "_" << std::setfill('0') << std::setw(3) << picture_id << ".dot";
        
        file.open(filename.str());
        file << "digraph BinarySearchTree {\n";
        file << "   labelloc=\"top\";\n";
        file << "   label=\"" << label << "\";\n";
        file << "   node [shape=circle];\n";

        if(root) {
            // Add the root node, or you cannot see the root node if it is the only one node left
            file << "   " << root->key << ";\n";
            visualize_node(file, root);
        }

        file << "}\n";
        file.close();

        std::string generated_picture_path = filename.str().substr(0, filename.str().find_last_of('.')) + ".png";
        std::string command = "dot -Tpng " + filename.str() + " -o " + generated_picture_path;
        system(command.c_str());

        // open the generated picture
        command = "xdg-open " + generated_picture_path;
        system(command.c_str());
    }

    void test_structure() {
        if (root == nullptr) {
            std::cout << "The tree is empty\n";
            return;
        }
        std::vector<TreeNode *> collected_inorder_list, collected_inorder_list_v2;
        inorder(root, collected_inorder_list);
        std::cout << std::endl;

        TreeNode *next_node = tree_minimum(root);
        while (next_node != nullptr) {
            collected_inorder_list_v2.push_back(next_node);
            next_node = next_node->succ;
        }
        for (TreeNode *node : collected_inorder_list_v2) {
            std::cout << node->key << " ";
        }
        std::cout << std::endl;

        int num_nodes = collected_inorder_list.size();
        int num_nodes_v2 = collected_inorder_list_v2.size();
        if (num_nodes != num_nodes_v2){
            std::cerr << "The two inorder lists have different sizes: " << num_nodes << " " << num_nodes_v2 << "\n";
            exit(1);
        }
        for(int i = 0; i < num_nodes; i++){
            if (collected_inorder_list[i] != collected_inorder_list_v2[i]){
                std::cerr << "The two inorder lists are different\n";
                exit(1);
            }
            if (i > 0) {
                if (collected_inorder_list[i-1]->key >= collected_inorder_list[i]->key){
                    std::cerr << "The inorder list is not sorted\n";
                    exit(1);
                }
            
            }
        }
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
            if (node->succ != nullptr) {
                file << "   " << node->key << " -> " << node->succ->key << " [color=red];\n";
            }
        }
    }
};

void test() {
    BinarySearchTree bst;

    // Generate a random BST with 15 nodes and keys in the range 1 to 100
    // bst.generate_random_bst(15, std::make_pair(1, 100));
    bst.generate_random_bst_with_verbose_info(15, std::make_pair(1, 100));

    std::vector<TreeNode*> inorder_list;
    bst.inorder(bst.root, inorder_list);
    std::cout << std::endl;

    int picture_id = 1;
    while (!inorder_list.empty()) {
        // Pop the node from the inorder list randomly
        int index = rand() % inorder_list.size();
        TreeNode* node = inorder_list[index];
        std::string label = "After deleting " + std::to_string(node->key);
        inorder_list.erase(inorder_list.begin() + index);
        std::cout << "Deleting node with key " << node->key << "\n";
        bst.tree_delete(node);

        // // Sleep a bit to see the visualization
        // std::this_thread::sleep_for(std::chrono::seconds(1));
        bst.visualize(picture_id, label, "deletion");
        picture_id++;

        bst.test_structure();
    }
}

int main() {
    srand(static_cast<unsigned int>(time(0)));
    test();
    return 0;
}
