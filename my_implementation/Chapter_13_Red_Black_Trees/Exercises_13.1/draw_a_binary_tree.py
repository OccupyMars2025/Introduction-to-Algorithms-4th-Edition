import networkx as nx
from graphviz import Digraph

def build_tree():
    # Define the tree structure using networkx
    tree = nx.DiGraph()
    
    # Add nodes with labels and colors
    nodes = {
        8: '8B', 4: '4R', 12: '12R', 2: '2B', 6: '6B', 10: '10B', 14: '14B',
        1: '1B', 3: '3B', 5: '5B', 7: '7B', 9: '9B', 11: '11B', 13: '13B', 15: '15B'
    }
    
    # Add nodes to the graph
    for key in nodes:
        tree.add_node(key, label=nodes[key][:-1], color='red' if 'R' in nodes[key] else 'black')
    
    # Define edges
    edges = [
        (8, 4), (8, 12), (4, 2), (4, 6), (12, 10), (12, 14),
        (2, 1), (2, 3), (6, 5), (6, 7), (10, 9), (10, 11),
        (14, 13), (14, 15)
    ]
    
    # Add edges to the graph
    tree.add_edges_from(edges)
    
    return tree

def draw_binary_tree(tree):
    # Create a Digraph from the networkx graph
    dot = Digraph()
    
    # Add nodes and edges to the Digraph
    for node in tree.nodes(data=True):
        dot.node(str(node[0]), label=node[1]['label'], color=node[1]['color'], fontcolor=node[1]['color'])
    
    for edge in tree.edges():
        dot.edge(str(edge[0]), str(edge[1]))
    
    # Render and view the graph
    dot.render(filename='binary_tree', format='png', cleanup=True)
    dot.view()

# Build and draw the binary tree
tree = build_tree()
draw_binary_tree(tree)
