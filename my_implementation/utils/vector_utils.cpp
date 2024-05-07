#include <iostream>
#include <random>
#include <vector>
#include <cassert>
#include <algorithm>
#include <numeric>

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
    for(const auto& element : a) {
        std::cout << element << " ";
    }
    std::cout << std::endl;
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



void testSortingAlgorithm(void (*sortingMethod)(std::vector<int>& vec), std::string methodName) {
    for(int i = 1; i < 50; ++i) {
        std::vector<int> randomVector = generateRandomVector(i, -100, 100);
        sortingMethod(randomVector);
        bool isVecSorted = isSorted(randomVector);
        if(!isVecSorted) {
            std::cout << "Error: The test of the sorting algorithm " << methodName << " is failed !" << std::endl;
            std::cout << "The failed vector: ";
            printVector(randomVector);
            assert(false);
        }
    }
    std::cout << methodName << " passed all tests" << std::endl;
}


