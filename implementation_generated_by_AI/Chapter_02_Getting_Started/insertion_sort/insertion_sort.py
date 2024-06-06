from typing import List, Tuple, Optional, Union


def insertion_sort(a: List):
    """

    :param a: array to be sorted
    :return:
    """
    length = len(a)
    for i in range(1, length):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


def insertion_sort_into_decreasing_order(a: List):
    """

    :param a: array to be sorted
    :return:
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


if __name__ == "__main__":
    import random
    import copy
    a = random.choices(range(-100, 100), k=19)
    a_test = copy.deepcopy(a)
    print(f"len={len(a)}: ", a)
    insertion_sort(a)
    print(f"len={len(a)}: ", a)    
    assert a == sorted(a_test)

    a2 = random.choices(range(-100, 100), k=100)
    a2_test = copy.deepcopy(a2)
    insertion_sort_into_decreasing_order(a2)
    print(f"len={len(a2)}: ", a2)
    assert a2 == sorted(a2_test, reverse=True)