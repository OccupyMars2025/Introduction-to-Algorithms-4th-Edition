#include <iostream>
#include <random>
#include <vector>
#include "vector_utils.hpp"


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