from typing import List, Tuple, Optional, Union


def merge(a: List, start: int, middle: int, stop: int):
    """
    merge two sorted lists a[start, middle], a[middle + 1, stop-1]
    into a sorted list a[start, stop-1]
    use sentinels
    :param a:
    :param start:
    :param middle:
    :param stop:
    :return:
    """
    left_list, right_list = [], []
    for e in a[start: middle+1]:
        left_list.append(e)
    left_list.append(float('inf'))
    for e in a[middle+1: stop]:
        right_list.append(e)
    right_list.append(float('inf'))

    i, j = 0, 0
    for k in range(start, stop):
        if left_list[i] <= right_list[j]:
            a[k] = left_list[i]
            i += 1
        else:
            a[k] = right_list[j]
            j += 1


def merge_v2(a: List, start: int, middle: int, stop: int):
    """
    Merge two sorted lists a[start, middle], a[middle+1, stop-1]
    into a sorted list a[start, stop-1].
    Don't use sentinels.
    :param a:
    :param start:
    :param middle:
    :param stop:
    :return:
    """
    left_list, right_list = [], []
    for e in a[start: middle+1]:
        left_list.append(e)
    for e in a[middle+1: stop]:
        right_list.append(e)

    i, j, k = 0, 0, start
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            a[k] = left_list[i]
            i += 1
        else:
            a[k] = right_list[j]
            j += 1
        k += 1

    # Wrong: a[k-1] is not the last element of a,
    # you cannot use a.extend() here
    # if i < len(left_list):
    #     a.extend(left_list[i:])
    # if j < len(right_list):
    #     a.extend(right_list[j:])
    while i < len(left_list):
        a[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        a[k] = right_list[j]
        j += 1
        k += 1


def merge_sort(a: List, start: int, stop: int):
    """
    sort a[start, stop)
    :param a:
    :param start:
    :param stop:
    :return:
    """
    if start >= stop - 1:
        return
    middle = (start + stop - 1) // 2
    merge_sort(a, start, middle + 1)
    merge_sort(a, middle + 1, stop)
    # merge(a, start, middle, stop)
    merge_v2(a, start, middle, stop)


if __name__ == "__main__":
    import random
    import copy
    
    for n in range(1, 1000):
        a = random.choices(range(-100, 100), k=n)
        a_copy = copy.deepcopy(a)
        merge_sort(a, 0, len(a))
        assert a == sorted(a_copy)
    print("All tests passed!")
