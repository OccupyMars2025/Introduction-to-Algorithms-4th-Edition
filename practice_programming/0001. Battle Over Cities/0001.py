"""

Here is a complete implementation in Python to solve the problem using Kruskal's algorithm for calculating the minimum spanning tree (MST) cost after simulating the conquest of each city.

### Explanation:

1. **Disjoint Set Union (DSU)**:
   - A class to manage the union-find structure, which helps in detecting the connectivity of components.

2. **Kruskal's Algorithm**:
   - A function to compute the MST cost using Kruskal's algorithm. It sorts edges by cost and adds them to the MST if they connect disjoint components.

3. **Main Logic**:
   - Parse the input and convert city numbers to zero-based for easier array management.
   - For each city, simulate its conquest by removing it and all connected edges.
   - Calculate the minimum repair cost to reconnect the remaining cities using Kruskal's algorithm.
   - Track the city that requires the maximum repair cost.

4. **Output**:
   - Print the cities that need the most attention in ascending order, or `0` if no repairs are needed.

To use this script, you need to provide the input in the specified format via standard input. This is typically done in a competitive programming environment or can be adapted for other uses.

"""

from typing import List, Tuple


class DisjointSetUnion:
    """
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    """
    def __init__(self, n: int):
        """

        Args:
            n (int): number of cities
        """
        self.parent = list(range(n))
        self.rank = [0] * n
    
    # def find(self, u: int):
    #     """
    #     Recursive version, the deep call stack may cause "Memory Limit Exceeded"
        
    #     Args:
    #         u (int): the id of a city,in the range [0, n-1]

    #     Returns:
    #         the root of the tree containing u
    #     """
    #     if self.parent[u] != u:
    #         self.parent[u] = self.find(self.parent[u])
    #     return self.parent[u]
    
    def find(self, u: int):
        """
        Iterative version
        
        Args:
            u (int): the id of a city,in the range [0, n-1]

        Returns:
            the root of the tree containing u
        """
        root = u
        while root != self.parent[root]:
            root = self.parent[root]
        while self.parent[u] != root:
            u, self.parent[u] = self.parent[u], root
        return root
    
    def union(self, u: int, v: int):
        """
        Merge the tree containing city u with the tree containing city v

        Args:
            u (int): the id of a city,in the range [0, n-1]
            v (int): the id of a city,in the range [0, n-1]
        """
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(n: int, edges: List[Tuple[int, int, int]]) -> Tuple[int, int]:
    """
    Finds the minimum spanning tree (MST) cost using Kruskal's algorithm.

    Args:
        n (int): The number of vertices in the graph.
        edges (List[Tuple[int, int, int]]): The list of edges in the graph, where each edge is represented as a tuple (u, v, cost).
        u and v are in the range [0, n-1], and cost is a non-negative integer.

    Returns:
        List[Tuple[int, int, int]]: all the edges of the minimum spanning forest (MSF) of the graph.
    """
    dsu = DisjointSetUnion(n)
    edges = sorted(edges, key=lambda x: x[2])
    edges_of_msf = []
    msf_edges = 0
    
    for u, v, cost in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            edges_of_msf.append((u, v, cost))
            msf_edges += 1
            if msf_edges == n - 1:
                break
    
    return edges_of_msf


def find_city_to_protect(n: int, m: int, highways: List[Tuple[int, int, int, int]]) -> List[int]:
    """
    Finds the critical cities that need to be protected in order to minimize the repair cost of highways.

    Args:
        n (int): The number of cities.
        m (int): The number of highways.
        highways (list): A list of tuples representing the highways. Each tuple contains four elements:
                         city1 (int): The first city connected by the highway.
                         city2 (int): The second city connected by the highway.
                         cost (int): The cost of repairing the highway.
                         status (int): The status of the highway (1 for existing, 0 for damaged).

    Returns:
        list: A list of critical cities that need to be protected. If no critical cities are found, returns [0].
    """
    original_edges = []
    for city1, city2, cost, status in highways:
        if status == 1:
            original_edges.append((city1 - 1, city2 - 1, cost))
    
    
    city_and_minimum_repair_cost : List[Tuple[int, int]] = []
    
    # If one of these cities is removed, the remaining graph will be disconnected even all destroyed highways are repaired
    essential_cities = []
    
    for city in range(n):
        filtered_edges = [(u, v, cost) for u, v, cost in original_edges if u != city and v != city]
        dsu = DisjointSetUnion(n)
        
        for u, v, cost in filtered_edges:
            dsu.union(u, v)
        
        components = len(set(dsu.find(i) for i in range(n) if i != city))
        
        if components == 1:
            # Even after removing the city, the graph remains connected
            continue
        
        repair_edges = [(city1 - 1, city2 - 1, cost) for city1, city2, cost, status in highways if status == 0 and city1 - 1 != city and city2 - 1 != city]
        edges_of_msf = kruskal(n, filtered_edges + repair_edges)
        if len(edges_of_msf) == n - 2:
            # After removing this city, the remaining graph can be connected after repairing some damaged highways
            if len(essential_cities) > 0:
                continue
            min_repair_cost = 0
            for edge in edges_of_msf:
                if edge in repair_edges:
                    min_repair_cost += edge[2]
            if min_repair_cost > 0:
                city_and_minimum_repair_cost.append((city, min_repair_cost))
        else:
            # After removing this city, the remaining graph will be disconnected even all destroyed highways are repaired
            essential_cities.append(city)
    
    if len(essential_cities) > 0:
        essential_cities = sorted(essential_cities)
        return [city + 1 for city in essential_cities]
    elif len(city_and_minimum_repair_cost) > 0:
        city_and_minimum_repair_cost = sorted(city_and_minimum_repair_cost, key=lambda x: x[1], reverse=True)
        critical_cities = []
        for item in city_and_minimum_repair_cost:
            if item[1] == city_and_minimum_repair_cost[0][1]:
                critical_cities.append(item[0])
            else:
                break
        critical_cities = sorted(critical_cities)
        return [city + 1 for city in critical_cities]
    else:
        return [0]

# Reading input
import sys
# test_case = """
# 4 5
# 1 2 1 1
# 1 3 1 1
# 2 3 1 0
# 2 4 1 1
# 3 4 1 0
# """
# data = test_case.split()

data = sys.stdin.read().split()
N = int(data[0])
M = int(data[1])
highways = []
index = 2
for _ in range(M):
    City1 = int(data[index]) # in the range [1, N]
    City2 = int(data[index + 1]) # in the range [1, N]
    Cost = int(data[index + 2])
    Status = int(data[index + 3])
    highways.append((City1, City2, Cost, Status))
    index += 4

# print(N, M, highways, sep="\n")

result = find_city_to_protect(N, M, highways)
print(" ".join(map(str, result)))
