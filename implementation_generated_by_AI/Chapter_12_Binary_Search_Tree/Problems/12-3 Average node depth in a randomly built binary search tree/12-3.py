import random
from typing import List

def quicksort(arr: List[int], left: int, right: int) -> None:
    """
    Sort the array using the quicksort algorithm.
    :param arr: the array to be sorted
    :param left: the left index of the array, inclusive
    :param right: the right index of the array, inclusive
    """
    if left >= right:
        return

    pivot = arr[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    quicksort(arr, left, j - 1)
    quicksort(arr, j + 1, right)


def main() -> None:
    min_value = 0
    max_value = 100

    for n in range(1, 1001):
        random_vector = random.choices(range(min_value, max_value + 1), k=n)
        quicksort(random_vector, 0, len(random_vector) - 1)

        if not all(random_vector[i] <= random_vector[i + 1] for i in range(len(random_vector) - 1)):
            print("Error: The array is not sorted.")
            exit(1)

    print("All tests passed.")

if __name__ == "__main__":
    main()
