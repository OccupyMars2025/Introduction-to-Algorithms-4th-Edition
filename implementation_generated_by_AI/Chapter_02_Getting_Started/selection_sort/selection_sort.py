'''
book, page 56
'''

def selection_sort(A, n):
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
        
        
if __name__ == '__main__':
    import random
    import copy
    A = random.choices(range(10), k=20)
    original_A = copy.deepcopy(A)
    n = len(A)
    print(A)
    selection_sort(A, n)
    assert sorted(original_A) == A
    print(A)