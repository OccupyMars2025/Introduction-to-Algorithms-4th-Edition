"""
1. All the nodes in the binary search tree have distinct keys.
2. Each node x has an attribute x.succ , but no attribute x.parent.
"""

import random
from typing import List, Optional, Tuple
from graphviz import Digraph  # type: ignore

class TreeNode:
    def __init__(self, key: int):
        """
        Initialize a tree node.
        
        :param key: The key of the node
        """
        self.key: int = key
        self.left: Optional['TreeNode'] = None  # Left child
        self.right: Optional['TreeNode'] = None # Right child
        self.succ: Optional['TreeNode'] = None     # successor node

class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root: Optional[TreeNode] = None

    def transplant(self, u_parent: Optional[TreeNode], u: TreeNode, v: Optional[TreeNode]) -> None:
        """
        Replace the subtree rooted at node u with the subtree rooted at node v.
        
        :param u_parent: The parent of the node u
        :param u: The node to be replaced
        :param v: The node to replace u
        """
        if u_parent is None:
            self.root = v
            if v is not None:
                self.tree_maximum(v).succ = None
            return
        
        # Now u_parent is not None
        if v is None:
            if u_parent.left is u:
                u_parent.left = None
                u_subtree_predecessor = self.predecessor(self.tree_minimum(u))
                if u_subtree_predecessor is not None:
                    u_subtree_predecessor.succ = u_parent
            else:
                u_parent.right = None
                u_parent.succ = self.tree_maximum(u).succ   
            return
        
        # Now u_parent is not None and v is not None
        if u_parent.left is u:
            u_parent.left = v
            self.tree_maximum(v).succ = u_parent
            
            u_subtree_predecessor = self.predecessor(self.tree_minimum(u))
            if u_subtree_predecessor is not None:
                u_subtree_predecessor.succ = self.tree_minimum(v)
        else:
            u_parent.right = v
            u_parent.succ = self.tree_minimum(v)
            self.tree_maximum(v).succ = self.tree_maximum(u).succ

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

    def get_parent(self, x: TreeNode) -> Optional[TreeNode]:
        """
        Find the parent of the node x.
        
        :param x: The node whose parent is to be found
        :return: The parent of x
        """
        if self.root is None or self.root is x:
            return None
        current: Optional[TreeNode] = self.root
        while current is not None:
            if current.left is x or current.right is x:
                return current
            if x.key < current.key:
                current = current.left
            else:
                current = current.right
        return None
    
    def tree_delete(self, z: TreeNode) -> None:
        """
        Delete the node z from the binary search tree.
        
        :param z: The node to be deleted
        """
        q = self.get_parent(z)
        if z.left is None:
            self.transplant(q, z, z.right)
        elif z.right is None:
            self.transplant(q, z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_parent = self.get_parent(y)
            if y_parent is not z:
                self.transplant(y_parent, y, y.right)
                y.right = z.right
                # No need to update y.succ
            self.transplant(q, z, y)
            y.left = z.left
            self.tree_maximum(y.left).succ = y

    def insert(self, key: int) -> None:
        """
        Insert a node with the given key into the binary search tree.
        
        :param key: The key of the node to be inserted
        """
        z = TreeNode(key)
        if self.root is None:
            self.root = z
            return
        y: TreeNode = self.root
        x: Optional[TreeNode] = self.root

        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        if z.key < y.key:
            y_predecessor = self.predecessor(y)
            y.left = z
            z.succ = y
            if y_predecessor is not None:
                y_predecessor.succ = z
        else:
            y.right = z
            z.succ = y.succ
            y.succ = z


    def predecessor(self, x: TreeNode) -> Optional[TreeNode]:
        """
        Find the predecessor of the node x.
        
        :param x: The node whose predecessor is to be found
        :return: The predecessor of x
        """
        if x.left is not None:
            return self.tree_maximum(x.left)
        
        # x has no left child, the predecessor of x is the lowest ancestor of x whose right child is also an ancestor of x
        x_predecessor = None
        current = self.root
        while current is not None:
            if current.key < x.key:
                x_predecessor = current
                current = current.right
            elif current.key > x.key:
                current = current.left
            else:
                break
        return x_predecessor
        
    def inorder(self, node: Optional[TreeNode], collected_inorder_list : List[TreeNode]) -> None:
        """
        Print the inorder traversal of the binary search tree.
        
        :param node: The root of the subtree
        :param collected_inorder_list: The list to collect the inorder traversal
        """        
        if node is not None:
            self.inorder(node.left, collected_inorder_list)
            print(node.key, end=' ')
            collected_inorder_list.append(node)
            self.inorder(node.right, collected_inorder_list)            

    def generate_random_bst(self, n: int, key_range: Tuple[int, int]) -> None:
        """
        Generate a random binary search tree with n nodes with distinct keys.
        
        :param n: Number of nodes
        :param key_range: Tuple representing the range of keys (min, max)
        """
        keys = random.sample(range(*key_range), n)
        for key in keys:
            self.insert(key)
    
    def generate_random_bst_with_verbose_info(self, n: int, key_range: Tuple[int, int]) -> None:
        """
        Generate a random binary search tree with n nodes with distinct keys.
        But generate a picture of the structure of the BST after each insertion.
        
        :param n: Number of nodes
        :param key_range: Tuple representing the range of keys (min, max)
        """
        picture_id = 0
        
        # Visualize the BST
        self.visualize(picture_id=picture_id, label="empty BST", additional_info_to_path="insert")
        
        keys = random.sample(range(*key_range), n)
        for key in keys:
            self.insert(key)
            picture_id += 1
            self.visualize(picture_id=picture_id, label=f"After inserting key: {key}", additional_info_to_path="insert")
            # import time
            # time.sleep(1)

    def visualize(self, picture_id: int, label: str, additional_info_to_path: str) -> None:
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
                if node.succ is not None:
                    # dot.edge(str(node.key), str(node.succ.key), style='dotted', color='red', label='S')
                    dot.edge(str(node.key), str(node.succ.key), color='red')


        if self.root is not None:
            dot.node(str(self.root.key))
            add_edges(self.root)

        #         The line of code you're looking at is written in Python and it's using the `attr` method of a `dot` object.
        # `dot.attr(rankdir='TB')`: This line is setting an attribute of the `dot` object. The attribute being set is `rankdir`, and it's being set to `'TB'`.
        # The `dot` object is likely an instance of the `Digraph` or `Graph` class from the `graphviz` library, which is a Python interface for creating and rendering graph descriptions in the DOT language.
        # The `rankdir` attribute controls the direction of the graph layout. The value `'TB'` stands for "Top-Bottom", which means that the graph will be laid out from top to bottom. Other possible values for `rankdir` include `'LR'` for "Left-Right", `'BT'` for "Bottom-Top", and `'RL'` for "Right-Left".
        # So, in summary, this line of code is configuring the `dot` graph to be laid out from top to bottom.
        dot.attr(rankdir='TB')
        dot.render(f'./graphviz/bst_{additional_info_to_path}_{picture_id:03d}.dot', format='png', view=True)

    def test_the_structure(self):
        print("Inorder traversal of the BST:")
        if self.root is None:
            print("Empty tree")
            return
        collected_inorder_list :List[TreeNode] = []
        self.inorder(self.root, collected_inorder_list)
        print()
        for node in collected_inorder_list:
            print(f"{node.key},succ:{node.succ.key if node.succ is not None else None}", end=' ')
        print()
        
        collected_inorder_list_v2 :List[TreeNode] = []
        next_node: Optional[TreeNode] = self.tree_minimum(self.root)
        while next_node is not None:
            print(next_node.key, end=' ')
            collected_inorder_list_v2.append(next_node)
            next_node = next_node.succ
        print()
        assert len(collected_inorder_list) == len(collected_inorder_list_v2)
        for i in range(len(collected_inorder_list)):
            assert collected_inorder_list[i] is collected_inorder_list_v2[i]


def test():
    # Example usage
    bst = BinarySearchTree()

    # Generate a random BST with 15 nodes and keys in the range 1 to 100
    bst.generate_random_bst_with_verbose_info(15, (1, 100))

    # Test the structure of the BST
    bst.test_the_structure()
    
    collected_inorder_list :List[TreeNode] = []
    bst.inorder(bst.root, collected_inorder_list)
    print()
    
    picture_id = 0
    while collected_inorder_list:
        node = random.choice(collected_inorder_list)
        bst.tree_delete(node)
        collected_inorder_list.remove(node)
        print(f"After deleting {node.key}")
        bst.visualize(picture_id=picture_id, label=f"After deleting {node.key}", additional_info_to_path="delete")
        picture_id += 1
        bst.test_the_structure()
    assert bst.root is None  
        
if __name__ == "__main__":
    test()