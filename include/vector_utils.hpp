#pragma once

#include <iostream>
#include <random>
#include <vector>
#include <cassert>

std::vector<int> generateRandomVector(int size, int minValue, int maxValue);
void printVector(const std::vector<int>& a);
bool isSorted(const std::vector<int>& a);


template<typename SortingMethod>
void testSortingAlgorithm(SortingMethod& sortingMethod) {
    for(int i = 1; i < 50; ++i) {
        std::vector<int> randomVector = generateRandomVector(i, -100, 100);
        sortingMethod(randomVector);
        bool isVecSorted = isSorted(randomVector);
        if(!isVecSorted) {
            std::cout << "Error: The test of the sorting algorithm is failed !" << std::endl;
            std::cout << "The failed vector: ";
            printVector(randomVector);
            assert(false);
        }
    }
    std::cout << "The test of the sorting algorithm is passed" << std::endl;
}