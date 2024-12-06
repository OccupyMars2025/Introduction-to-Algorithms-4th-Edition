from typing import List
from bisect import bisect_left

def longest_increasing_subsequence(sequence: List[int]) -> List[int]:
    if not sequence:
        return []

    # Array to store the smallest tail element of all increasing subsequences
    # with different lengths
    tail: List[int] = []
    # Array to help reconstruct the LIS by storing the previous index of each element
    prev_indices: List[int] = [-1] * len(sequence)
    # To store indices of elements in tail to help with the reconstruction
    lis_indices: List[int] = []

    for i, num in enumerate(sequence):
        # Find the position to insert num in the tail array using binary search
        pos: int = bisect_left(tail, num)

        # If pos is equal to the length of tail, it means num is larger than
        # all elements in tail, so we can extend the longest subsequence by 1
        if pos == len(tail):
            tail.append(num)
            # Update prev_indices to keep track of the previous element for reconstruction
            if lis_indices:
                prev_indices[i] = lis_indices[-1]
            lis_indices.append(i)
        else:
            # Replace the element at pos with num to maintain the smallest possible
            # tail element for subsequences of this length
            tail[pos] = num
            lis_indices[pos] = i
            # Update prev_indices if pos is greater than 0
            if pos > 0:
                prev_indices[i] = lis_indices[pos - 1]

    # Reconstruct the LIS from prev_indices and lis_indices
    lis: List[int] = []
    k: int = lis_indices[-1]  # Start from the last index in the LIS

    # Backtrack through prev_indices to build the LIS
    while k >= 0:
        lis.append(sequence[k])
        k = prev_indices[k]
    lis.reverse()  # The LIS is built backwards, so we reverse it

    return lis

# Example usage
sequence: List[int] = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Longest Increasing Subsequence:", longest_increasing_subsequence(sequence))
