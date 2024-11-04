from typing import List, Tuple

def reconstruct_lcs(X: List[int], Y: List[int], c: List[List[int]]) -> List[int]:
    # Lengths of sequences X and Y
    m: int = len(X)
    n: int = len(Y)
    
    # Initialize variables for tracing back through the table
    i: int = m  # Start from the last row index
    j: int = n  # Start from the last column index
    lcs: List[int] = []  # This will store the LCS elements

    # Traverse the c table starting from the bottom-right corner
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:  # Match found
            lcs.append(X[i - 1])  # Add the element to LCS
            i -= 1
            j -= 1
        elif c[i - 1][j] >= c[i][j - 1]:  # Move up in the table
            assert c[i][j] == c[i - 1][j]
            i -= 1
        else:  # Move left in the table
            assert c[i][j] == c[i][j - 1]
            j -= 1

    # Reverse the lcs list to get the correct order of the LCS
    lcs.reverse()
    return lcs  # Return the LCS as a list of integers


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
    X = [random.randint(0, 6) for _ in range(10)]
    Y = [random.randint(0, 6) for _ in range(15)]
    print("X =", X)
    print("Y =", Y)
    
    C, b = LCS_length(X, Y)
    print("Length of the longest common subsequence is", C[-1][-1])
    printLCS(b, X, len(X), len(Y))
    print("\nreconstruct the LCS without using b table")
    print(reconstruct_lcs(X, Y, C))
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