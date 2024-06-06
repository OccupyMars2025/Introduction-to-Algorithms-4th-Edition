from typing import List, Dict
from graphviz import Digraph # type: ignore

class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_string: bool = False

class RadixTree:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, string: str) -> None:
        node: TrieNode = self.root
        for char in string:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_string = True

    def lexicographic_sort(self) -> List[str]:
        result: List[str] = []
        self._pre_order_traversal(self.root, "", result)
        return result

    def _pre_order_traversal(self, node: TrieNode, prefix: str, result: List[str]) -> None:
        if node.is_end_of_string:
            result.append(prefix)
        for char in sorted(node.children.keys()):
            self._pre_order_traversal(node.children[char], prefix + char, result)

    def visualize(self, filename: str) -> None:
        """
        Generate a visual representation of the radix tree using graphviz.
        """
        dot = Digraph(comment='Radix Tree')
        dot.attr('node', shape='circle')
        self._add_edges(self.root, "", dot)
        
        # Configure the graph to be laid out from top to bottom
        dot.attr(rankdir='TB')
        dot.render(filename, format='png', view=True)

    def _add_edges(self, node: TrieNode, prefix: str, dot: Digraph) -> None:
        # for char, child in node.children.items():
        for char in sorted(node.children.keys()):
            child = node.children[char]
            child_prefix = prefix + char
            dot.node(child_prefix, label=child_prefix)
            dot.edge(prefix, child_prefix, label=char)
            self._add_edges(child, child_prefix, dot)
            if child.is_end_of_string:
                dot.node(child_prefix, label=child_prefix, style='filled', fillcolor='lightgrey')


# Example usage
if __name__ == "__main__":
    bit_strings: List[str] = ["1011", "10", "011", "100", "0"]
    radix_tree: RadixTree = RadixTree()
    for bit_string in bit_strings:
        radix_tree.insert(bit_string)

    sorted_strings: List[str] = radix_tree.lexicographic_sort()
    print(sorted_strings)  # Output: ['0', '011', '10', '100', '1011']

    # Visualize the radix tree
    radix_tree.visualize('./graphviz/radix_tree.dot')
    