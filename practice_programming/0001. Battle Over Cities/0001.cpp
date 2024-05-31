#include <bits/stdc++.h>
using namespace std;

class DisjointSetUnion {
    vector<int> parent, rank;
public:
    DisjointSetUnion(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
    }

    // int find(int u) {
    //     if (u != parent[u]) {
    //         parent[u] = find(parent[u]);
    //     }
    //     return parent[u];
    // }

    // int find(int u) {
    //     int root = u;
    //     while (root != parent[root]) {
    //         root = parent[root];
    //     }
    //     while (parent[u] != root) {
    //         int next = parent[u];
    //         parent[u] = root;
    //         u = next;
    //     }
    //     return root;
    // }

    int find(int u) {
        while(u != parent[u]) {
            parent[u] = parent[parent[u]];
            u = parent[u];
        }

        return u;
    }

    void unionSet(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u != root_v) {
            if (rank[root_u] > rank[root_v]) {
                parent[root_v] = root_u;
            } else if (rank[root_u] < rank[root_v]) {
                parent[root_u] = root_v;
            } else {
                parent[root_v] = root_u;
                rank[root_u]++;
            }
        }
    }
};

/*
Actually, we don't need Kruskal's algorithm, we don't need to find the minimum spanning tree.
But the idea is similar to Kruskal's algorithm.
*/
// vector<tuple<int, int, int>> kruskal(int n, vector<tuple<int, int, int>>& edges) {
//     DisjointSetUnion dsu(n);
//     sort(edges.begin(), edges.end(), [](auto& a, auto& b) {
//         return get<2>(a) < get<2>(b);
//     });
//     vector<tuple<int, int, int>> edges_of_msf;
//     int msf_edges = 0;
//     for (auto& [u, v, cost] : edges) {
//         if (dsu.find(u) != dsu.find(v)) {
//             dsu.unionSet(u, v);
//             edges_of_msf.push_back({u, v, cost});
//             msf_edges++;
//             if (msf_edges == n - 1) {
//                 break;
//             }
//         }
//     }
//     return edges_of_msf;
// }



// Custom comparator for the priority queue to compare the third element of the tuple
struct CompareCost {
    bool operator()(tuple<int, int, int> const& t1, tuple<int, int, int> const& t2) {
        return get<2>(t1) > get<2>(t2);  // Min-heap: higher priority for smaller third element
    }
};


vector<int> find_city_to_protect(int n, vector<tuple<int, int, int, int>>& highways) {
    vector<tuple<int, int>> city_and_minimum_repair_cost;
    int max_of_all_min_repair_costs = 0;
    vector<int> essential_cities;

    vector<tuple<int, int, int>> existing_edges;
    // vector<tuple<int, int, int>> repair_edges;
    /*
    Use a priority queue for `repair_edges`:** Instead of sorting `repair_edges` every time, you could use a priority queue. This would keep the edges in sorted order as they're added, which could be more efficient if there are a lot of edges.
    priority_queue has no clear() method, so put it in the for loop
    */
    // Example priority queue using the custom comparator for a min-heap
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, CompareCost> repair_edges;



    int min_repair_cost = 0;
    int num_components = 0;
    set<int> components;
    for (int city = 0; city < n; ++city) {
        existing_edges.clear();
        // repair_edges.clear();
        for (auto& [u, v, cost, status] : highways) {
            if (u != city && v != city) {
                if (status == 1)
                    existing_edges.push_back({u, v, cost});
                else 
                    repair_edges.push({u, v, cost});
                    // repair_edges.push_back({u, v, cost});
            }
        }
        DisjointSetUnion dsu(n);
        for (auto& [u, v, cost] : existing_edges) {
            dsu.unionSet(u, v);
        }

        components.clear();
        for (int i = 0; i < n; ++i) {
            components.insert(dsu.find(i));
        }
        num_components = components.size();
        if (num_components == 2) {
            // After removing city, all other cities are still connected
            continue;
        }
        // --------------start: similar to Kruskal's algorithm ----------------
        min_repair_cost = 0;
        while(!repair_edges.empty()) {
            auto [u, v, cost] = repair_edges.top();
            repair_edges.pop();
            if(dsu.find(u) != dsu.find(v)) {
                dsu.unionSet(u, v);
                min_repair_cost += cost;
                num_components--;
                if(2 == num_components) {
                    break;
                }
            }
        }
        while (!repair_edges.empty()) {
            repair_edges.pop();
        }

        // sort(repair_edges.begin(), repair_edges.end(), [](auto& a, auto& b) {
        //     return get<2>(a) < get<2>(b);
        // });
        // for (auto& [u, v, cost] : repair_edges) {
        //     if(dsu.find(u) != dsu.find(v)) {
        //         dsu.unionSet(u, v);
        //         min_repair_cost += cost;
        //         num_components--;
        //         if(2 == num_components) {
        //             break;
        //         }
        //     }
        // }
        
        // --------------end: similar to Kruskal's algorithm ----------------

        if (num_components > 2) {
            // After removing city, some cities are still disconnected even after repairing all destroyed highways
            essential_cities.push_back(city);
        } else if (num_components == 2) {
            if (min_repair_cost >= max_of_all_min_repair_costs) {
                max_of_all_min_repair_costs = min_repair_cost;
                city_and_minimum_repair_cost.push_back({city, min_repair_cost});
            }
        } else {
            assert(0);
        }
    }

    if (!essential_cities.empty()) {
        return essential_cities;
    } else if (!city_and_minimum_repair_cost.empty()) {
        sort(city_and_minimum_repair_cost.begin(), city_and_minimum_repair_cost.end(), [](auto& a, auto& b) {
            return get<1>(a) > get<1>(b);
        });
        if(get<1>(city_and_minimum_repair_cost[0]) == 0) {
            return {-1};
        }
        vector<int> critical_cities;
        for (auto& [city, cost] : city_and_minimum_repair_cost) {
            if (cost == get<1>(city_and_minimum_repair_cost[0])) {
                critical_cities.push_back(city);
            } else {
                break;
            }
        }
        sort(critical_cities.begin(), critical_cities.end());
        return critical_cities;
    } else {
        return {-1};
    }
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<tuple<int, int, int, int>> highways(M);
    for (auto& [city1, city2, cost, status] : highways) {
        cin >> city1 >> city2 >> cost >> status;
        city1--;
        city2--;
    }
    auto result = find_city_to_protect(N, highways);
    for(size_t i = 0; i < result.size() - 1; i++) {
        cout << result[i] + 1 << " ";
    }
    cout << result[result.size() - 1] + 1;
    return 0;
}