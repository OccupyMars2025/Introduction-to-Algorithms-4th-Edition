"""
page 69, chapter 2, problem: 2-4 Inversions
Give an algorithm that determines the number of inversions in any permutation
on n distinct elements in theta(n*log(n)) worst-case time. 
(Hint: Modify merge sort.)


The core part: similar to merge sort, A and B are sorted lists, 
we need to count how many inversions between A and B.
that is how many (i, j) pairs such that A[i] > B[j]. 
All the inversions constitute a set S

Step 1:
when A[i] and B[j] are exposed, if A[i] > B[j], we execute:
inversions += len(A) - i, thus all the inversions we have counted 
constitute a set T.  It is clear that T is a subset of S.

Step 2:
For each element (i, j) in S, we know A[i] > B[j], 
so when we low to move B[j] to the merged list, 
A[i] must have NOT been moved to the merged list.
so (i, j) is in T. S is a subset of T.

Conclusion: S is T. Our calculation is correct and won't miss any inversion.
"""

from typing import List, Tuple, Optional, Union


def merge_inversions(a: List, low: int, middle: int, high: int):
    """
    Merge two sorted lists a[low, middle], a[middle+1, high-1]
    into a sorted list a[low, high-1].
    Don't use sentinels.
    
    :return: number of inversions between a[low, middle] and a[middle+1, high-1],
    that is, the number of (i, j) pairs such that a[i] > a[j], in which
    low <= i <= middle 
    middle+1 <= j <= high-1
    """
    num_inversions = 0
    left_list, right_list = [], []
    for e in a[low: middle+1]:
        left_list.append(e)
    for e in a[middle+1: high]:
        right_list.append(e)

    i, j, k = 0, 0, low
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            a[k] = left_list[i]
            i += 1
            k += 1
        elif left_list[i] > right_list[j]:
            # the core part
            num_inversions += len(left_list) - i
            a[k] = right_list[j]
            j += 1
            k += 1
        else:
            assert False, "should not reach here"

    while i < len(left_list):
        a[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        a[k] = right_list[j]
        j += 1
        k += 1

    return num_inversions


def count_inversions(a: List, low: int, high: int) -> int:
    """
    sort a[low, high), return the number of inversions in the original a[low, high)
    """
    if low >= high - 1:
        return 0
    num_inversions = 0
    middle = (low + high - 1) // 2
    num_inversions += count_inversions(a, low, middle + 1)
    num_inversions += count_inversions(a, middle + 1, high)
    num_inversions += merge_inversions(a, low, middle, high)
    
    return num_inversions


def count_inversions_brute_force(a: List, low: int, high: int) -> int:
    """
    return the number of inversions in a[low, high)
    """
    num_inversions = 0
    for i in range(low, high):
        for j in range(i+1, high):
            if a[i] > a[j]:
                num_inversions += 1
    return num_inversions


if __name__ == "__main__":
    import random
    import copy
    
    for n in range(1, 500):
        a = random.sample(range(10**6), n)
        a_copy = copy.deepcopy(a)
        num_inversions_1 = count_inversions_brute_force(a, 0, len(a))
        num_inversions_2 = count_inversions(a, 0, len(a))
        assert a == sorted(a_copy)
    print("All tests passed!")
