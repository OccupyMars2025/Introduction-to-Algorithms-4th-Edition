"""
brute force solution: check every combination of the strings
"""

from pprint import pprint
from typing import Dict, List, Tuple

def count_beads(s: str) -> Dict[str, int]:
    """Helper function to count the frequency of each bead in a string."""
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def add_counts(count1: Dict[str, int], count2: Dict[str, int]) -> Dict[str, int]:
    """Helper function to add two bead counts together."""
    result = count1.copy()
    for char, count in count2.items():
        if char in result:
            result[char] += count
        else:
            result[char] = count
    return result

def count_extra_and_missing_beads(total_counts: Dict[str, int], required_counts: Dict[str, int]) -> Tuple[int, int]:
    """Helper function to count extra and missing beads compared to required beads."""
    extra_beads = 0
    for char, total in total_counts.items():
        required = required_counts.get(char, 0)
        extra_beads += max(0, total - required)
    missing_beads = 0
    for char, required in required_counts.items():
        missing_beads += max(0, required - total_counts.get(char, 0))
    return extra_beads, missing_beads


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    desired_string = data[0]
    N = int(data[1])
    shop_strings = data[2:]
    assert len(shop_strings) == N
    
    required_beads: Dict[str, int] = count_beads(desired_string)
    required_total = sum(required_beads.values())
    shop_bead_counts: List[Dict[str, int]] = [count_beads(s) for s in shop_strings]
    
    # {collected_beads_tuple: (extra_beads, missing_beads)}
    dp: Dict[Tuple[Tuple[str, int], ...], Tuple[int, int]] = {(): (0, required_total)}
    
    # brute force solution: check every combination of the strings
    for shop_beads in shop_bead_counts:
        new_dp = dp.copy()
        for collected_beads, (extra, missing) in dp.items():
            combined_beads = add_counts(dict(collected_beads), shop_beads)
            combined_beads_tuple = tuple(sorted(combined_beads.items()))
            combined_extra, combined_missing = count_extra_and_missing_beads(combined_beads, required_beads)            
            
            if combined_beads_tuple not in new_dp:
                new_dp[combined_beads_tuple] = (combined_extra, combined_missing)
        dp = new_dp
    
    min_extra = float('inf')
    min_missing = float('inf')
    for collected_beads, (extra, missing) in dp.items():
        if missing == 0:
            min_extra = min(min_extra, extra)
            min_missing = 0
        else:
            min_missing = min(min_missing, missing)
    
    # pprint(dp)
    if min_missing > 0:
        print(f"No {min_missing}")
    else:
        print(f"Yes {min_extra}")

if __name__ == "__main__":
    main()
