from typing import List

def construct_LIS(arr: List[int]) -> List[int]:
    n: int = len(arr)
    if n == 0:
        return []

    # Initialize the dp and prev arrays
    dp: List[int] = [1] * n         # dp[i] is the length of LIS ending at index i
    prev: List[int] = [-1] * n      # prev[i] stores the index of the previous element in the LIS ending at i

    # Fill dp and prev arrays
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] <= arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Find the index of the maximum length in dp
    lis_length: int = max(dp)
    lis_index: int = dp.index(lis_length)

    # Reconstruct the LIS by backtracking using the prev array
    lis: List[int] = []
    while lis_index != -1:
        lis.append(arr[lis_index])
        lis_index = prev[lis_index]

    # The sequence was built backwards, so reverse it
    lis.reverse()
    return lis



from typing import List, Dict, Tuple

def construct_LIS_memo(arr: List[int]) -> List[int]:
    n = len(arr)
    if n == 0:
        return []

    # Memoization dictionary for the LIS length and predecessor
    memo: Dict[int, Tuple[int, int]] = {}

    # Recursive function with memoization
    def lis_ending_at(i: int) -> int:
        if i in memo:
            return memo[i][0]
        
        max_len = 1  # The minimum LIS ending at any element is itself
        predecessor = -1

        # Check all previous elements for possible LIS extension
        for j in range(i):
            if arr[j] <= arr[i]:
                current_len = lis_ending_at(j) + 1
                if current_len > max_len:
                    max_len = current_len
                    predecessor = j
        
        memo[i] = (max_len, predecessor)
        return max_len

    # Calculate LIS ending at each index
    max_length = 0
    last_index = -1
    for i in range(n):
        current_length = lis_ending_at(i)
        if current_length > max_length:
            max_length = current_length
            last_index = i

    # Reconstruct the LIS by following predecessors
    lis: List[int] = []
    while last_index != -1:
        lis.append(arr[last_index])
        last_index = memo[last_index][1]

    lis.reverse()
    return lis



def main():
    import random
    for num in range(2, 50):
        arr = random.choices(range(1, 100), k=num)
        print("Input:", arr)
        lis = construct_LIS(arr)
        lis_memo = construct_LIS_memo(arr)
        assert len(lis) == len(lis_memo)
        print("Output:", lis)
        # check if the LIS is sorted
        assert all([a <= b for a, b in zip(lis[:-1], lis[1:])])
        assert all([a <= b for a, b in zip(lis_memo[:-1], lis_memo[1:])])
        
        
if __name__ == "__main__":
    main()