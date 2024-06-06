### Problem 12-2: Radix Trees

Given two strings \( a = a_0 a_1 \ldots a_p \) and \( b = b_0 b_1 \ldots b_q \), where each \( a_i \) and \( b_j \) belongs to some ordered set of characters, we say that string \( a \) is lexicographically less than string \( b \) if either:

1. There exists an integer \( j \), where \( 0 \le j \le \min \{p, q\} \), such that \( a_i = b_i \) for all \( i = 0, 1, \ldots, j-1 \) and \( a_j < b_j \), or
2. \( p < q \) and \( a_i = b_i \) for all \( i = 0, 1, \ldots, p \).

For example, if \( a \) and \( b \) are bit strings, then \( 10100 < 10110 \) by rule 1 (letting \( j = 3 \)) and \( 10100 < 101000 \) by rule 2. This ordering is similar to that used in English-language dictionaries.

### Radix Tree Description

The radix tree data structure shown in Figure 12.5 (also known as a trie) stores the bit strings \( 1011, 10, 011, 100, \) and \( 0 \). When searching for a key \( a = a_0 a_1 \ldots a_p \), go left at a node of depth \( i \) if \( a_i = 0 \) and right if \( a_i = 1 \). Let \( S \) be a set of distinct bit strings whose lengths sum to \( n \). Show how to use a radix tree to sort \( S \) lexicographically in \( \Theta(n) \) time. For the example in Figure 12.5, the output of the sort should be the sequence \( 0, 011, 10, 100, 1011 \).

### Solution:

To sort a set of bit strings \( S \) lexicographically using a radix tree, follow these steps:

1. **Construct the Radix Tree**: Insert each string from the set \( S \) into the radix tree.
2. **Perform a Lexicographic Traversal**: Perform an pre-order traversal of the radix tree to retrieve the strings in lexicographic order.

#### 1. Constructing the Radix Tree

Insert each string into the radix tree by following the bits of the string. If the bit is 0, go left; if the bit is 1, go right. Create nodes as needed.

#### 2. Lexicographic Traversal

A pre-order traversal of the radix tree will naturally visit the nodes in lexicographic order because:

- Parent nodes come before their children.
- Left child (0) comes before the right child (1) at each level of the tree.

### Pseudocode

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_string = False

class RadixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        node = self.root
        for char in string:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_string = True

    def lexicographic_sort(self):
        result = []
        self._in_order_traversal(self.root, "", result)
        return result

    def _in_order_traversal(self, node, prefix, result):
        if node.is_end_of_string:
            result.append(prefix)
        for char in sorted(node.children.keys()):
            self._in_order_traversal(node.children[char], prefix + char, result)

# Example usage
bit_strings = ["1011", "10", "011", "100", "0"]
radix_tree = RadixTree()
for bit_string in bit_strings:
    radix_tree.insert(bit_string)

sorted_strings = radix_tree.lexicographic_sort()
print(sorted_strings)  # Output: ['0', '011', '10', '100', '1011']
```

### Explanation:

- **Insertion**: The `insert` function inserts a string into the radix tree by iterating through its characters and creating child nodes as needed.
- **Lexicographic Sort**: The `lexicographic_sort` function performs an in-order traversal of the radix tree, accumulating the strings in lexicographic order.
- **In-order Traversal**: The `_in_order_traversal` helper function recursively traverses the tree, appending strings to the result list when a terminal node (`is_end_of_string`) is reached.

### Example with Bit Strings

For the bit strings `["1011", "10", "011", "100", "0"]`, the radix tree will be constructed as shown in Figure 12.5. The in-order traversal will yield the sorted order `["0", "011", "10", "100", "1011"]`.

By using the radix tree structure and performing an in-order traversal, we can sort the set of bit strings \( S \) lexicographically in \( \Theta(n) \) time, where \( n \) is the sum of the lengths of the strings in \( S \).