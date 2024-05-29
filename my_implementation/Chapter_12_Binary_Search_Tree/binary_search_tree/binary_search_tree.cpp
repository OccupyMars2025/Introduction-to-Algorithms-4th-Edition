#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <optional>

class TreeNode {
public:
    int key;
    TreeNode* left;
    TreeNode* right;
    TreeNode* parent;

    TreeNode(int k) : key(k), left(nullptr), right(nullptr), parent(nullptr) {}
};

std::optional<TreeNode*> tree_minimum(TreeNode* root) {
    if (root == nullptr) {
        return std::nullopt;
    }
    while (root->left != nullptr) {
        root = root->left;
    }
    return root;
}

std::optional<TreeNode*> tree_maximum(TreeNode* root) {
    if (root == nullptr) {
        return std::nullopt;
    }
    while (root->right != nullptr) {
        root = root->right;
    }
    return root;
}

std::optional<TreeNode*> tree_successor(TreeNode* x) {
    if (x == nullptr) {
        return std::nullopt;
    }

    if (x->right != nullptr) {
        return tree_minimum(x->right).value();
    } else {
        TreeNode* node = x->parent;
        while (node != nullptr && x == node->right) {
            x = node;
            node = node->parent;
        }
        return node;
    }
}

std::optional<TreeNode*> tree_predecessor(TreeNode* x) {
    if (x == nullptr) {
        return std::nullopt;
    }

    if (x->left != nullptr) {
        return tree_maximum(x->left).value();
    } else {
        TreeNode* node = x->parent;
        while (node != nullptr && x == node->left) {
            x = node;
            node = node->parent;
        }
        return node;
    }
}

std::vector<TreeNode*> inorder_traversal(TreeNode* root) {
    std::vector<TreeNode*> result;
    if (root == nullptr) {
        return result;
    }

    std::vector<TreeNode*> left = inorder_traversal(root->left);
    result.insert(result.end(), left.begin(), left.end());
    result.push_back(root);
    std::vector<TreeNode*> right = inorder_traversal(root->right);
    result.insert(result.end(), right.begin(), right.end());

    return result;
}

void print_binary_tree(TreeNode* root, const std::string& indent = "", const std::string& last = "updown") {
    if (root == nullptr) {
        return;
    }
    std::string updown_prefix = (last == "updown") ? "└── " : "├── ";
    std::cout << indent << updown_prefix << root->key << std::endl;
    std::string new_indent = indent + ((last == "updown") ? "    " : "│   ");
    std::vector<std::pair<TreeNode*, std::string>> children = {{root->left, "left"}, {root->right, "right"}};
    for (int i = 0; i < children.size(); ++i) {
        std::string last_direction = (i == children.size() - 1) ? "updown" : "left";
        print_binary_tree(children[i].first, new_indent, last_direction);
    }
}

TreeNode* tree_search(TreeNode* root, int key) {
    if (root == nullptr || root->key == key) {
        return root;
    }
    if (key < root->key) {
        return tree_search(root->left, key);
    } else {
        return tree_search(root->right, key);
    }
}

TreeNode* iterative_tree_search(TreeNode* root, int key) {
    while (root != nullptr && root->key != key) {
        if (key < root->key) {
            root = root->left;
        } else {
            root = root->right;
        }
    }
    return root;
}

TreeNode* generate_random_binary_search_tree(int min_value, int max_value) {
    if (min_value > max_value) {
        return nullptr;
    }
    int mid = min_value + rand() % (max_value - min_value + 1);
    TreeNode* node = new TreeNode(mid);

    if ((rand() / (RAND_MAX + 1.0)) < 0.9) {
        node->left = generate_random_binary_search_tree(min_value, mid - 1);
        if (node->left != nullptr) {
            node->left->parent = node;
        }
    } else {
        node->left = nullptr;
    }

    if ((rand() / (RAND_MAX + 1.0)) < 0.9) {
        node->right = generate_random_binary_search_tree(mid + 1, max_value);
        if(node->right != nullptr) {
            node->right->parent = node;
        }
    } else {
        node->right = nullptr;
    }

    return node;
}

// int main() {
//     srand(time(nullptr)); // 初始化随机数生成器
//     for (int i = 0; i < 200000; ++i) {
//         TreeNode* tree_root = generate_random_binary_search_tree(-100, 100);
//         for (int key = -150; key < 150; ++key) {
//             TreeNode* result = iterative_tree_search(tree_root, key);
//             TreeNode* result_2 = tree_search(tree_root, key);
//             if (result == nullptr) {
//                 if (result_2 != nullptr) {
//                     std::cerr << "Assertion failed!" << std::endl;
//                     return 1;
//                 }
//             } else {
//                 if (result_2 == nullptr || result->key != result_2->key) {
//                     std::cerr << "Assertion failed!" << std::endl;
//                     return 1;
//                 }
//             }
//         }
//         // 注意：在实际应用中，需要递归删除树以避免内存泄漏
//     }
//     return 0;
// }


int main() {
    srand(time(nullptr)); // Seed the random number generator

    for (int i = 0; i < 20000; ++i) {
        TreeNode* treeRoot = generate_random_binary_search_tree(-100, 100);
        std::vector<TreeNode*> inorderTraversalResult = inorder_traversal(treeRoot);

        if (inorderTraversalResult.empty()) {
            std::cerr << "Assertion failed: Empty inorder traversal result" << std::endl;
            return 1;
        }

        for (int j = 0; j < inorderTraversalResult.size() - 1; ++j) {
            if (inorderTraversalResult[j]->key >= inorderTraversalResult[j + 1]->key) {
                std::cerr << "Assertion failed: Inorder traversal not sorted" << std::endl;
                return 1;
            }
        }

        if (tree_predecessor(inorderTraversalResult[0]).value() != nullptr) {
            std::cerr << "Assertion failed: First node should have no predecessor" << std::endl;
            return 1;
        }

        for (int j = 1; j < inorderTraversalResult.size(); ++j) {
            if (tree_predecessor(inorderTraversalResult[j]) != inorderTraversalResult[j - 1]) {
                std::cerr << "Assertion failed: Incorrect predecessor" << std::endl;
                return 1;
            }
        }

        if (tree_successor(inorderTraversalResult.back()) != nullptr) {
            std::cerr << "Assertion failed: Last node should have no successor" << std::endl;
            return 1;
        }

        for (int j = 0; j < inorderTraversalResult.size() - 1; ++j) {
            if (tree_successor(inorderTraversalResult[j]).value() != inorderTraversalResult[j + 1]) {
                std::cerr << "Assertion failed: Incorrect successor" << std::endl;
                return 1;
            }
        }
    }

    std::cout << "Test passed" << std::endl;
    return 0;
}