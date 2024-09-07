import random
from typing import Optional, List
import graphviz

class TreeNode:
    def __init__(self, key: int, color: str):
        self.key: int = key
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        self.color: str = color

class RedBlackTree:
    def __init__(self):
        self.nil: TreeNode = TreeNode(0, 'BLACK')  # Sentinel node
        self.root: TreeNode = self.nil

    def left_rotate(self, stack: List[TreeNode]) -> None:
        x: TreeNode = stack[-1]  # top of the stack
        y: TreeNode = x.right
        x.right = y.left
        y.left = x
        if len(stack) > 1:
            parent: TreeNode = stack[-2]
            if parent.left is x:
                parent.left = y
            else:
                parent.right = y
        else:
            self.root = y

    def right_rotate(self, stack: List[TreeNode]) -> None:
        y: TreeNode = stack[-1]  # top of the stack
        x: TreeNode = y.left
        y.left = x.right
        x.right = y
        if len(stack) > 1:
            parent: TreeNode = stack[-2]
            if parent.left is y:
                parent.left = x
            else:
                parent.right = x
        else:
            self.root = x

    def insert(self, key: int) -> None:
        node: TreeNode = TreeNode(key, 'RED')
        node.left = self.nil
        node.right = self.nil

        stack: List[TreeNode] = []
        y: TreeNode = self.nil
        x: TreeNode = self.root

        while x is not self.nil:
            y = x
            stack.append(x)
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        if y is self.nil:
            self.root = node
            node.color = 'BLACK'
            return
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        stack.append(node)
        self.insert_fixup(stack)

    def insert_fixup(self, stack: List[TreeNode]) -> None:
        while len(stack) >= 3 and stack[-2].color == 'RED':
            if stack[-2] is stack[-3].left:
                y: TreeNode = stack[-3].right
                if y.color == 'RED':
                    stack[-2].color = 'BLACK'
                    y.color = 'BLACK'
                    stack[-3].color = 'RED'
                    stack.pop()
                    stack.pop()
                else:
                    if stack[-1] is stack[-2].right:
                        self.left_rotate(stack[:-1])
                        stack[-1], stack[-2] = stack[-2], stack[-1]
                        
                    stack[-2].color = 'BLACK'
                    stack[-3].color = 'RED'
                    self.right_rotate(stack[:-2])
                    A = stack.pop()
                    B = stack.pop()
                    C = stack.pop()
                    stack.append(B)
                    # Caution: break the while loop
                    break
            else:
                y: TreeNode = stack[-3].left
                if y.color == 'RED':
                    stack[-2].color = 'BLACK'
                    y.color = 'BLACK'
                    stack[-3].color = 'RED'
                    stack.pop()
                    stack.pop()
                else:
                    if stack[-1] is stack[-2].left:
                        self.right_rotate(stack[:-1])
                        stack[-1], stack[-2] = stack[-2], stack[-1]
                    stack[-2].color = 'BLACK'
                    stack[-3].color = 'RED'
                    self.left_rotate(stack[:-2])
                    A = stack.pop()
                    B = stack.pop()
                    C = stack.pop()
                    stack.append(B)
                    # Caution: break the while loop
                    break
        self.root.color = 'BLACK'

    def inorder_traversal(self, node: TreeNode) -> None:
        if node != self.nil:
            self.inorder_traversal(node.left)
            print(f"({node.key}, {node.color})")
            self.inorder_traversal(node.right)

    def to_graphviz(self, node: Optional[TreeNode] = None, graph: Optional[graphviz.Digraph] = None, label: str = '') -> graphviz.Digraph:
        if graph is None:
            graph = graphviz.Digraph()
            # graph.attr('graph', label=label, labelloc='t', fontsize='20')
            graph.attr('graph', label=label, labelloc='t')
            graph.attr('node', shape='circle')

        if node is None:
            node = self.root

        if node != self.nil:
            node_label = f'{node.key}'
            graph.node(node_label, style='filled', fillcolor='red' if node.color == 'RED' else 'black', fontcolor='white' if node.color == 'BLACK' else 'black')
            
            if node.left != self.nil:
                left_label = f'{node.left.key}'
                graph.edge(node_label, left_label)
                self.to_graphviz(node.left, graph)

            if node.right != self.nil:
                right_label = f'{node.right.key}'
                graph.edge(node_label, right_label)
                self.to_graphviz(node.right, graph)

        return graph

# Generate a random red-black tree and visualize it using Graphviz
if __name__ == "__main__":
    import time
    
    rb_tree = RedBlackTree()
    num_nodes = 10
    random_keys = random.sample(range(1, 100), num_nodes)

    picture_id = 0
    for key in random_keys:
        rb_tree.insert(key)
        # Visualize the Red-Black Tree using Graphviz
        time.sleep(1)
        graph = rb_tree.to_graphviz(label=f'After inserting {key}')
        graph.render(f'./graphviz/red_black_tree_{picture_id: 03d}.dot', format='png', cleanup=True, view=True)
        picture_id += 1
        
    print("Inorder Traversal of the Red-Black Tree:")
    rb_tree.inorder_traversal(rb_tree.root)
