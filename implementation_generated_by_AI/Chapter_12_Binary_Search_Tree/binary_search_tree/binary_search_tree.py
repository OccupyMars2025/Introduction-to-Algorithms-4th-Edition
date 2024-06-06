from typing import List, Optional
import random


class TreeNode:
    def __init__(self, key: int, left=None, right=None, parent=None) -> None:
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        
        
def tree_minimum(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root
    

def tree_maximum(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    while root.right is not None:
        root = root.right
    return root
    

def tree_successor(x: Optional[TreeNode]) -> Optional[TreeNode]:
    if x is None:
        return None
    
    if x.right is not None:
        return tree_minimum(x.right)
    else:
        node = x.parent
        while node is not None and x is node.right:
            x = node
            node = node.parent
        return node
    
    
def tree_predecessor(x: Optional[TreeNode]) -> Optional[TreeNode]:
    if x is None:
        return None
    
    if x.left is not None:
        return tree_maximum(x.left)
    else:
        node = x.parent
        while node is not None and x is node.left:
            x = node
            node = node.parent
        return node
    

def inorder_traversal(root: Optional[TreeNode]) -> Optional[List[TreeNode]]:
    if root is None:
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root)
    result.extend(inorder_traversal(root.right))
    
    return result


def print_binary_tree(root: Optional[TreeNode], indent="", last='updown'):
    if root is None:
        return 
    updown_prefix = "└── " if last == 'updown' else "├── "
    print(indent + updown_prefix + str(root.key))
    indent += "    " if last == 'updown' else "│   "
    children = [(root.left, 'left'), (root.right, 'right')]
    for i, (child, direction) in enumerate(children):
        last_direction = 'updown' if i == len(children) - 1 else 'right'
        print_binary_tree(child, indent, last_direction)


def tree_search(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if root is None or root.key == key:
        return root
    if key < root.key:
        return tree_search(root.left, key)
    else:
        return tree_search(root.right, key)
    
    
def iterative_tree_search(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    while root is not None and root.key != key:
        if key < root.key:
            root = root.left
        else:
            root = root.right
    return root
    
    
    
def generate_random_binary_search_tree(min_value: int, max_value: int) -> Optional[TreeNode]:
    if min_value > max_value:
        return None
    mid = random.randint(min_value, max_value)
    node = TreeNode(mid)
    
    if random.random() < 0.9:
        node.left = generate_random_binary_search_tree(min_value, mid - 1)
        if node.left is not None:
            node.left.parent = node
    else:
        node.left = None
        
    if random.random() < 0.9:
        node.right = generate_random_binary_search_tree(mid + 1, max_value)
        if node.right is not None:
            node.right.parent = node
    else:
        node.right = None
        
    return node



if __name__ == "__main__":
    for i in range(20000):
        tree_root = generate_random_binary_search_tree(-100, 100)
        inorder_traversal_result = inorder_traversal(tree_root)
        # print_binary_tree(tree_root)
        
        if len(inorder_traversal_result) == 0:
            assert False
        for i in range(len(inorder_traversal_result) - 1):
            assert inorder_traversal_result[i].key < inorder_traversal_result[i + 1].key
        
        assert tree_predecessor(inorder_traversal_result[0]) is None
        for i in range(1, len(inorder_traversal_result)):
            assert tree_predecessor(inorder_traversal_result[i]) is inorder_traversal_result[i - 1]
        
        assert tree_successor(inorder_traversal_result[-1]) is None
        for i in range(len(inorder_traversal_result) - 1):
            assert tree_successor(inorder_traversal_result[i]) is inorder_traversal_result[i + 1]
    print("Test passed")

# if __name__ == "__main__":
#     for i in range(2000):
#         tree_root = generate_random_binary_search_tree(-100, 100)
#         for key in range(-150, 150):
#             result = iterative_tree_search(tree_root, key)
#             result_2 = tree_search(tree_root, key)
#             if result is None:
#                 assert result_2 is None
#             else:
#                 assert result_2 is not None
#                 assert result.key == result_2.key
                
#             # if result is None:
#             #     print(f"Key {key} not found")
#             # else:
#             #     print(f"Key {key} found with node {result}")
