#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>
#include <cmath>
#include <stack>
#include <cassert>


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    // just for printing purposes
    int indent = 0;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};


/**
 * recursive inorder traversal
*/
std::vector<int> inorderTraversal(TreeNode* root) {
    if (root == nullptr) {
        return {};
    }
    
    std::vector<int> result;

    // Left subtree
    auto left = inorderTraversal(root->left);
    result.insert(result.end(), left.begin(), left.end());

    // Root node
    result.push_back(root->val);

    // Right subtree
    auto right = inorderTraversal(root->right);
    result.insert(result.end(), right.begin(), right.end());

    return result;
}


/**
 * use stack to implement inorder traversal
*/
std::vector<int> inorderTraversal_V2(TreeNode* root) {
    if (root == nullptr) {
        return {};
    }
    std::vector<int> result;
    std::stack<TreeNode*> s;

    TreeNode* current = root;
    while (true)
    {
        if (current)
        {
            s.push(current);
            current = current->left;
        } 
        else if (!s.empty())
        {
            current = s.top();
            result.push_back(current->val);
            s.pop();
            current = current->right;
        } else {
            break;
        }
    }
    
    return result;
}


TreeNode* generateRandomBinaryTree(int maxLevel, int currentLevel) {
    if (currentLevel >= maxLevel) {
        return nullptr;
    }
    TreeNode* root = new TreeNode(rand() % 100);
   
    if(rand() % 5 > 0)
        root->left = generateRandomBinaryTree(maxLevel, currentLevel + 1);
    else 
        root->left = nullptr;

    if(rand() % 5 > 0)
        root->right = generateRandomBinaryTree(maxLevel, currentLevel + 1);
    else 
        root->right = nullptr;

    return root;
}



/*
Function to print the binary tree in a visually appealing way.
Use level order traversal to gather nodes at each level.
*/ 
void printBinaryTree(TreeNode* root) {
    if (!root) return;

    // Level order traversal to gather nodes at each level
    std::queue<TreeNode*> q;
    q.push(root);

    int level = 0;
    int nodesInNextLevel = 0;

    while (true) {
        for (int i = 0; i < std::pow(2, level) - 1; ++i) {
            std::cout << " ";
        }

        for (int i = 0; i < std::pow(2, level); ++i) {
            TreeNode* node = q.front();
            q.pop();

            if (node) {
                std::cout << std::setw(4) << node->val << " ";
                q.push(node->left);
                q.push(node->right);
                if (node->left) ++nodesInNextLevel;
                if (node->right) ++nodesInNextLevel;
            } else {
                std::cout << "   ";
                q.push(nullptr);
                q.push(nullptr);
            }

            for (int j = 0; j < std::pow(2, level+1) - 1; ++j) {
                std::cout << " ";
            }
        }
        std::cout << std::endl;
        if (nodesInNextLevel == 0) break;
        nodesInNextLevel = 0;
        ++level;
    }
}

int main() {
    srand(time(nullptr));

    for(int i = 0; i < 100; ++i) {
        // Generate a random binary tree
        TreeNode* root = generateRandomBinaryTree(20, 0);

        // Perform inorder traversal and print the result
        auto result = inorderTraversal(root);
        auto result2 = inorderTraversal_V2(root);
        assert(result == result2);

        // for (auto& i : result) {
        //     std::cout << i << " ";
        // }
        // std::cout << std::endl;

        // // Print the binary tree
        // printBinaryTree(root);
    }

    return 0;
}
