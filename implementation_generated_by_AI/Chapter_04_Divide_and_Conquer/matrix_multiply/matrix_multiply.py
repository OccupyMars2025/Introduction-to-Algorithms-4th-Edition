import numpy as np

def matrix_multiply_straightforward(A: np.ndarray, B: np.ndarray, C: np.ndarray) -> None:
    """
    Straightforward implementation of matrix multiplication.
    
    :param A: np.array
        2-D array of shape (n, n)
    :param B: np.array
        2-D array of shape (n, n)
    :param C: np.array
        2-D array of shape (n, n)
        
    C = A * B + C
    """
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            C[i, j] += A[i, :].dot(B[:, j])


def matrix_multiply_recursive(A: np.ndarray, B: np.ndarray, C: np.ndarray) -> None:
    """
    Recursive implementation of matrix multiplication.
    Divide and conquer.
    
    :param A: np.array
        2-D array of shape (n, n)
    :param B: np.array
        2-D array of shape (n, n)
    :param C: np.array
        2-D array of shape (n, n)
    n is an exact power of 2.
        
    C = A * B + C
    """
    n = A.shape[0]
    if n == 1:
        C += A * B
        return
    
    assert n % 2 == 0
    half_n = n // 2
    
    A11 = A[:half_n, :half_n]
    A12 = A[:half_n, half_n:]
    A21 = A[half_n:, :half_n]
    A22 = A[half_n:, half_n:]
    
    B11 = B[:half_n, :half_n]
    B12 = B[:half_n, half_n:]
    B21 = B[half_n:, :half_n]
    B22 = B[half_n:, half_n:]
    
    C11 = C[:half_n, :half_n]
    C12 = C[:half_n, half_n:]
    C21 = C[half_n:, :half_n]
    C22 = C[half_n:, half_n:]
    
    matrix_multiply_recursive(A11, B11, C11)
    matrix_multiply_recursive(A12, B21, C11)
    
    matrix_multiply_recursive(A11, B12, C12)
    matrix_multiply_recursive(A12, B22, C12)
    
    matrix_multiply_recursive(A21, B11, C21)
    matrix_multiply_recursive(A22, B21, C21)
    
    matrix_multiply_recursive(A21, B12, C22)
    matrix_multiply_recursive(A22, B22, C22)
            
            
def test_square_maxtrix_multiply():
    print('Testing square matrix multiplication...')
    for n in range(1, 200):
        A = np.random.randint(100, size=(n, n))
        B = np.random.randint(100, size=(n, n))
        C = np.random.randint(100, size=(n, n))
        C_copy1 = C.copy()
        C_copy2 = C.copy()
        C_copy3 = C.copy()

        C += np.matmul(A, B)
        
        matrix_multiply_straightforward(A, B, C_copy1)
        assert np.all(C == C_copy1)        
        
        if n == 2 ** int(np.log2(n)):
            print(f'Test the recursive method for n = {n} passed.')
            matrix_multiply_recursive(A, B, C_copy2)
            assert np.all(C == C_copy2)
            square_matrix_multiply_strassen(A, B, C_copy3)
            assert np.all(C == C_copy3)
            
    print('All tests passed.')
    
    
def generalized_matrix_multiply_straightforward(A: np.ndarray, B: np.ndarray, C: np.ndarray) -> None:
    """
    Generalized matrix multiplication for any n x m matrices.
        
    :param A: np.array
        2-D array of shape (n, m)
    :param B: np.array
        2-D array of shape (m, p)
    :param C: np.array
        2-D array of shape (n, p)
    C = A * B + C
    """
    assert A.shape[1] == B.shape[0] and C.shape[0] == A.shape[0] and C.shape[1] == B.shape[1]
    n, m, p = A.shape[0], A.shape[1], B.shape[1]
    for i in range(n):
        for j in range(p):
            C[i, j] += sum([A[i, k] * B[k, j] for k in range(m)])


