import copy
from typing import List, Tuple, Optional, Union, Callable
import random
from ...utils.test_methods import test_search_method


def binary_search(a: List, value: int):
    """
    iterative version

    a: sorted array where the value is searched
    value:
    
    return: (found: bool, index: int)
    if found == True, then a[index] == value
    if found == False, then the value can be inserted before a[index]
    
    Let's find out which index to return if the value is NOT in the list
    
    Part 1:
    First, you can find that the while loop is NOT infinite.
        
        
    Part 2:
    In the last time the while loop body executes:
    if case 1 happens:
        low - 1 <= high
    if case 2 happens:
        high + 1 >= low
    thus for the 2 cases, we both have  low <= high + 1
    when we exit the while loop, low > high
    so when we exit the while loop, we have:  low = high + 1
    
    
    Part 3: When we exit the while loop:
    if only case 1 has happened:
        "low" is continuously updated to "middle + 1", "high" is not updated at all
        a[low - 1] < value
        => a[high] < value
        we should return "high + 1", that is "low"
    if only case 2 has happened:
        "high" is continuously updated to "middle - 1", "low" is not updated at all
        value < a[high + 1]
        => value < a[low]
        we should return "low"
    Conclusion: when the value is NOT in the list, we should return "low"
    """
    low, high = 0, len(a) - 1
    middle = None
    while low <= high:
        middle = (low + high) // 2
        if a[middle] < value:  
            low = middle + 1    # case 1
        elif value < a[middle]: 
            high = middle - 1   # case 2
        else:
            return True, middle
    
    # the value is NOT found in the list
    # Caution: pay attention to the returned index
    return False, low

def is_sorted(a: List):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


if __name__ == '__main__':
    test_search_method(binary_search)

    