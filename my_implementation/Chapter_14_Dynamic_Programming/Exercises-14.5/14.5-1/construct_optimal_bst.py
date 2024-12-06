from typing import List, Tuple, Dict

def optimal_binary_search_tree(p: List[float], q: List[float]) -> Tuple[Dict[Tuple[int, int], float], Dict[Tuple[int, int], int]]:
    n = len(p)
    assert len(p) + 1 == len(q)
    
    e, w = dict(), dict()
    root = dict()
    for i in range(1, n+2):
        e[(i, i-1)] = w[(i, i-1)] = q[i-1]
    for length in range(1, n+1):
        for i in range(1, n-length+2):
            j = i + length - 1
            w[(i, j)] = p[j-1] + q[j] + w[(i, j-1)]
            e[(i, j)] = float('inf')
            for r in range(i, j+1): 
                temp = e[(i, r-1)] + e[(r+1, j)] 
                if temp < e[(i, j)]:
                    e[(i, j)] = temp
                    root[(i, j)] = r
            e[(i, j)] += w[(i, j)]
    return e, root
              
              
def construct_optimal_bst(root: Dict[Tuple[int, int], int], i: int, j: int):
    # if i == j + 1:
    #     return "d" + str(i - 1)  # External node (dummy key)
    if i > j:
        return
    r = root[(i, j)]  # Get the root of the subtree
    print(f"k{r} is the root of subtree [{i}, {j}]")
    
    if i == j:
        return 
    construct_optimal_bst(root, i, r - 1)
    construct_optimal_bst(root, r + 1, j)
    
    
    
if __name__ == '__main__':
    # 14.5-1
    p = [0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    
    # # 14.5-2
    # p = [0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
    # q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]
    assert sum(p) + sum(q) == 1.0
    cost, root = optimal_binary_search_tree(p, q)
    print("Cost of Optimal BST is", cost[(1, len(p))])
    construct_optimal_bst(root, 1, len(p))
    print("cost:")
    print(cost)
    print("root:")
    print(root)