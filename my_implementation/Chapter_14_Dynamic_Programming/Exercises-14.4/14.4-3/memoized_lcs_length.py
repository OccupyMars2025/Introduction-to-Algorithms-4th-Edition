from typing import List, Dict, Tuple

def memoized_lcs_length(X: List[int], Y: List[int]) -> int:
    # Define the memoization dictionary
    memo: Dict[Tuple[int, int], int] = {}

    def lcs_recursive(i: int, j: int) -> int:
        # Base case: If either sequence is empty, LCS length is 0
        if i == 0 or j == 0:
            return 0

        # Check if result is already in memo
        if (i, j) in memo:
            return memo[(i, j)]

        # If characters match, add 1 to the result and move diagonally in both sequences
        if X[i - 1] == Y[j - 1]:
            memo[(i, j)] = 1 + lcs_recursive(i - 1, j - 1)
        else:
            # Otherwise, take the maximum of excluding one character from either sequence
            memo[(i, j)] = max(lcs_recursive(i - 1, j), lcs_recursive(i, j - 1))

        return memo[(i, j)]

    # Call the recursive function starting from the end of both sequences
    return lcs_recursive(len(X), len(Y))


def LCS_length(X: List[int], Y: List[int]) -> Tuple[List[List[int]], List[List[str]]]:
    m = len(X)
    n = len(Y)
    C = [[0] * (n + 1) for _ in range(m + 1)]
    b = [[" "] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                C[i][j] = 1 + C[i-1][j-1]
                b[i][j] = "↖"
            else:
                if C[i-1][j] >= C[i][j-1]:
                    C[i][j] = C[i-1][j]
                    b[i][j] = "↑"
                else:
                    C[i][j] = C[i][j-1]
                    b[i][j] = "←"
    return C, b


def printLCS(b: List[List[str]], X: List[int], i: int, j: int) -> None:
    if i == 0 or j == 0:
        return
    if b[i][j] == "↖":
        printLCS(b, X, i-1, j-1)
        print(f"{X[i-1]}, ", end='')
    elif b[i][j] == "↑":
        printLCS(b, X, i-1, j)
    else:
        printLCS(b, X, i, j-1)
    
    
def test():
    # generate two random sequences of integers
    import random
    X = [random.randint(0, 6) for _ in range(15)]
    Y = [random.randint(0, 6) for _ in range(20)]
    print("X =", X)
    print("Y =", Y)
    
    C, b = LCS_length(X, Y)
    assert memoized_lcs_length(X, Y) == C[-1][-1]
    print("Length of the longest common subsequence is", C[-1][-1])
    printLCS(b, X, len(X), len(Y))
    print()
    
    # # print the table C
    # print("Table C")
    # for i in range(len(C)):
    #     print(C[i])
        
    # # print the table b
    # print("\nTable b")
    # for i in range(len(b)):
    #     print(b[i])
    

if __name__ == "__main__":
    test()
