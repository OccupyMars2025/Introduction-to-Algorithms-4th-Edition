from typing import List
import random

def counting_sort_not_stable(A: List[int], k: int) -> List[int]:
    """
    Counting sort algorithm.
    
    Each element in A is an integer in [0, k].
    
    Time complexity: O(n + k).
    Space complexity: O(n + k).
    """
    count = [0] * (k + 1)
    for a in A:
        count[a] += 1
    A_sorted = []
    for i, count_i in enumerate(count):
        for j in range(count_i):
            A_sorted.append(i)
    return A_sorted


def counting_sort_stable_version(A: List[int], k: int) -> List[int]:
    """
    Counting sort algorithm.
    
    Each element in A is an integer in [0, k].
    
    Time complexity: O(n + k).
    Space complexity: O(k).
    """
    count = [[] for _ in range(k + 1)]
    for a in A:
        count[a].append(a)
    A_sorted = []
    for i in range(len(count)):
        if count[i] != []:
            for a in count[i]:
                A_sorted.append(a)
    return A_sorted


def counting_sort_stable_version2(A: List[int], k: int) -> List[int]:
    """
    Counting sort algorithm.
    
    Each element in A is an integer in [0, k].
    
    Time complexity: O(n + k).
    Space complexity: O(k).
    """
    count = [0] * (k + 1)
    for a in A:
        count[a] += 1
    for i in range(1, k + 1):
        count[i] += count[i - 1]
    A_sorted = [None] * len(A)
    for i in range(len(A) - 1, -1, -1):
        a = A[i]
        count[a] -= 1
        A_sorted[count[a]] = a
    return A_sorted


def test_counting_sort():
    for k in range(1, 100):
        for n in range(1, 100):
            A = [random.randint(0, k) for _ in range(n)]
            # print("Input:", A)
            A_sorted = counting_sort_not_stable(A, k)
            # print("Output:", A_sorted)
            A_sorted_stable = counting_sort_stable_version(A, k)
            A_sorted_stable2 = counting_sort_stable_version2(A, k)
            assert A_sorted == sorted(A) and A_sorted_stable == sorted(A) and A_sorted_stable2 == sorted(A)
            
            
if __name__ == "__main__":
    test_counting_sort()


