from typing import List, Tuple

def lcs_length_two_rows(X: List[int], Y: List[int]) -> int:
    m: int = len(X)  # Length of list X
    n: int = len(Y)  # Length of list Y

    # Ensure that X is the longer list for optimization
    if m < n:
        X, Y = Y, X
        m, n = n, m

    previous_row: List[int] = [0] * (n + 1)  # Stores previous row of LCS values
    current_row: List[int] = [0] * (n + 1)   # Stores current row of LCS values

    # Iterate over each element in X
    for i in range(1, m + 1):
        # Iterate over each element in Y
        for j in range(1, n + 1):
            # Check if elements from X and Y match
            if X[i - 1] == Y[j - 1]:
                current_row[j] = previous_row[j - 1] + 1  # Match found, increment LCS count
            else:
                current_row[j] = max(previous_row[j], current_row[j - 1])  # Take max of previous row or column

        # Swap rows: current_row becomes previous_row for next iteration
        previous_row, current_row = current_row, previous_row

    return previous_row[n]  # Return the LCS length in the last cell of the previous row


def lcs_length_one_row(X: List[int], Y: List[int]) -> int:
    m: int = len(X)  # Length of list X
    n: int = len(Y)  # Length of list Y

    # Ensure that X is the longer list for optimization
    if m < n:
        X, Y = Y, X
        m, n = n, m

    current_row: List[int] = [0] * (n + 1)  # Stores LCS values for current and previous rows

    # Iterate over each element in X
    for i in range(1, m + 1):
        previous: int = 0  # Tracks the value of current_row[j-1] from the previous iteration

        # Iterate over each element in Y
        for j in range(1, n + 1):
            temp: int = current_row[j]  # Temporarily store current cell's value

            # Check if elements from X and Y match
            if X[i - 1] == Y[j - 1]:
                current_row[j] = previous + 1  # Match found, increment LCS count
            else:
                current_row[j] = max(current_row[j], current_row[j - 1])  # Take max of current row or previous cell

            previous = temp  # Update `previous` for the next column iteration

    return current_row[n]  # Return the LCS length in the last cell of the row


###################################33


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
    for i in range(1, 20):
        for j in range(1, 20):
            X = [random.randint(0, 6) for _ in range(i)]
            Y = [random.randint(0, 6) for _ in range(j)]
            print("X =", X)
            print("Y =", Y)
            
            C, b = LCS_length(X, Y)
            length_lcs_v001 = lcs_length_one_row(X, Y)
            length_lcs_v002 = lcs_length_two_rows(X, Y)
            assert (length_lcs_v002 == length_lcs_v001) and (length_lcs_v001 == C[-1][-1])
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