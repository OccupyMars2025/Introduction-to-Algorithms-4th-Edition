from typing import List, Tuple, Dict

def optimal_binary_search_tree(p: List[float], q: List[float]) -> Tuple[float, Dict[Tuple[int, int], int]]:
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
    return e[(1, n)], root
              