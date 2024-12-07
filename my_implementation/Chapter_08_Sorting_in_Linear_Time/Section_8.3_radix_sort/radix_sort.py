from typing import List

# Function to get the digit at a specific position (exp)
def get_digit(num: int, exp: int) -> int:
    return (num // exp) % 10

# Function to perform counting sort based on the digit represented by exp
def counting_sort(arr: List[int], exp: int, output: List[int]) -> None:
    n: int = len(arr)
    count: List[int] = [0] * 10
    assert len(output) == n
    
    # Count occurrences of digits at the current place value (exp)
    for num in arr:
        index: int = get_digit(num, exp)
        count[index] += 1
    
    # Calculate the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Place the numbers in sorted order based on the current digit
    for i in range(n - 1, -1, -1):
        num: int = arr[i]
        index: int = get_digit(num, exp)
        count[index] -= 1
        output[count[index]] = num
    

# Main function to implement Radix Sort
def radix_sort(arr: List[int]) -> List[int]:
    # Find the maximum number to determine the number of digits
    assert min(arr) >= 0
    max_num: int = max(arr)
    output: List[int] = [None] * len(arr)
    
    # Perform counting sort for every digit (starting from the least significant digit)
    exp: int = 1
    while max_num // exp > 0:
        counting_sort(arr, exp, output)
        arr, output = output, arr
        exp *= 10
        
    return arr


def test_radix_sort():
    import random  
    for _ in range(100):
        arr = random.choices(range(100), k=random.randint(1, 200))
        sorted_arr = sorted(arr)
        output = radix_sort(arr)
        print(output)
        assert output == sorted_arr
        
if __name__ == "__main__":
    test_radix_sort()