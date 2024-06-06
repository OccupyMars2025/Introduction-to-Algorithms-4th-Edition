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
void squareMatrixMultiplyStraightforward(Matrix &A, Matrix &B, Matrix &C) {
    int n = A.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < n; ++k) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

class SubmatrixProxy {
public:
    SubmatrixProxy(Matrix& matrix)
        : matrix(matrix), rowStart(0), rowEnd(matrix.size()), colStart(0), colEnd(matrix[0].size()) {}

    SubmatrixProxy(SubmatrixProxy& submatrix, int rowStart, int rowEnd, int colStart, int colEnd)
        : matrix(submatrix.matrix), rowStart(submatrix.rowStart + rowStart), rowEnd(submatrix.rowStart + rowEnd), 
            colStart(submatrix.colStart + colStart), colEnd(submatrix.colStart + colEnd) {}

    // Implement operators to access and modify the submatrix
    int& operator()(int row, int col) {
        return matrix[rowStart + row][colStart + col];
    }

    const int& operator()(int row, int col) const {
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

    Matrix operator+(const SubmatrixProxy& other) const {
        assert(getNumRows() == other.getNumRows());
        assert(getNumCols() == other.getNumCols());

        Matrix result(getNumRows(), std::vector<int>(getNumCols(), 0));
        for (int i = 0; i < getNumRows(); ++i) {
            for (int j = 0; j < getNumCols(); ++j) {
                result[i][j] = (*this)(i, j) + other(i, j);
            }
        }
        return result;
    }

    SubmatrixProxy& operator+=(const SubmatrixProxy& other) {
        assert(getNumRows() == other.getNumRows());
        assert(getNumCols() == other.getNumCols());
        for (int i = 0; i < getNumRows(); ++i) {
            for (int j = 0; j < getNumCols(); ++j) {
                (*this)(i, j) += other(i, j);
            }
        }
        return *this;
    }

    SubmatrixProxy& operator-=(const SubmatrixProxy& other) {
        assert(getNumRows() == other.getNumRows());
        assert(getNumCols() == other.getNumCols());
        for (int i = 0; i < getNumRows(); ++i) {
            for (int j = 0; j < getNumCols(); ++j) {
                (*this)(i, j) -= other(i, j);
            }
        }
        return *this;
    }


    Matrix operator-(const SubmatrixProxy& other) const {
        assert(getNumRows() == other.getNumRows());
        assert(getNumCols() == other.getNumCols());

        Matrix result(getNumRows(), std::vector<int>(getNumCols(), 0));
        for (int i = 0; i < getNumRows(); ++i) {
            for (int j = 0; j < getNumCols(); ++j) {
                result[i][j] = (*this)(i, j) - other(i, j);
            }
        }
        return result;
    }

private:
    Matrix& matrix;
    int rowStart, rowEnd, colStart, colEnd;
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
void squareMatrixMultiplyRecursive(SubmatrixProxy &A, SubmatrixProxy &B, SubmatrixProxy &C) {
    int n = A.getNumRows();
    if (n == 1) {
        C(0, 0) += A(0, 0) * B(0, 0);
        return;
    }
    assert(n % 2 == 0);
    int half_n = n / 2;

    SubmatrixProxy A11(A, 0, half_n, 0, half_n);
    SubmatrixProxy A12(A, 0, half_n, half_n, n);
    SubmatrixProxy A21(A, half_n, n, 0, half_n);
    SubmatrixProxy A22(A, half_n, n, half_n, n);

    SubmatrixProxy B11(B, 0, half_n, 0, half_n);
    SubmatrixProxy B12(B, 0, half_n, half_n, n);
    SubmatrixProxy B21(B, half_n, n, 0, half_n);
    SubmatrixProxy B22(B, half_n, n, half_n, n);

    SubmatrixProxy C11(C, 0, half_n, 0, half_n);
    SubmatrixProxy C12(C, 0, half_n, half_n, n);
    SubmatrixProxy C21(C, half_n, n, 0, half_n);
    SubmatrixProxy C22(C, half_n, n, half_n, n);

    squareMatrixMultiplyRecursive(A11, B11, C11);
    squareMatrixMultiplyRecursive(A12, B21, C11);

    squareMatrixMultiplyRecursive(A11, B12, C12);
    squareMatrixMultiplyRecursive(A12, B22, C12);

    squareMatrixMultiplyRecursive(A21, B11, C21);
    squareMatrixMultiplyRecursive(A22, B21, C21);

    squareMatrixMultiplyRecursive(A21, B12, C22);
    squareMatrixMultiplyRecursive(A22, B22, C22);
}


/**
 * Strassen's algorithm for matrix multiplication (n, n)
 * in which n is an exact power of 2.
 * 
 * Divide and conquer.
 * 
 * Just modify C in place.
 * C = A * B + C
 * 
 * @param A - matrix (n, n)
 * @param B - matrix (n, n)
 * @param C - matrix (n, n)
*/
void squareMatrixMultiplyStrassen(SubmatrixProxy &A, SubmatrixProxy &B, SubmatrixProxy &C) {
    int n = A.getNumRows();
    assert(n == A.getNumCols());
    assert(n == B.getNumRows());
    assert(n == B.getNumCols());
    assert(n == C.getNumRows());
    assert(n == C.getNumCols());

    if (n == 1) {
        C(0, 0) += A(0, 0) * B(0, 0);
        return;
    }
    assert(n % 2 == 0);
    int half_n = n / 2;

    SubmatrixProxy A11(A, 0, half_n, 0, half_n);
    SubmatrixProxy A12(A, 0, half_n, half_n, n);
    SubmatrixProxy A21(A, half_n, n, 0, half_n);
    SubmatrixProxy A22(A, half_n, n, half_n, n);

    SubmatrixProxy B11(B, 0, half_n, 0, half_n);
    SubmatrixProxy B12(B, 0, half_n, half_n, n);
    SubmatrixProxy B21(B, half_n, n, 0, half_n);
    SubmatrixProxy B22(B, half_n, n, half_n, n);

    SubmatrixProxy C11(C, 0, half_n, 0, half_n);
    SubmatrixProxy C12(C, 0, half_n, half_n, n);
    SubmatrixProxy C21(C, half_n, n, 0, half_n);
    SubmatrixProxy C22(C, half_n, n, half_n, n);

    std::vector<Matrix> S(11, Matrix(half_n, std::vector<int>(half_n, 0)));
    S[1] = B12 - B22;
    S[2] = A11 + A12;
    S[3] = A21 + A22;
    S[4] = B21 - B11;
    S[5] = A11 + A22;
    S[6] = B11 + B22;
    S[7] = A12 - A22;
    S[8] = B21 + B22;
    S[9] = A11 - A21;
    S[10] = B11 + B12;
    std::vector<SubmatrixProxy> S_proxy;
    for(int i = 0; i < 11; ++i) {
        S_proxy.push_back(SubmatrixProxy(S[i]));
    }

    std::vector<Matrix> P(8, Matrix(half_n, std::vector<int>(half_n, 0)));
    std::vector<SubmatrixProxy> P_proxy;
    for(int i = 0; i < 8; ++i) {
        P_proxy.push_back(SubmatrixProxy(P[i]));
    }

    squareMatrixMultiplyStrassen(A11, S_proxy[1], P_proxy[1]);
    squareMatrixMultiplyStrassen(S_proxy[2], B22, P_proxy[2]);
    squareMatrixMultiplyStrassen(S_proxy[3], B11, P_proxy[3]);
    squareMatrixMultiplyStrassen(A22, S_proxy[4], P_proxy[4]);
    squareMatrixMultiplyStrassen(S_proxy[5], S_proxy[6], P_proxy[5]);
    squareMatrixMultiplyStrassen(S_proxy[7], S_proxy[8], P_proxy[6]);
    squareMatrixMultiplyStrassen(S_proxy[9], S_proxy[10], P_proxy[7]);


    // C11 += P[5] + P[4] - P[2] + P[6]
    // C12 += P[1] + P[2]
    // C21 += P[3] + P[4]
    // C22 += P[5] + P[1] - P[3] - P[7]
    C11 += P_proxy[5];
    C11 += P_proxy[4];
    C11 -= P_proxy[2];
    C11 += P_proxy[6];

    C12 += P_proxy[1];
    C12 += P_proxy[2];

    C21 += P_proxy[3];
    C21 += P_proxy[4];

    C22 += P_proxy[5];
    C22 += P_proxy[1];
    C22 -= P_proxy[3];
    C22 -= P_proxy[7];
}


void testSquareMatrixMultiply() {
    std::cout << "Testing square matrix multiply (n, n)(n is an exact power of 2)..." << std::endl;

    for (int i = 0; i < 8; ++i) {
        int n = 1 << i;
        std::cout << "Testing n = " << n << std::endl;

        Matrix A = generateRandomMatrix(n, n, -100, 100);
        SubmatrixProxy A_proxy(A);
        Matrix B = generateRandomMatrix(n, n, -100, 100);
        SubmatrixProxy B_proxy(B);
        Matrix benchmark_C = generateRandomMatrix(n, n, -100, 100);
        Matrix C_copy1 = benchmark_C;
        SubmatrixProxy C_proxy1(C_copy1);
        Matrix C_copy2 = benchmark_C;
        SubmatrixProxy C_proxy2(C_copy2);

        squareMatrixMultiplyStraightforward(A, B, benchmark_C);
        squareMatrixMultiplyRecursive(A_proxy, B_proxy, C_proxy1);
        squareMatrixMultiplyStrassen(A_proxy, B_proxy, C_proxy2);

        assert(C_proxy1.getWholeMatrix() == benchmark_C);
        assert(C_proxy2.getWholeMatrix() == benchmark_C);
    }
    std::cout << "All sqaure matrix multiply tests passed!" << std::endl;
}


/**
 *  Generalized matrix multiplication.
 *  
 *  @param A - matrix (n, m)
 *  @param B - matrix (m, p)
 *  @param C - matrix (n, p)
*/
void generalizedMatrixMultiplyStraightforward(SubmatrixProxy &A, SubmatrixProxy &B, SubmatrixProxy &C) {
    assert(A.getNumCols() == B.getNumRows());
    assert(C.getNumRows() == A.getNumRows());
    assert(C.getNumCols() == B.getNumCols());
    
    int n = A.getNumRows();
    int m = A.getNumCols();
    int p = B.getNumCols();

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j) {
            for (int k = 0; k < m; ++k) {
                C(i, j) += A(i, k) * B(k, j);
            }
        }
    }
}


