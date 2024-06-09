"""
Generating a random red-black tree requires creating a series of nodes and inserting them while maintaining the red-black tree properties. Here's a Python script to do this, including the insertion and balancing logic for a red-black tree:
"""

import random

class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left: 'TreeNode' = None
        self.right: 'TreeNode' = None
        self.p: 'TreeNode' = None  # Parent node
        self.color: str = 'RED'  # New nodes are typically inserted as red

class RedBlackTree:
    def __init__(self):
        self.nil: TreeNode = TreeNode(0)  # Sentinel node for leaf (NIL) nodes
        self.nil.color = 'BLACK'
        self.root: TreeNode = self.nil

    def left_rotate(self, x: TreeNode) -> None:
        y = x.right  # Set y
        x.right = y.left  # Turn y's left subtree into x's right subtree
        if y.left != self.nil:
            y.left.p = x  # Set y.left's parent to x
        y.p = x.p  # Set y's parent to x's parent
        if x.p == self.nil:
            self.root = y  # If x was the root, set y as the new root
        elif x == x.p.left:
            x.p.left = y  # If x was a left child, set y as the left child
        else:
            x.p.right = y  # If x was a right child, set y as the right child
        y.left = x  # Put x on y's left
        x.p = y  # Set x's parent to y

    def right_rotate(self, y: TreeNode) -> None:
        x: TreeNode = y.left  # set x
        y.left = x.right  # turn x's right subtree into y's left subtree
        if x.right is not None:
            x.right.p = y
        
        x.p = y.p  # link y's parent to x
        if y.p is None:  # y is root
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        
        x.right = y  # put y on x's right
        y.p = x
    
    def insert(self, key: int) -> None:
        node = TreeNode(key)
        node.left = self.nil
        node.right = self.nil

        y = self.nil
        x = self.root

        while x != self.nil:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.p = y
        if y == self.nil:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        node.color = 'RED'
        self.insert_fixup(node)

    def insert_fixup(self, z: TreeNode) -> None:
        while z.p.color == 'RED':
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 'RED':
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == 'RED':
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.left_rotate(z.p.p)
        self.root.color = 'BLACK'

    def inorder_traversal(self, node: TreeNode) -> None:
        if node != self.nil:
            self.inorder_traversal(node.left)
            print(f"Node: {node.key}, Color: {node.color}")
            self.inorder_traversal(node.right)

# Generate a random red-black tree
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    num_nodes = 10
    random_keys = random.sample(range(1, 100), num_nodes)

    for key in random_keys:
        rb_tree.insert(key)

    print("Inorder Traversal of the Red-Black Tree:")
    rb_tree.inorder_traversal(rb_tree.root)

