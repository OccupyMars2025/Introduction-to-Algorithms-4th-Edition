import random
from typing import List, Tuple


def bottom_up_cut_rod(p: List[int], n: int) -> Tuple[List[int], List[int]]:
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j//2 + 1):  # Attention: 1 <= i <= j//2
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        if q < p[j]:
            q = p[j]
            s[j] = j
        r[j] = q
    return r, s


def memoized_cut_rod(p: List[int], n: int) -> Tuple[List[int], List[int]]:
    r = [-1] * (n + 1)
    r[0] = 0
    s = [0] * (n + 1)
    memoized_cut_rod_aux(p, n, r, s)
    return r, s

def memoized_cut_rod_aux(p: List[int], n: int, r: List[int], s: List[int]) -> int:
    if r[n] >= 0:
        return r[n]
    if n == 0:
        s[0] = 0
        r[0] = 0
        # print(f"n: {n}, r: {r}")
        return 0
    else:
        q = float('-inf')
        best_first_cut = 0
        for i in range(1, n//2 + 1): # Attention: 1 <= i <= n//2
            if q < p[i] + memoized_cut_rod_aux(p, n - i, r, s):
                q = p[i] + memoized_cut_rod_aux(p, n - i, r, s)
                best_first_cut = i
        if q < p[n]:
            q = p[n]
            best_first_cut = n
        s[n] = best_first_cut
        r[n] = q
        return q
    
    
def test():
    # p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    for n in range(1, 100):
        p = random.choices(range(1, 1000), k=n)
        p.sort()
        p.insert(0, 0)
        # print(f"p: {p}")
        r1, s1 = bottom_up_cut_rod(p, n)
        r2, s2 = memoized_cut_rod(p, n)
        assert r1 == r2, f"r1: {r1} \nr2: {r2}"
        
        cut_off_pieces_v1 = []
        n1 = n
        while n1 > 0:
            cut_off_pieces_v1.append(s1[n1])
            n1 -= s1[n1]
        print(f"cut_off_pieces_v1: {cut_off_pieces_v1}")
        total_price_v1 = sum(p[i] for i in cut_off_pieces_v1)
        assert r1[n] == total_price_v1
            
        cut_off_pieces_v2 = []
        n2 = n
        while n2 > 0:
            cut_off_pieces_v2.append(s2[n2])
            n2 -= s2[n2]
        print(f"cut_off_pieces_v2: {cut_off_pieces_v2}")
        total_price_v2 = sum(p[i] for i in cut_off_pieces_v2)
        assert r2[n] == total_price_v2
        
        assert r1[n] == r2[n]
        
        print("Passed all tests!")
        
    
if __name__ == "__main__":
    test()