
import random
from typing import Callable, List, Tuple


def test_search_method(search_method: Callable[[List, int], Tuple[bool, int]]):
    """

    Args:
        search_method(a: List, value: int) -> (found: bool, index: int)
            a: sorted array where the value is searched
            value:
            
            return: (found: bool, index: int)
            if found == True, then a[index] == value
            if found == False, then the value can be inserted before a[index] while still maintaining the sorted order
            
    """
    for n in range(1, 1000):
        sorted_list = sorted(random.choices(range(-100, 100), k=n))
        for elem in sorted_list:
            found, index = search_method(sorted_list, elem)
            assert ((found is True) and (sorted_list[index] == elem))
            
        for x in range(-200, 200):           
            found, index = search_method(sorted_list, x)
            if found:
                assert sorted_list[index] == x
            else:
                assert index >= 0 and index <= len(sorted_list)
                if index == 0:
                    assert sorted_list[index] > x
                elif index == len(sorted_list):
                    assert sorted_list[index - 1] < x
                else:
                    assert sorted_list[index - 1] < x and x < sorted_list[index]
    print(f'{search_method.__name__} passed all tests.')

