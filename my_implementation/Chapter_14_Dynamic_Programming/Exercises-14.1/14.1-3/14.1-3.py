from typing import List, Tuple

def cut_rod_with_cost(p: List[int], n: int, c: int) -> Tuple[int, List[int]]:
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float('-inf')
        longest_piece = min(j, len(p)-1)
        for i in range(1, longest_piece):
            if q < p[i] + r[j - i] - c:
                q = p[i] + r[j - i] - c
                s[j] = i
        if longest_piece < j:
            if q < p[longest_piece] + r[j - longest_piece] - c:
                q = p[longest_piece] + r[j - longest_piece] - c
                s[j] = longest_piece
        elif longest_piece == j:
            if q < p[j]:
                q = p[j]
                s[j] = j
        r[j] = q
        
    cut_off_pieces = []
    while n > 0:
        cut_off_pieces.append(s[n])
        n -= s[n]
    return r[-1], cut_off_pieces


def main():
    p = [0, 1, 5, 8, 9, 10, 17, 18, 20, 24, 30]
    n = 20
    c = 1
    max_revenue, cut_off_pieces = cut_rod_with_cost(p, n, c)
    print(f"Max revenue: {max_revenue}")
    print(f"Cut off pieces: {cut_off_pieces}")
    
    
if __name__ == "__main__":
    main()