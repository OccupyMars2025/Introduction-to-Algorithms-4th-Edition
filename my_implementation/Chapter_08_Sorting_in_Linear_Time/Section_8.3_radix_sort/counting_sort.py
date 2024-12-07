from typing import List

def counting_sort(arr: List[int], output: List[int]) -> None:
    """
    all elements in arr are integers in the range [0, max(arr)]
    """
    count = [0] * (max(arr) + 1)
    
    assert len(output) == len(arr)
    
    for num in arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # traverse the input in reverse order
    for i in range(len(arr)-1, -1, -1):
        count[arr[i]] -= 1
        output[count[arr[i]]] = arr[i]
        

def test_counting_sort():
    import random  
    for _ in range(100):
        arr = random.choices(range(100), k=random.randint(1, 200))
        output = [None] * len(arr)
        counting_sort(arr, output)
        print(output)
        assert sorted(arr) == output
        
if __name__ == "__main__":
    test_counting_sort()
        