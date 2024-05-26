#pragma once

#include <iostream>
#include <random>
#include <vector>
#include <cassert>
#include <algorithm>
#include <iomanip>

typedef std::vector<std::vector<int>> Matrix;

template <typename T>
using SortingFunction = std::function<void(std::vector<T>& vec)>;
using SortingFunctionNotInPlace = std::function<std::vector<int>(const std::vector<int>& vec)>;

std::vector<int> generateRandomVectorWithDistinctValues(int size, int minValue, int maxValue);
template<typename T>
void testSearchingAlgorithm(bool (*searchingMethod)(std::vector<int> const& vec, int x, int* index), std::string methodName);
void testSortingAlgorithm(const SortingFunctionNotInPlace& sortingFunction, int maxArraySize, int minValue, int maxValue, std::string methodName);
Matrix generateRandomMatrix(int rows, int cols, int min, int max);
void printMatrix(Matrix const & matrix);

template<typename T>
void printVector(const std::vector<T>& a) {
    std::cout << "[";
    for(const auto& element : a) {
        std::cout << std::setw(10) << element << " ";
    }
    std::cout << "]" << std::endl;
}

template<typename T>
std::vector<T> generateRandomVector(int size, T minValue, T maxValue) {
    assert(minValue <= maxValue);
    std::vector<T> result(size);

    // Use the default random engine
    std::random_device rd;
    std::mt19937 gen(rd());

    if constexpr (std::is_floating_point_v<T>) {
        // Create a uniform distribution for floating-point types
        std::uniform_real_distribution<T> distr(minValue, maxValue);

        // Generate random values and store them in the vector
        std::generate(result.begin(), result.end(), [&]() { return distr(gen); });
    } else if constexpr (std::is_integral_v<T>) {
        // Create a uniform distribution for integer types
        std::uniform_int_distribution<T> distr(minValue, maxValue);

        // Generate random values and store them in the vector
        std::generate(result.begin(), result.end(), [&]() { return distr(gen); });
    } else {
        // Handle other types or throw an error
        static_assert(std::is_integral_v<T> || std::is_floating_point_v<T>,
                      "Unsupported type for generateRandomVector");
    }

    return result;
}



template<typename T>
bool isSorted(const std::vector<T>& a) {
    for(int i = 0; i < a.size() - 1; ++i) {
        if (a[i] > a[i + 1]) {
            return false;
        }
    }
    return true;
}


template<typename T>
void testSortingAlgorithm(const SortingFunction<T>& sortingFunction, int maxArraySize, T minValue, T maxValue, std::string methodName) {
    for(int n = 1; n <= maxArraySize; ++n) {
        std::vector<T> randomVector = generateRandomVector(n, minValue, maxValue);
        std::vector<T> sortedVector = randomVector;
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
