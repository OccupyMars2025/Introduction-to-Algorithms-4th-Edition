"""
### Python Implementation of Counterexample

Here is a Python implementation to demonstrate the counterexample:

This script calculates and prints the maximum obtainable value using both the greedy and optimal (bottom-up dynamic programming) approaches, demonstrating the counterexample.
"""

from typing import List, Tuple

def greedy_cut_rod(p: List[int], n: int) -> Tuple[int, List[int]]:
    revenue = 0
    cut_off_pieces = []
    while n > 0:
        max_density = 0
        best_length = 0
        # Caution: len(p) can be much smaller than n
        for i in range(1, min(n + 1, len(p))):
            density = p[i] / i
            if density > max_density:
                max_density = density
                best_length = i
        revenue += p[best_length]
        cut_off_pieces.append(best_length)
        n -= best_length
    return revenue, cut_off_pieces


def bottom_up_cut_rod(p: List[int], n: int) -> Tuple[int, List[int]]:
    r: List[int] = [0] * (n + 1)
    first_cut: List[int] = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float('-inf')
        best_length = 0
        for i in range(1, min(j + 1, len(p))):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                best_length = i
        r[j] = q
        first_cut[j] = best_length
    
    cut_off_pieces = []
    while n > 0:
        cut_off_pieces.append(first_cut[n])
        n -= first_cut[n]
    return r[-1], cut_off_pieces


def main() -> None:
    # Example usage:
    prices: List[int] = [0, 1, 5, 8, 9]
    length_of_rod: int = 4
    max_revenue_greedy, cut_off_pieces_greedy = greedy_cut_rod(prices, length_of_rod)
    max_revenue_optimal, cut_off_pieces_optimal = bottom_up_cut_rod(prices, length_of_rod)    
    print("Maximum obtainable value (Greedy) is: ", max_revenue_greedy, " by cutting the rod into pieces of length ", cut_off_pieces_greedy)
    print("Maximum obtainable value (Optimal) is: ", max_revenue_optimal, " by cutting the rod into pieces of length ", cut_off_pieces_optimal)


if __name__ == "__main__":
    main()