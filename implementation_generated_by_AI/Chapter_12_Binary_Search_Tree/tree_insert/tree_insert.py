from __future__ import annotations
from typing import Optional

class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None

class BinarySearchTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def tree_insert(self, z: Node) -> None:
        """Inserts node z into the BST."""
        y: Optional[Node] = None
        x: Optional[Node] = self.root

        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y is None:
            self.root = z  # Tree was empty
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def inorder_traversal(self, node: Optional[Node]) -> None:
        """Performs in-order traversal starting from the given node."""
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)

# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()

    keys = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
    nodes = [Node(key) for key in keys]

    for node in nodes:
        bst.tree_insert(node)

    print("Inorder traversal of the BST:")
    bst.inorder_traversal(bst.root)
    print()