def generalized_matrix_multiply_recursive(A: np.ndarray, B: np.ndarray, C: np.ndarray) -> None:
    """
    Generalized matrix multiplication for any n x m matrices.
        
    :param A: np.array
        2-D array of shape (n, m)
    :param B: np.array
        2-D array of shape (m, p)
    :param C: np.array
        2-D array of shape (n, p)
    C = A * B + C
    """
    assert A.shape[1] == B.shape[0] and C.shape[0] == A.shape[0] and C.shape[1] == B.shape[1]
    n, m, p = A.shape[0], A.shape[1], B.shape[1]
    if n == 1 or m == 1 or p == 1:
        generalized_matrix_multiply_straightforward(A, B, C)
        return
    
    half_n = n // 2
    half_m = m // 2
    half_p = p // 2
    
    A11 = A[:half_n, :half_m]
    A12 = A[:half_n, half_m:]
    A21 = A[half_n:, :half_m]
    A22 = A[half_n:, half_m:]
    
    B11 = B[:half_m, :half_p]
    B12 = B[:half_m, half_p:]
    B21 = B[half_m:, :half_p]
    B22 = B[half_m:, half_p:]
    
    C11 = C[:half_n, :half_p]
    C12 = C[:half_n, half_p:]
    C21 = C[half_n:, :half_p]
    C22 = C[half_n:, half_p:]
    
    generalized_matrix_multiply_recursive(A11, B11, C11)
    generalized_matrix_multiply_recursive(A12, B21, C11)
    
    generalized_matrix_multiply_recursive(A11, B12, C12)
    generalized_matrix_multiply_recursive(A12, B22, C12)
    
    generalized_matrix_multiply_recursive(A21, B11, C21)
    generalized_matrix_multiply_recursive(A22, B21, C21)
    
    generalized_matrix_multiply_recursive(A21, B12, C22)
    generalized_matrix_multiply_recursive(A22, B22, C22)


def test_generalized_matrix_multiply(max_n: int, max_m: int, max_p: int) -> None:
    print('Testing generalized matrix multiply...')
    for n in range(1, max_n):
        for m in range(1, max_m):
            for p in range(1, max_p):
                # print(f'n = {n}, m = {m}, p = {p}')                
                
                A = np.random.randint(low=0, high=100, size=(n, m))
                B = np.random.randint(low=0, high=100, size=(m, p))
                C = np.random.randint(low=0, high=100, size=(n, p))
                C_copy = C.copy()
                C_copy2 = C.copy()
                
                C += np.matmul(A, B)
                
                generalized_matrix_multiply_straightforward(A, B, C_copy)
                assert np.all(C == C_copy)
                
                generalized_matrix_multiply_recursive(A, B, C_copy2)
                assert np.all(C == C_copy2)

    print('All tests passed')
        
        
def square_matrix_multiply_strassen(A: np.ndarray, B: np.ndarray, C: np.ndarray) -> None:
    """
    Strassen's matrix multiplication for square matrices of size n x n 
    in which n is an exact power of 2.
        
    :param A: np.array
        2-D array of shape (n, n)
    :param B: np.array
        2-D array of shape (n, n)
    :param C: np.array
        2-D array of shape (n, n)
    C = A * B + C
    """
    assert len(A.shape) == 2 and A.shape[0] == A.shape[1]
    assert A.shape == B.shape and C.shape == B.shape
    
    n = A.shape[0]
    if n == 1:
        C[0, 0] += A[0, 0] * B[0, 0]
        return
    
    assert n % 2 == 0
    half_n = n // 2
    
    A11 = A[:half_n, :half_n]
    A12 = A[:half_n, half_n:]
    A21 = A[half_n:, :half_n]
    A22 = A[half_n:, half_n:]
    
    B11 = B[:half_n, :half_n]
    B12 = B[:half_n, half_n:]
    B21 = B[half_n:, :half_n]
    B22 = B[half_n:, half_n:]
    
    C11 = C[:half_n, :half_n]
    C12 = C[:half_n, half_n:]
    C21 = C[half_n:, :half_n]
    C22 = C[half_n:, half_n:]
    
    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12
    
    P = [np.zeros(A11.shape, dtype=np.int64) for _ in range(8)]
    square_matrix_multiply_strassen(A11, S1, P[1])
    square_matrix_multiply_strassen(S2, B22, P[2])
    square_matrix_multiply_strassen(S3, B11, P[3])
    square_matrix_multiply_strassen(A22, S4, P[4])
    square_matrix_multiply_strassen(S5, S6, P[5])
    square_matrix_multiply_strassen(S7, S8, P[6])
    square_matrix_multiply_strassen(S9, S10, P[7])
    
    C11 += P[5] + P[4] - P[2] + P[6]
    C12 += P[1] + P[2]
    C21 += P[3] + P[4]
    C22 += P[5] + P[1] - P[3] - P[7]



if __name__ == '__main__':
    test_square_maxtrix_multiply()    
    test_generalized_matrix_multiply(20, 20, 20)