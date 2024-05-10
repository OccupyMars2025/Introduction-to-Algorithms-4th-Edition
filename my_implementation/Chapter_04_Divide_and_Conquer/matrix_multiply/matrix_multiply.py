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
            
            
def test_maxtrix_multiply():
    for n in range(1, 260):
        A = np.random.randint(100, size=(n, n))
        B = np.random.randint(100, size=(n, n))
        C = np.random.randint(100, size=(n, n))
        C_copy1 = C.copy()
        C_copy2 = C.copy()

        C += np.matmul(A, B)
        
        matrix_multiply_straightforward(A, B, C_copy1)
        assert np.all(C == C_copy1)        
        
        if n == 2 ** int(np.log2(n)):
            matrix_multiply_recursive(A, B, C_copy2)
            assert np.all(C == C_copy2)
            print(f'Test the recursive method for n = {n} passed.')
            
    print('All tests passed.')
        
        
if __name__ == '__main__':
    test_maxtrix_multiply()
    