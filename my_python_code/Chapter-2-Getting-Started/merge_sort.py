from typing import List, Tuple, Optional, Union
import random


def merge(a: List, start: int, middle: int, stop: int):
    """
    merge two sorted lists a[start, middle), a[middle, stop)
    into a sorted list a[start, stop)
    use sentinels
    :param a:
    :param start:
    :param middle:
    :param stop:
    :return:
    """
    left_list, right_list = [], []
    for e in a[start: middle]:
        left_list.append(e)
    left_list.append(float('inf'))
    for e in a[middle: stop]:
        right_list.append(e)
    right_list.append(float('inf'))

    i, j = 0, 0
    for k in range(start, stop):
        if left_list[i] < right_list[j]:
            a[k] = left_list[i]
            i += 1
        else:
            a[k] = right_list[j]
            j += 1


def merge_v2(a: List, start: int, middle: int, stop: int):
    """
    Merge two sorted lists a[start, middle), a[middle, stop)
    into a sorted list a[start, stop).
    Don't use sentinels.
    :param a:
    :param start:
    :param middle:
    :param stop:
    :return:
    """
    left_list, right_list = [], []
    for e in a[start: middle]:
        left_list.append(e)
    for e in a[middle: stop]:
        right_list.append(e)

    i, j, k = 0, 0, start
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
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
    middle = (start + stop) // 2
    merge_sort(a, start, middle)
    merge_sort(a, middle, stop)
    # merge(a, start, middle, stop)
    merge_v2(a, start, middle, stop)


if __name__ == "__main__":
    # n = int(input("How many elements: "))
    a = []
    for n in range(1, 100):
        for i in range(n):
            a.append(random.random() * 1000 -500)
        print(a)
        merge_sort(a, 0, len(a))
        print("After sorting:", a, sep='\n')
        for i in range(len(a) - 1):
            assert a[i] <= a[i + 1], "merge sort doesn't work correctly!"
        a.clear()
