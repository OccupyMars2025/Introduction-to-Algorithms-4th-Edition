#include <iostream>
#include <random>
#include <vector>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <iomanip>
#include <functional>

#include "vector_utils.hpp"


std::vector<int> generateRandomVectorWithDistinctValues(int size, int minValue, int maxValue) {
    std::random_device rd;
    std::mt19937 g(rd());

    std::vector<int> values(maxValue - minValue + 1);
    std::iota(values.begin(), values.end(), minValue); // Fill the vector with sequential values

    std::shuffle(values.begin(), values.end(), g); // Shuffle the vector

    std::vector<int> vec(values.begin(), values.begin() + size); // Take the first size elements

    return vec;
}

std::vector<int> generateRandomVector(int size, int minValue, int maxValue) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(minValue, maxValue);

    std::vector<int> vec(size);
    for (int i = 0; i < size; ++i) {
        vec[i] = dis(gen);
    }

    return vec;
}


void printVector(const std::vector<int>& a) {
    std::cout << "[";
    for(const auto& element : a) {
        std::cout << std::setw(10) << element << " ";
    }
    std::cout << "]" << std::endl;
}

bool isSorted(const std::vector<int>& a) {
    for(int i = 0; i < a.size() - 1; ++i) {
        if (a[i] > a[i + 1]) {
            return false;
        }
    }
    return true;
}



void testSearchingAlgorithm(bool (*searchingMethod)(std::vector<int> const& vec, int x, int* index), std::string methodName) {
    /**
     * bool (*searchingMethod)(std::vector<int> const& vec, int x, int* index)
     * searches for the value x in a vector vec,
     * if the value is found, returns true and sets "*index" to the position of x in vec;
     * if the value is not found, returns false and sets "*index" to the position before which x should be inserted in vec
    */
    int index;
    for(int n = 1; n < 50; ++n) {
        std::vector<int> vec = generateRandomVector(n, -100, 100);
        std::sort(vec.begin(), vec.end());
        for (int x=-200; x < 200; ++x) {
            bool found = searchingMethod(vec, x, &index);
            if (found) {
                assert(index >= 0 && index < n);
                assert(vec[index] == x);
            } else {
                assert(index >= 0 && index <= n);
                if(index == 0) {
                    assert(vec[index] > x);
                } else if (index == n) {
                    assert(vec[index-1] < x);
                } else {
                    assert(vec[index-1] < x && vec[index] > x);
                }               
            }
        }
    }
    std::cout << methodName << " passed all tests" << std::endl;
}


void testSortingAlgorithm(const SortingFunction& sortingFunction, int maxArraySize, int minValue, int maxValue, std::string methodName) {
    for(int n = 1; n <= maxArraySize; ++n) {
        std::vector<int> randomVector = generateRandomVector(n, minValue, maxValue);
        std::vector<int> sortedVector = randomVector;
        std::sort(sortedVector.begin(), sortedVector.end());

        sortingFunction(randomVector);
        bool isVecSorted = isSorted(randomVector);
        if(!isVecSorted) {
            std::cout << "Error: The test of the sorting algorithm " << methodName << " is failed !" << std::endl;
            std::cout << "The failed vector: ";
            printVector(randomVector);
            assert(false);
        }

        for(int j = 0; j < sortedVector.size(); ++j) {
            assert(randomVector[j] == sortedVector[j]);
        }
    }
    std::cout << methodName << " passed all tests" << std::endl;
}

void testSortingAlgorithm(const SortingFunctionNotInPlace& sortingFunction, int maxArraySize, int minValue, int maxValue, std::string methodName) {
    for(int n = 1; n <= maxArraySize; ++n) {
        std::vector<int> randomVector = generateRandomVector(n, minValue, maxValue);
        std::vector<int> sortedVector = randomVector;
        std::sort(sortedVector.begin(), sortedVector.end());

        std::vector<int> sortedVector002 = sortingFunction(randomVector);
        bool isVecSorted = isSorted(sortedVector002);
        if(!isVecSorted) {
            std::cout << "Error: The test of the sorting algorithm " << methodName << " is failed !" << std::endl;
            std::cout << "The failed vector: ";
            printVector(sortedVector002);
            assert(false);
        }

        assert(sortedVector002.size() == sortedVector.size());
        for(int j = 0; j < sortedVector.size(); ++j) {
            assert(sortedVector002[j] == sortedVector[j]);
        }
    }
    std::cout << methodName << " passed all tests" << std::endl;
}




Matrix generateRandomMatrix(int rows, int cols, int min, int max) {
    assert(rows > 0 && cols > 0 && min <= max);
    Matrix matrix(rows, std::vector<int>(cols));

    for(int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            matrix[i][j] = rand() % (max - min + 1) + min;
        }
    }

    return matrix;
}


void printMatrix(Matrix const & matrix) {
    std::cout << "--------------------------------------------------" << std::endl;
    std::cout << "Matrix (" << matrix.size() << ", " << matrix[0].size() << ") :" << std::endl;
    for(int i = 0; i < matrix.size(); ++i) {
        printVector(matrix[i]);
    }
    std::cout << "--------------------------------------------------" << std::endl;
}
