from typing import List, Tuple


def cut_rod_v1(p: List[int], n: int) -> int:
    """
    Recursive top-down implementation of rod cutting problem

    Args:
        p (List[int]): price table, p[0] is 0, p[i] is price of rod with length i, i = 0, 1, ..., n
        n (int): length of rod

    Returns:
        int: maximum obtainable revenue
    """
    if n <= 0:
        return 0
    q = float('-inf')
    for i in range(1, n + 1):
            q = max(q, p[i] + cut_rod_v1(p, n - i))
    return q

        
def memoized_cut_rod(p: List[int], n: int) -> int:
    r: List[int] = [float('-inf')] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p: List[int], n: int, r: List[int]) -> int:
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, len(p)):
            if i > n:
                break
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q


def bottom_up_cut_rod(p: List[int], n: int) -> int:
    r: List[int] = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, min(j + 1, len(p))):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]



def extended_bottom_up_cut_rod(p: List[int], n: int) -> Tuple[List[int], List[int]]:
    r: List[int] = [0] * (n + 1)
    s: List[int] = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, min(j + 1, len(p))):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s


def print_cut_rod_solution(p: List[int], n: int) -> None:
    r, s = extended_bottom_up_cut_rod(p, n)
    total_value = 0
    
    while n > 0:
        print(s[n], end=", ")
        total_value += p[s[n]]
        n = n - s[n]
    print()
    assert total_value == r[-1]
    
    


def test():
    # Example usage:
    # p is the price array where p[i] is the price of a rod of length i
    # For example, for a rod of length 4, the price array could be [1, 5, 8, 9]
    prices: List[int] = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    for length in range(1, 40):
        # max_value = cut_rod_v1(prices, length)
        max_value_v2 = memoized_cut_rod(prices, length)
        max_value_v3 = bottom_up_cut_rod(prices, length)
        r, s = extended_bottom_up_cut_rod(prices, length)
        # assert max_value == max_value_v2 
        assert max_value_v2 == max_value_v3
        assert max_value_v2 == r[length]
        print_cut_rod_solution(prices, length)
        print(f"Maximum obtainable value for rod of length {length: 3d} is {max_value_v2: 4d}")
        

if __name__ == "__main__":
    test()