
/*
Sure, here is the C++ implementation of the `TREE-INSERT` function from the provided pseudocode:


### Explanation

1. **Node Class**:
   - Represents a node in the binary search tree (BST).
   - Has attributes `key`, `left`, `right`, and `parent`.

2. **BinarySearchTree Class**:
   - Represents the BST itself.
   - Has an attribute `root` which is the root of the tree.

3. **tree_insert Method**:
   - Implements the `TREE-INSERT` algorithm from the pseudocode.
   - Inserts a node `z` into the BST.
   - Uses `y` as the trailing pointer to keep track of the parent of the new node `z`.
   - Traverses the tree starting from the root until it finds the correct position for `z`.
   - Updates the parent pointers and the left or right child pointers as necessary.

4. **inorder_traversal Method**:
   - Performs an in-order traversal of the BST and prints the keys in sorted order.

5. **main Function**:
   - Creates a BST and inserts nodes with given keys.
   - Performs an in-order traversal of the BST to display the keys in sorted order.
   - Cleans up the allocated nodes to prevent memory leaks.

This C++ implementation should work correctly and reflect the logic of the `TREE-INSERT` algorithm from the provided pseudocode.
*/

#include <iostream>
using namespace std;

class Node {
public:
    int key;
    Node* left;
    Node* right;
    Node* parent;

    Node(int key) : key(key), left(nullptr), right(nullptr), parent(nullptr) {}
};

class BinarySearchTree {
public:
    Node* root;

    BinarySearchTree() : root(nullptr) {}

    void tree_insert(Node* z) {
        Node* y = nullptr;
        Node* x = root;

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
            root = z; // Tree was empty
        } else if (z->key < y->key) {
            y->left = z;
        } else {
            y->right = z;
        }
    }

    void inorder_traversal(Node* node) {
        if (node != nullptr) {
            inorder_traversal(node->left);
            cout << node->key << " ";
            inorder_traversal(node->right);
        }
    }
};

int main() {
    BinarySearchTree bst;

    int keys[] = {15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9};
    Node* nodes[sizeof(keys)/sizeof(keys[0])];

    for (int i = 0; i < sizeof(keys)/sizeof(keys[0]); ++i) {
        nodes[i] = new Node(keys[i]);
        bst.tree_insert(nodes[i]);
    }

    cout << "Inorder traversal of the BST:" << endl;
    bst.inorder_traversal(bst.root);
    cout << endl;

    // Clean up allocated nodes
    for (int i = 0; i < sizeof(keys)/sizeof(keys[0]); ++i) {
        delete nodes[i];
    }

    return 0;
}
