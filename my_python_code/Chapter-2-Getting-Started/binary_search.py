from typing import List, Tuple, Optional, Union
import random


def binary_search_v1(a: List, value: Union[int, float]):
    """
    iterative version

    a: sorted array where the value is searched
    value:
    
    return: (found: bool, index: int)
    if found == True, then a[index] == value
    if found == False, then the value can be inserted before a[index]
    """
    low, high = 0, len(a) - 1
    middle = None
    while low <= high:
        middle = (low + high) // 2
        if a[middle] < value:
            low = middle + 1
        elif value < a[middle]:
            high = middle - 1
        else:
            return True, middle
    
    # the value is NOT found in the list
    # Caution: pay attention to the returned index
    if low == middle + 1:
        assert high == middle
        return False, low
    else:
        assert high == middle - 1
        assert low == middle
        return False, middle


def binary_search_v2(a: List, low: int, high: int, value: Union[int, float]):
    """
    recursive version

    a[low, high] is the sorted array where the value is searched
    :param a:
    :param low:
    :param high:
    :param value:
    :return: (found: bool, index: int)
    if found == True, then a[index] == value
    if found == False, then the value can be inserted before a[index]
    """
    # base case: low == high
    if low < high:
        middle = (low + high) // 2
        if a[middle] < value:
            # [middle+1, high]
            if middle == high:
                return False, middle + 1
            else:
                return binary_search_v2(a, middle+1, high, value)
        elif value < a[middle]:
            if middle == low:
                return False, middle
            else:
                return binary_search_v2(a, low, middle-1, value)
        else:
            return True, middle
    elif low == high:
        if value < a[low]:
            return False, low
        elif a[low] < value:
            return False, low + 1
        else:
            return True, low
    else:
        assert True, "Error: low > high"


def binary_search_v3(a: List, value: Union[int, float]):
    """
    iterative version

    :param a: the sorted array where the value is searched
    :param value:
    :return: if found, return the index,
        else return None
    """
    low, high = 0, len(a) - 1
    while low <= high:
        middle = (low + high) // 2
        if value < a[middle]:
            high = middle - 1
        elif a[middle] < value:
            low = middle + 1
        else:
            return middle
    return None


def binary_search_v4(a: List, low: int, high: int, value: Union[int, float]):
    """
    recursive version

    a[low, high] is the sorted array where the value is searched

    :param a:
    :param low:
    :param high:
    :param value:
    :return: if found, return the index,
        else return None
    """
    if low < high:
        middle = (low + high) // 2
        if value < a[middle]:
            return binary_search_v4(a, low, middle-1, value)
        elif a[middle] < value:
            return binary_search_v4(a, middle+1, high, value)
        else:
            return middle
    elif low == high:
        if value == a[low]:
            return low
        else:
            return None
    else:
        assert True, "Error, low > high"


def test_binary_search():
    """
    test binary search function which returns (found, index)
    :return: None
    """
    a = list()
    for n in range(1, 200):
        for i in range(n):
            a.append(random.randint(-100, 100))
        a = sorted(a)
        for e in a:
            # found, index = binary_search_v1(a, e)
            found, index = binary_search_v2(a, 0, len(a)-1, e)
            print("found, index, value: ", found, index, e)
            assert found and a[index] == e
        for _ in range(50):
            value = random.randint(-150, 150)
            # found, index = binary_search_v1(a, value)
            found, index = binary_search_v2(a, 0, len(a)-1, value)
            if found:
                assert a[index] == value
            else:
                print("Before insertion: ", a, sep='\n')
                print("found, index, value: ", found, index, value)
                a.insert(index, value)
                print("After insertion: ", a, sep='\n')
                for i in range(len(a) - 1):
                    assert a[i] <= a[i + 1], "{}".format(a)
                a.pop(index)
        a.clear()


def test_binary_search_v2():
    """
    test binary search function which returns index

    :return: None
    """
    a = list()
    for n in range(1, 20):
        for _ in range(n):
            a.append(random.randint(-100, 100))
        a = sorted(a)
        print(a)
        for i in range(len(a)):
            # index = binary_search_v3(a, a[i])
            index = binary_search_v4(a, 0, len(a)-1, a[i])
            assert a[i] == a[index]
        for _ in range(50):
            value = random.randint(-150, 150)
            # index = binary_search_v3(a, value)
            index = binary_search_v4(a, 0, len(a)-1, value)
            if index is None:
                assert value not in a
            else:
                assert a[index] == value
        a.clear()


if __name__ == "__main__":
    # test_binary_search()
    test_binary_search_v2()
