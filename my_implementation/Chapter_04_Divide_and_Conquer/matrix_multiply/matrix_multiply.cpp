#include <iostream>
#include <vector>

#include "vector_utils.hpp"


/**
 * Straightforward implementation of matrix multiplication.
 * 
 * C = A * B + C
 * 
 * @param A - matrix (n, n)
 * @param B - matrix (n, n)
 * @param C - matrix (n, n)
*/
void matrixMultiplyStraightforward(Matrix &A, Matrix &B, Matrix &C) {
    int n = A.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < n; ++k) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}


typedef std::vector<std::vector<int>> Matrix;

class SubmatrixProxy {
public:
    SubmatrixProxy(Matrix& matrix)
        : matrix(matrix), rowStart(0), colStart(0), rowEnd(matrix.size()), colEnd(matrix[0].size()) {}

    SubmatrixProxy(SubmatrixProxy& submatrix, int rowStart, int colStart, int rowEnd, int colEnd)
        : matrix(submatrix.matrix), rowStart(submatrix.rowStart + rowStart), colStart(submatrix.colStart + colStart),
          rowEnd(submatrix.rowStart + rowEnd), colEnd(submatrix.colStart + colEnd) {}

    // Implement operators to access and modify the submatrix
    int& operator()(int row, int col) {
        return matrix[rowStart + row][colStart + col];
    }

    int getNumRows() const {
        return rowEnd - rowStart;
    }

    int getNumCols() const {
        return colEnd - colStart;
    }

    Matrix& getWholeMatrix() {
        return matrix;
    }

private:
    Matrix& matrix;
    int rowStart, colStart, rowEnd, colEnd;
};



/**
 * Recursive implementation of matrix multiplication.
 * Divide and conquer.
 * 
 * Just modify C in place.
 * C = A * B + C
 * 
 * @param A - matrix (n, n)
 * @param B - matrix (n, n)
 * @param C - matrix (n, n)
*/
void matrixMultiplyRecursive(SubmatrixProxy &A, SubmatrixProxy &B, SubmatrixProxy &C) {
    int n = A.getNumRows();
    if (n == 1) {
        C(0, 0) += A(0, 0) * B(0, 0);
        return;
    }
    assert(n % 2 == 0);
    int half_n = n / 2;

    SubmatrixProxy A11(A, 0, 0, half_n, half_n);
    SubmatrixProxy A12(A, 0, half_n, half_n, n);
    SubmatrixProxy A21(A, half_n, 0, n, half_n);
    SubmatrixProxy A22(A, half_n, half_n, n, n);

    SubmatrixProxy B11(B, 0, 0, half_n, half_n);
    SubmatrixProxy B12(B, 0, half_n, half_n, n);
    SubmatrixProxy B21(B, half_n, 0, n, half_n);
    SubmatrixProxy B22(B, half_n, half_n, n, n);

    SubmatrixProxy C11(C, 0, 0, half_n, half_n);
    SubmatrixProxy C12(C, 0, half_n, half_n, n);
    SubmatrixProxy C21(C, half_n, 0, n, half_n);
    SubmatrixProxy C22(C, half_n, half_n, n, n);

    matrixMultiplyRecursive(A11, B11, C11);
    matrixMultiplyRecursive(A12, B21, C11);

    matrixMultiplyRecursive(A11, B12, C12);
    matrixMultiplyRecursive(A12, B22, C12);

    matrixMultiplyRecursive(A21, B11, C21);
    matrixMultiplyRecursive(A22, B21, C21);

    matrixMultiplyRecursive(A21, B12, C22);
    matrixMultiplyRecursive(A22, B22, C22);
}


void testMatrixMultiply() {
    for (int i = 0; i < 10; ++i) {
        int n = 1 << i;

        Matrix A = generateRandomMatrix(n, n, -100, 100);
        SubmatrixProxy A_proxy(A);
        Matrix B = generateRandomMatrix(n, n, -100, 100);
        SubmatrixProxy B_proxy(B);
        Matrix benchmark_C = generateRandomMatrix(n, n, -100, 100);
        Matrix C_copy1 = benchmark_C;
        SubmatrixProxy C_proxy1(C_copy1);

        matrixMultiplyStraightforward(A, B, benchmark_C);
        matrixMultiplyRecursive(A_proxy, B_proxy, C_proxy1);

        assert(isMatrixEqual(C_proxy1.getWholeMatrix(), benchmark_C));
    }
    std::cout << "All tests passed !" << std::endl;
}

int main(int argc, char const *argv[])
{
    testMatrixMultiply();
    return 0;
}
