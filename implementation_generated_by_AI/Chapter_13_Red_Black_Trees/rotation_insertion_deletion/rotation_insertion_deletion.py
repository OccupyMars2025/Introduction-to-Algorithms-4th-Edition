"""
Generating a random red-black tree requires creating a series of nodes and inserting them while maintaining the red-black tree properties. Here's a Python script to do this, including the insertion and balancing logic for a red-black tree:
"""

import random
from typing import Optional

import graphviz

class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional['TreeNode'] = None # Left child # type: ignore
        self.right: Optional['TreeNode'] = None  # Right child # type: ignore
        self.p: Optional['TreeNode'] = None  # Parent node # type: ignore
        self.color: str = 'RED'  # New nodes are typically inserted as red

class RedBlackTree:
    def __init__(self):
        self.nil: TreeNode = TreeNode(0)  # Sentinel node for leaf (NIL) nodes
        self.nil.color = 'BLACK'
        self.root: TreeNode = self.nil

    def to_graphviz(self, node: Optional[TreeNode] = None, graph: Optional[graphviz.Digraph] = None, label: str = '') -> graphviz.Digraph:
        if graph is None:
            graph = graphviz.Digraph()
            graph.attr('node', shape='circle')
            graph.attr('graph', label=label, labelloc='t')

        if node is None:
            node = self.root

        if node != self.nil:
            node_label = f'{node.key}'
            graph.node(node_label, style='filled', fillcolor='red' if node.color == 'RED' else 'black', fontcolor='white' if node.color == 'BLACK' else 'black')
            if node.p != self.nil:
                parent_label = f'{node.p.key}'
                graph.edge(node_label, parent_label, style='dashed', color='red')
            
            if node.left != self.nil:
                left_label = f'{node.left.key}'
                graph.edge(node_label, left_label)
                self.to_graphviz(node.left, graph)

            if node.right != self.nil:
                right_label = f'{node.right.key}'
                graph.edge(node_label, right_label)
                self.to_graphviz(node.right, graph)
                

        return graph
    
    def left_rotate(self, x: TreeNode) -> None:
        y = x.right  # Set y
        x.right = y.left  # Turn y's left subtree into x's right subtree
        if y.left is not self.nil:
            y.left.p = x  # Set y.left's parent to x
        y.p = x.p  # Set y's parent to x's parent
        if x.p is self.nil:
            self.root = y  # If x was the root, set y as the new root
        elif x is x.p.left:
            x.p.left = y  # If x was a left child, set y as the left child
        else:
            x.p.right = y  # If x was a right child, set y as the right child
        y.left = x  # Put x on y's left
        x.p = y  # Set x's parent to y

    def right_rotate(self, y: TreeNode) -> None:
        x: TreeNode = y.left  # set x
        y.left = x.right  # turn x's right subtree into y's left subtree
        # if x.right is not None:
        if x.right is not self.nil:
            x.right.p = y
        
        x.p = y.p  # link y's parent to x
        # if y.p is None:  # y is root
        if y.p is self.nil:  # y is root
            self.root = x
        elif y is y.p.left:
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
            print(f"({node.key}, {node.color})")
            self.inorder_traversal(node.right)

# Generate a random red-black tree
if __name__ == "__main__":
    import time
    
    rb_tree = RedBlackTree()
    # num_nodes = 10
    # random_keys = random.sample(range(1, 100), num_nodes)
    random_keys = [41, 38, 31, 12, 19, 8]
    picture_id: int = 0
    for key in random_keys:
        rb_tree.insert(key)
        graph = rb_tree.to_graphviz(label=f'After Inserting {key}')
        time.sleep(1)
        # graph.render(f'./graphviz/red_black_tree_{picture_id}.dot', format='png', cleanup=True)
        graph.render(f'./graphviz/red_black_tree_{picture_id}.dot', format='png', view=True)
        picture_id += 1

    print("Inorder Traversal of the Red-Black Tree:")
    rb_tree.inorder_traversal(rb_tree.root)
    


