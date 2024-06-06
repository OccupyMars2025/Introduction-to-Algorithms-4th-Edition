import random
from typing import List, Optional, Tuple
from graphviz import Digraph  # type: ignore

class TreeNode:
    def __init__(self, key: int):
        """
        Initialize a tree node.
        
        :param key: The key or value of the node
        """
        self.key: int = key
        self.left: Optional['TreeNode'] = None  # Left child
        self.right: Optional['TreeNode'] = None # Right child
        self.parent: Optional['TreeNode'] = None     # Parent node

class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root: Optional[TreeNode] = None

    def transplant(self, u: TreeNode, v: Optional[TreeNode]) -> None:
        """
        Replace the subtree rooted at node u with the subtree rooted at node v.
        
        :param u: The node to be replaced
        :param v: The node to replace u
        """
        if u.parent is None:
            # u is the root node
            self.root = v
        elif u is u.parent.left:
            # u is the left child of its parent
            u.parent.left = v
        else:
            # u is the right child of its parent
            u.parent.right = v
        if v is not None:
            # Set the parent of v to the parent of u
            v.parent = u.parent

    def tree_minimum(self, x: TreeNode) -> TreeNode:
        """
        Find the node with the minimum key in the subtree rooted at x.
        
        :param x: The root of the subtree
        :return: The node with the minimum key
        """
        while x.left is not None:
            x = x.left
        return x
    
    def tree_maximum(self, x: TreeNode) -> TreeNode:
        """
        Find the node with the maximum key in the subtree rooted at x.
        
        :param x: The root of the subtree
        :return: The node with the maximum key
        """
        while x.right is not None:
            x = x.right
        return x

    def tree_delete(self, z: TreeNode) -> None:
        """
        Delete the node z from the binary search tree.
        
        :param z: The node to be deleted
        """
        if z.left is None:
            # z has no left child
            self.transplant(z, z.right)
        elif z.right is None:
            # z has no right child
            self.transplant(z, z.left)
        else:
            # z has two children
            # select one from the predecessor or the successor randomly
            if random.randint(0, 1) == 0:
                # choose y as the successor of z
                y = self.tree_minimum(z.right)
                if y.parent != z:
                    # y is not the right child of z
                    self.transplant(y, y.right)
                    y.right = z.right
                    y.right.parent = y
                self.transplant(z, y)
                y.left = z.left
                y.left.parent = y
            else:
                # choose y as the predecessor of z
                y = self.tree_maximum(z.left)
                if y.parent != z:
                    # y is not the left child of z
                    self.transplant(y, y.left)
                    y.left = z.left
                    y.left.parent = y
                self.transplant(z, y)
                y.right = z.right
                y.right.parent = y

    def insert(self, key: int) -> None:
        """
        Insert a node with the given key into the binary search tree.
        
        :param key: The key of the node to be inserted
        """
        z = TreeNode(key)
        y: Optional[TreeNode] = None
        x: Optional[TreeNode] = self.root

        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def inorder(self, node: Optional[TreeNode], inorder_list : List[TreeNode]) -> None:
        """
        Print the inorder traversal of the binary search tree.
        
        :param node: The root of the subtree
        :param inorder_list: The list to store the inorder traversal
        """
        if node is not None:
            self.inorder(node.left, inorder_list)
            print(node.key, end=' ')
            inorder_list.append(node)
            self.inorder(node.right, inorder_list)
                        
    def generate_random_bst(self, n: int, key_range: Tuple[int, int]) -> None:
        """
        Generate a random binary search tree with n nodes with distinct keys.
        
        :param n: Number of nodes
        :param key_range: Tuple representing the range of keys (min, max)
        """
        keys = random.sample(range(*key_range), n)
        for key in keys:
            self.insert(key)

    def visualize(self, picture_id: int, label: str) -> None:
        """
        Generate a visual representation of the binary search tree.
        """
        dot = Digraph(comment='Binary Search Tree')
        dot.attr('node', shape='circle')
        dot.attr('graph', label=label, labelloc='top')
        
        def add_edges(node: Optional[TreeNode]) -> None:
            if node is not None:
                if node.left is not None:
                    dot.edge(str(node.key), str(node.left.key), label='L')
                    add_edges(node.left)
                if node.right is not None:
                    dot.edge(str(node.key), str(node.right.key), label='R')
                    add_edges(node.right)

        if self.root is not None:
            dot.node(str(self.root.key))
            add_edges(self.root)

        dot.attr(rankdir='TB')
        dot.render(f'./graphviz/bst_{picture_id:03d}.dot', format='png', view=True)


def test():
    # Example usage
    bst = BinarySearchTree()

    # Generate a random BST with 15 nodes and keys in the range 1 to 100
    bst.generate_random_bst(15, (1, 100))

    print("Inorder traversal of the random BST:")
    inorder_list :List[TreeNode] = []
    bst.inorder(bst.root, inorder_list)
    print()
    for node in inorder_list:
        print(node.key, end=' ')
    print()

    # Visualize the BST
    picture_id = 0
    bst.visualize(picture_id=picture_id, label="original BST")
    
    while inorder_list:
        # pop the node from the inorder list randomly
        node = inorder_list.pop(random.randint(0, len(inorder_list) - 1))
        print(f"Deleting node with key {node.key}")
        bst.tree_delete(node)
        
        # sleep a bit to see the visualization
        picture_id += 1
        # import time
        # time.sleep(1)
        bst.visualize(picture_id=picture_id, label=f"after deleting {node.key}")
        
        inorder_list_v2 :List[TreeNode] = []
        bst.inorder(bst.root, inorder_list_v2)
        print()
        assert len(inorder_list) == len(inorder_list_v2)
        for i in range(len(inorder_list)):
            assert inorder_list[i] is inorder_list_v2[i]
    
    print("All tests passed!")

if __name__ == "__main__":
    test()