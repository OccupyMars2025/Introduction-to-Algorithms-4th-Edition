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
    a = random.choices(range(-10, 10), k=19)
    a_test = copy.deepcopy(a)
    print(a, len(a))
    insertion_sort(a)
    print(a, len(a))
    print(a_test, len(a_test))
    assert a == sorted(a_test)

    a2 = random.choices(range(-10, 10), k=1000)
    a2_test = copy.deepcopy(a2)
    insertion_sort_into_decreasing_order(a2)
    assert a2 == sorted(a2_test, reverse=True)