/**
 *  Generalized matrix multiplication.
 *  Divides the problem into 4 subproblems.
 * 
 *  @param A - matrix (n, m)
 *  @param B - matrix (m, p)
 *  @param C - matrix (n, p)
 * 
*/
void generalizedMatrixMultiplyRecursive(SubmatrixProxy &A, SubmatrixProxy &B, SubmatrixProxy &C) {
    assert(A.getNumCols() == B.getNumRows());
    assert(C.getNumRows() == A.getNumRows());
    assert(C.getNumCols() == B.getNumCols());
    
    int n = A.getNumRows();
    int m = A.getNumCols();
    int p = B.getNumCols();

    if (n == 1 || m == 1 || p == 1) {
        generalizedMatrixMultiplyStraightforward(A, B, C);
        return;
    }

    int half_n = n / 2;
    int half_m = m / 2;
    int half_p = p / 2;

    SubmatrixProxy A11(A, 0, half_n, 0, half_m);
    SubmatrixProxy A12(A, 0, half_n, half_m, m);
    SubmatrixProxy A21(A, half_n, n, 0, half_m);
    SubmatrixProxy A22(A, half_n, n, half_m, m);

    SubmatrixProxy B11(B, 0, half_m, 0, half_p);
    SubmatrixProxy B12(B, 0, half_m, half_p, p);
    SubmatrixProxy B21(B, half_m, m, 0, half_p);
    SubmatrixProxy B22(B, half_m, m, half_p, p);

    SubmatrixProxy C11(C, 0, half_n, 0, half_p);
    SubmatrixProxy C12(C, 0, half_n, half_p, p);
    SubmatrixProxy C21(C, half_n, n, 0, half_p);
    SubmatrixProxy C22(C, half_n, n, half_p, p);


    generalizedMatrixMultiplyRecursive(A11, B11, C11);
    generalizedMatrixMultiplyRecursive(A12, B21, C11);

    generalizedMatrixMultiplyRecursive(A11, B12, C12);
    generalizedMatrixMultiplyRecursive(A12, B22, C12);

    generalizedMatrixMultiplyRecursive(A21, B11, C21);
    generalizedMatrixMultiplyRecursive(A22, B21, C21);

    generalizedMatrixMultiplyRecursive(A21, B12, C22);
    generalizedMatrixMultiplyRecursive(A22, B22, C22);
}

