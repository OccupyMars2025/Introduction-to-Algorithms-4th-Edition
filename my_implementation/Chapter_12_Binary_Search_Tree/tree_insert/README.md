In Python, the single quotes around `'Node'` in type annotations are used to specify a forward reference. This is necessary when the class being referenced is not yet fully defined at the point where it is used. In this case, the `Node` class is being defined, so the references to `Node` for the `left`, `right`, and `parent` attributes must use forward references.

### Detailed Explanation

Python type hints were introduced in PEP 484, and one of the features is forward references, which allow you to refer to classes that are not yet defined.

When you use `'Node'` as a type hint, you are telling the type checker that the actual type will be `Node` once it is fully defined. Without the quotes, Python would raise a `NameError` because it tries to resolve `Node` before the class definition is complete.

### Example without Quotes (This would cause an error)

```python
class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: Node = None  # This would cause a NameError
        self.right: Node = None  # This would cause a NameError
        self.parent: Node = None  # This would cause a NameError
```

### Example with Quotes (Correct)

```python
class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: 'Node' = None  # Forward reference
        self.right: 'Node' = None  # Forward reference
        self.parent: 'Node' = None  # Forward reference
```

In Python 3.7 and later, you can also enable forward references without quotes by using a feature from `__future__`:

### Example using `from __future__ import annotations`

```python
from __future__ import annotations

class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: Node = None  # Forward reference without quotes
        self.right: Node = None  # Forward reference without quotes
        self.parent: Node = None  # Forward reference without quotes
```

By importing `annotations` from `__future__`, all annotations are automatically treated as string literals, and forward references work without explicitly quoting them.

### Updated Python Implementation

Here's the updated implementation using `from __future__ import annotations` to avoid using quotes:

```python
from __future__ import annotations

class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None

class BinarySearchTree:
    def __init__(self):
        self.root: Node = None

    def tree_insert(self, z: Node):
        """Inserts node z into the BST."""
        y: Node = None
        x: Node = self.root

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

    def inorder_traversal(self, node: Node):
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
```

This approach maintains readability and avoids the need for quoting type annotations.