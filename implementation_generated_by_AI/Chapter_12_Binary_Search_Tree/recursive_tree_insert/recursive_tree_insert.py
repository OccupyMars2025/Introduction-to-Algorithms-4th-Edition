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
        self.p: Optional['TreeNode'] = None     # Parent node

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
        if u.p is None:
            # u is the root node
            self.root = v
        elif u is u.p.left:
            # u is the left child of its parent
            u.p.left = v
        else:
            # u is the right child of its parent
            u.p.right = v
        if v is not None:
            # Set the parent of v to the parent of u
            v.p = u.p

    def tree_minimum(self, x: TreeNode) -> TreeNode:
        """
        Find the node with the minimum key in the subtree rooted at x.
        
        :param x: The root of the subtree
        :return: The node with the minimum key
        """
        while x.left is not None:
            x = x.left
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
            y = self.tree_minimum(z.right)
            if y.p != z:
                # y is not the right child of z
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            
        z.left = None
        z.right = None
        z.p = None

    def recursive_insert(self, parent: Optional[TreeNode], x: Optional[TreeNode], key: int) -> None:
        """
        Recursively insert a node with the given key into the binary search tree.
        parent and x cannot be None at the same time.
        
        :param parent: The parent of the current node
        :param x: The current node
        :param key: The key of the node to be inserted
        """
        if x is None:
            z = TreeNode(key)
            z.p = parent
            assert parent is not None
            if z.key < parent.key:
                parent.left = z
            else:
                parent.right = z
        elif key < x.key:
            self.recursive_insert(x, x.left, key)
        else:
            self.recursive_insert(x, x.right, key)
    
    
    def insert_v2(self, key: int) -> None:
        """
        Insert a node with the given key into the binary search tree.
        
        :param key: The key of the node to be inserted
        """
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self.recursive_insert(self.root.p, self.root, key)
        
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

        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def inorder(self, node: Optional[TreeNode]) -> List[TreeNode]:
        """
        Print the inorder traversal of the binary search tree.
        
        :param node: The root of the subtree
        """
        inorder_list : List[TreeNode]= []
        
        if node is not None:
            inorder_list.extend(self.inorder(node.left))
            print(node.key, end=' ')
            inorder_list.append(node)
            inorder_list.extend(self.inorder(node.right))
            
        return inorder_list

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
    # test recursive insertion
    bst = BinarySearchTree()
    keys = random.sample(range(100), 15)
    picture_id = 0
    bst.visualize(picture_id, 'Initial tree')
    for key in keys:
        bst.insert_v2(key)
        print(f'Inserting {key}')
        picture_id += 1
        import time
        time.sleep(1)
        bst.visualize(picture_id, f'After inserting {key}')


if __name__ == "__main__":
    test()