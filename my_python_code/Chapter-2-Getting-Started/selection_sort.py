from typing import List, Tuple, Optional, Union


def selection_sort(a: List):
    """

    :param a: the array to be sorted
    :return: None
    """
    length = len(a)
    for i in range(length - 1):
        smallest_value = a[i]
        index_of_smallest_value = i
        for j in range(i + 1, length):
            if a[j] < smallest_value:
                smallest_value = a[j]
                index_of_smallest_value = j
        if index_of_smallest_value != i:
            a[i], a[index_of_smallest_value] = a[index_of_smallest_value], a[i]


if __name__ == "__main__":
    a = [23, 42, -832, 1, 9, -3, 87, 3, 12, -34]
    print(a, len(a))
    selection_sort(a)
    print(a, len(a))
