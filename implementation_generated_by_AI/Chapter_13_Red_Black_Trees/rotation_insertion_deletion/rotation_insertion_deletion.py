"""
Generating a random red-black tree requires creating a series of nodes and inserting them while maintaining the red-black tree properties. Here's a Python script to do this, including the insertion and balancing logic for a red-black tree:
"""

import random
from typing import List, Optional

import graphviz

class TreeNode:
    def __init__(self, key: int, color: str):
        self.key = key
        self.left: Optional['TreeNode'] = None # Left child # type: ignore
        self.right: Optional['TreeNode'] = None  # Right child # type: ignore
        self.p: Optional['TreeNode'] = None  # Parent node # type: ignore
        self.color: str = color  # New nodes are typically inserted as red

class RedBlackTree:
    def __init__(self):
        self.nil: TreeNode = TreeNode(0, 'BLACK')  # Sentinel node for leaf (NIL) nodes
        self.root: TreeNode = self.nil

    def to_graphviz(self, node: Optional[TreeNode] = None, graph: Optional[graphviz.Digraph] = None, label: str = '') -> graphviz.Digraph:
        if graph is None:
            graph = graphviz.Digraph()
            graph.attr('node', shape='circle')
            graph.attr('graph', label=label, labelloc='t')

        if node is None:
            node = self.root

        if node is not self.nil:
            node_label = f'{node.key}'
            graph.node(node_label, style='filled', fillcolor='red' if node.color == 'RED' else 'black', fontcolor='white' if node.color == 'BLACK' else 'black')
            if node.p is not self.nil:
                parent_label = f'{node.p.key}'
                graph.edge(node_label, parent_label, style='dashed', color='red')
            
            if node.left is not self.nil:
                left_label = f'{node.left.key}'
                graph.edge(node_label, left_label)
                self.to_graphviz(node.left, graph)

            if node.right is not self.nil:
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
        node = TreeNode(key, 'RED')
        node.left = self.nil
        node.right = self.nil

        y = self.nil
        x = self.root

        while x is not self.nil:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.p = y
        if y is self.nil:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        node.color = 'RED'
        self.insert_fixup(node)

    def insert_fixup(self, z: TreeNode) -> None:
        while z.p.color == 'RED':
            if z.p is z.p.p.left:
                y = z.p.p.right
                if y.color == 'RED':
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if z is z.p.right:
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
                    if z is z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.left_rotate(z.p.p)
        self.root.color = 'BLACK'

    def inorder_traversal(self, node: TreeNode, inorder_traversal_list: List) -> None:
        if node is not self.nil:
            self.inorder_traversal(node.left, inorder_traversal_list)
            print(f"{node.key},", end=" ")
            inorder_traversal_list.append(node)
            self.inorder_traversal(node.right, inorder_traversal_list)

    def transplant(self, u: TreeNode, v: TreeNode) -> None:
        if u.p is self.nil:
            self.root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def tree_minimum(self, node: TreeNode):
        while node.left is not self.nil:
            node = node.left
        return node

    def delete(self, z: TreeNode) -> None:
        y = z
        y_original_color = y.color
        if z.left is self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p is z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 'BLACK':
            self.delete_fixup(x)

    def delete_fixup(self, x: TreeNode) -> None:
        while x is not self.root and x.color == 'BLACK':
            if x is x.p.left:
                w = x.p.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.p.color = 'RED'
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.p
                else:
                    if w.right.color == 'BLACK':
                        w.left.color = 'BLACK'
                        w.color = 'RED'
                        self.right_rotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.p.color = 'RED'
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                    w.color = 'RED'
                    x = x.p
                else:
                    if w.left.color == 'BLACK':
                        w.right.color = 'BLACK'
                        w.color = 'RED'
                        self.left_rotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = 'BLACK'
                    w.left.color = 'BLACK'
                    self.right_rotate(x.p)
                    x = self.root
        x.color = 'BLACK'
    
    
def test() -> None:
    import time
    
    rb_tree = RedBlackTree()
    num_nodes = 10
    random_keys = random.sample(range(1, 100), num_nodes)
    # random_keys = [41, 38, 31, 12, 19, 8]
    picture_id: int = 0
    inorder_traversal_list: List[TreeNode] = []
    for key in random_keys:
        rb_tree.insert(key)
        graph = rb_tree.to_graphviz(label=f'After Inserting {key}')
        time.sleep(1)
        graph.render(f'./graphviz/red_black_tree_insertion_{picture_id: 03d}.dot', format='png', view=True, cleanup=True)
        picture_id += 1

        # print("Inorder Traversal of the Red-Black Tree:")
        inorder_traversal_list.clear()
        rb_tree.inorder_traversal(rb_tree.root, inorder_traversal_list)
        print()
        # check the list is sorted
        assert inorder_traversal_list == sorted(inorder_traversal_list, key=lambda x: x.key)    
    
    
    longest_inorder_traversal_list = inorder_traversal_list
    picture_id = 0
    # choose a random node to delete from the inorder traversal list
    while longest_inorder_traversal_list:
        random_index = random.randint(0, len(longest_inorder_traversal_list) - 1)
        random_node = longest_inorder_traversal_list[random_index]
        rb_tree.delete(random_node)
        longest_inorder_traversal_list.pop(random_index)
        
        graph = rb_tree.to_graphviz(label=f'After Deleting {random_node.key}')
        time.sleep(1)
        graph.render(f'./graphviz/red_black_tree_deletion_{picture_id: 03d}.dot', format='png', view=True, cleanup=True)
        picture_id += 1

        # print("Inorder Traversal of the Red-Black Tree:")
        inorder_traversal_list.clear()
        rb_tree.inorder_traversal(rb_tree.root, inorder_traversal_list)
        print()
        # check the list is sorted
        assert inorder_traversal_list == sorted(inorder_traversal_list, key=lambda x: x.key)
    


        
# Generate a random red-black tree
if __name__ == "__main__":
    test()