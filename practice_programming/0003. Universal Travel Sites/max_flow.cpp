/*
Sure, let's implement the solution in C++ using the Edmonds-Karp algorithm to find the maximum flow in a flow network.

### Implementation in C++

Here's the full implementation:


### Explanation:

1. **Reading Input**:
   - Read the source and destination planets, and the number of connections.
   - Use an `unordered_map` to map planet names to unique indices.
   - Store the edges (connections) in a `vector` of tuples.

2. **Graph Construction**:
   - Construct an adjacency matrix `graph` to represent the capacities between planets.
   - Convert planet names to their corresponding indices using the `unordered_map`.

3. **BFS Function**:
   - Perform BFS to find an augmenting path in the residual graph.
   - Update the `parent` vector to record the path.

4. **Edmonds-Karp Algorithm**:
   - Initialize the residual graph.
   - Use BFS to find augmenting paths and update the residual capacities.
   - Accumulate the maximum flow.

5. **Main Function**:
   - Read the input, build the graph, and call the `edmondsKarp` function.
   - Print the result.

### Running the Script:
To compile and run the script, save it as `max_flow.cpp` and use the following commands:

```sh
g++ -o max_flow max_flow.cpp
./max_flow < input.txt
```

Or you can provide the input directly in the terminal using echo and pipe:

```sh
echo "EAR MAR 11 EAR AAA 300 EAR BBB 400 AAA BBB 100 AAA CCC 400 AAA MAR 300 BBB DDD 400 AAA DDD 400 DDD AAA 100 CCC MAR 400 DDD CCC 200 DDD MAR 300" | ./max_flow
```

This will read the input, build the graph, compute the maximum flow, and print the minimum capacity required for the planet station.
*/

#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <string>
#include <unordered_map>

using namespace std;

// Function to perform BFS and find if there is a path from source to sink
bool bfs(vector<vector<int>>& residualGraph, int source, int sink, vector<int>& parent) {
    parent.clear();
    
    int V = residualGraph.size();
    vector<bool> visited(V, false);
    queue<int> q;
    q.push(source);
    visited[source] = true;
    parent[source] = -1;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v = 0; v < V; v++) {
            if (!visited[v] && residualGraph[u][v] > 0) {
                q.push(v);
                parent[v] = u;
                visited[v] = true;
                if (v == sink) {
                    return true;
                }
            }
        }
    }

    return false;
}

// Implementation of Edmonds-Karp algorithm for finding the maximum flow
int edmondsKarp(vector<vector<int>>& graph, int source, int sink) {
    int V = graph.size();
    vector<vector<int>> residualGraph(V, vector<int>(V));
    for (int u = 0; u < V; u++) {
        for (int v = 0; v < V; v++) {
            residualGraph[u][v] = graph[u][v];
        }
    }

    vector<int> parent(V);
    int maxFlow = 0;

    while (bfs(residualGraph, source, sink, parent)) {
        int pathFlow = INT_MAX;
        for (int v = sink; v != source; v = parent[v]) {
            int u = parent[v];
            pathFlow = min(pathFlow, residualGraph[u][v]);
        }

        for (int v = sink; v != source; v = parent[v]) {
            int u = parent[v];
            residualGraph[u][v] -= pathFlow;
            residualGraph[v][u] += pathFlow;
        }

        maxFlow += pathFlow;
    }

    return maxFlow;
}

int main() {
    string sourcePlanet, destinationPlanet;
    int N;
    cin >> sourcePlanet >> destinationPlanet >> N;

    // Mapping planet names to unique indices
    unordered_map<string, int> planetIndex;
    vector<tuple<string, string, int>> edges;

    int index = 0;
    for (int i = 0; i < N; i++) {
        string src, dest;
        int capacity;
        cin >> src >> dest >> capacity;

        if (planetIndex.find(src) == planetIndex.end()) {
            planetIndex[src] = index++;
        }
        if (planetIndex.find(dest) == planetIndex.end()) {
            planetIndex[dest] = index++;
        }

        edges.push_back(make_tuple(src, dest, capacity));
    }

    int V = planetIndex.size();
    // adjacency matrix to represent the capacities between planets
    vector<vector<int>> graph(V, vector<int>(V, 0));

    for (auto& [src, dest, capacity] : edges) {
        int u = planetIndex[src];
        int v = planetIndex[dest];
        graph[u][v] = capacity;
    }

    int source = planetIndex[sourcePlanet];
    int sink = planetIndex[destinationPlanet];

    int maxFlow = edmondsKarp(graph, source, sink);
    cout << maxFlow << endl;

    return 0;
}

