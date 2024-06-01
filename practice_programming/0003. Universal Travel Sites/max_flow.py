"""
keyword: graph, flow network, Ford-Fulkerson, Edmonds-Karp, BFS, finding the maximum flow in a flow network
https://en.wikipedia.org/wiki/Flow_network
https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm

To solve this problem, we need to find the minimum capacity of a planet station that allows every space vessel to dock and download its passengers on arrival, ensuring that the source planet can reach the destination planet. This is a classic example of finding the maximum flow in a flow network, which can be solved using algorithms like the Ford-Fulkerson method or Edmonds-Karp algorithm (a specific implementation of the Ford-Fulkerson method using BFS).

Here’s how to approach this problem using Python:

1. **Model the problem as a flow network**:
   - Each planet station is a node.
   - Each connection between stations is an edge with a capacity (maximum number of passengers).

2. **Use the Edmonds-Karp algorithm to find the maximum flow**:
   - Initialize a residual graph.
   - Use BFS to find augmenting paths.
   - Update the residual capacities of the edges and reverse edges.

### Implementation in Python


### Explanation:
1. **Reading Input**:
   - The input is read from standard input and split into a list of strings.
   - The source and destination planets and the number of connections are extracted.
   - The connections are read into a graph represented by a `defaultdict` of `defaultdicts` to store capacities.

2. **BFS Function**:
   - This function checks for an augmenting path in the residual graph and updates the parent map to record the path.

3. **Edmonds-Karp Algorithm**:
   - Initializes the residual graph.
   - Uses BFS to find augmenting paths and updates the residual capacities.
   - Accumulates the maximum flow.

4. **Main Function**:
   - Parses the input and builds the graph.
   - Calls `edmonds_karp` to find the maximum flow from the source to the destination.
   - Prints the result.

### Running the Script:
To run this script, save it as `max_flow.py` and provide the input through stdin:

```sh
python max_flow.py < input.txt
```

Or you can provide the input directly in the terminal using echo and pipe:

```sh
echo "EAR MAR 11 EAR AAA 300 EAR BBB 400 AAA BBB 100 AAA CCC 400 AAA MAR 300 BBB DDD 400 AAA DDD 400 DDD AAA 100 CCC MAR 400 DDD CCC 200 DDD MAR 300" | python max_flow.py
```

This will read the input, build the graph, compute the maximum flow, and print the minimum capacity required for the planet station.

"""


from collections import deque, defaultdict
from pprint import pprint
from typing import Dict

# Function to perform BFS and find if there is a path from source to sink
def bfs(residual_graph: Dict[str, Dict[str, int]], source: str, sink: str, parent: Dict[str, str]) -> bool:
    parent.clear()
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        
        for v, capacity in residual_graph[u].items():
            if v not in visited and capacity > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

# Implementation of Edmonds-Karp algorithm for finding the maximum flow
def edmonds_karp(graph: Dict[str, Dict[str, int]], source: str, sink: str) -> int:
    """
    The reverse edges are crucial for two reasons:
    1. Flow Adjustment: If in a future iteration, we find that pushing flow through a different path requires reducing the flow along a previously used path, the reverse edges allow us to do so.
    2. Correctness: They ensure the algorithm can correctly backtrack and reallocate flow to achieve the maximum flow in the network.

    Args:
        graph (Dict[str, Dict[str, int]]): _description_
        source (str): _description_
        sink (str): _description_

    Returns:
        _type_: _description_
    """
    residual_graph = defaultdict(lambda: defaultdict(int))
    
    for u in graph:
        for v, capacity in graph[u].items():
            residual_graph[u][v] = capacity
    
    # parent[s] = the parent of node s in the path from source to sink, used to trace the path from sink to source
    parent :Dict[str, str]= {}
    max_flow = 0
    
    while bfs(residual_graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]
        
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            #  These reverse edges represent the possibility to reduce the flow along an edge.
            residual_graph[v][u] += path_flow
            v = u
        
        max_flow += path_flow
    
    return max_flow

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    source_planet = data[0]
    destination_planet = data[1]
    N = int(data[2])
    
    #  adjacency lists to represent the graph
    graph = defaultdict(lambda: defaultdict(int))
    
    index = 3
    for _ in range(N):
        src = data[index]
        dest = data[index + 1]
        capacity = int(data[index + 2])
        graph[src][dest] += capacity
        index += 3
    
    # print(graph)
    # pprint(graph)

    # Calculate the maximum flow
    max_capacity = edmonds_karp(graph, source_planet, destination_planet)
    
    # Output the result
    print(max_capacity)

if __name__ == "__main__":
    main()

