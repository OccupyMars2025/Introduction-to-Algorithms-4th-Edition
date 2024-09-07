import random
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> List[int]:
    """
    recursive
    """
    if root is None:
        return []
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    return result



def inorder_traversal_v2(root: TreeNode) -> List[int]:
    """
    use stack, not recursive
    """
    if root is None:
        return []
    
    result = []
    stack = []
    current = root
    
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif len(stack) > 0:
            current = stack.pop()
            result.append(current.val)
            current = current.right
        else:
            break
    
    return result


def generate_random_binary_tree(max_depth: int=5, current_depth=0) -> TreeNode:
    if current_depth >= max_depth:
        return None
    
    val = random.randint(-100, 100)  # Random value between 1 and 100
    node = TreeNode(val)
    
    # Randomly decide whether to add left and right children
    if random.random() > 0.5:
        node.left = generate_random_binary_tree(max_depth, current_depth + 1)
    if random.random() > 0.5:
        node.right = generate_random_binary_tree(max_depth, current_depth + 1)
    
    return node



def print_binary_tree(root: TreeNode, level: int=0, prefix: str='Root: ') -> None:
    if root is None:
        return
    print(' ' * (level * 4) + prefix + str(root.val))
    
    if root.left:
        print_binary_tree(root.left, level + 1, 'L-- ')
    else:
        print(' ' * ((level + 1) * 4) + 'L-- None')
        
    if root.right:
        print_binary_tree(root.right, level + 1, 'R-- ')
    else:
        print(' ' * ((level + 1) * 4) + 'R-- None')




if __name__ == "__main__":
    for i in range(10000):
        tree_root = generate_random_binary_tree(max_depth=100, current_depth=0)

        # print_binary_tree(tree_root)

        result = inorder_traversal(tree_root)
        result_v2 = inorder_traversal_v2(tree_root)
        assert result == result_v2