void testGeneralizedMatrixMultiply() {
    std::cout << "Testing generalized matrix multiply..." << std::endl;
    for (int n = 1; n <= 20; ++n) {
        for (int m = 1; m <= 20; ++m) {
            for (int p = 1; p <= 20; ++p) {
                Matrix A = generateRandomMatrix(n, m, -100, 100);
                SubmatrixProxy A_proxy(A);
                Matrix B = generateRandomMatrix(m, p, -100, 100);
                SubmatrixProxy B_proxy(B);
                Matrix C = generateRandomMatrix(n, p, -100, 100);
                SubmatrixProxy C_proxy(C);

                Matrix C_copy1 = C;
                SubmatrixProxy C_copy1_proxy(C_copy1);

                generalizedMatrixMultiplyStraightforward(A_proxy, B_proxy, C_proxy);
                generalizedMatrixMultiplyRecursive(A_proxy, B_proxy, C_copy1_proxy);

                assert(C_proxy.getWholeMatrix() == C_copy1_proxy.getWholeMatrix());
                // std::cout << "Test passed for n = " << n << ", m = " << m << ", p = " << p << std::endl;
            }
        }
    }
    std::cout << "All generalized matrix multiply tests passed!" << std::endl;
}


int main(int argc, char const *argv[])
{
    testSquareMatrixMultiply();
    testGeneralizedMatrixMultiply();

    return 0;
}
