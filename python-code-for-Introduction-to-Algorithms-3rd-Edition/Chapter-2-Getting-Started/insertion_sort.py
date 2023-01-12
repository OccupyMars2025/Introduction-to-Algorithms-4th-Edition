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
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


if __name__ == "__main__":
    a = [23, 42, -832, 1, 9, -3, 87, 3, 12, -34, 0]
    print(a, len(a))
    insertion_sort(a)
    print(a, len(a))