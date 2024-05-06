#include <iostream>
#include <random>
#include <vector>
#include "vector_utils.hpp"

void selectionSort(std::vector<int>& a) {
    int min_index;
    int temp;
    int n = a.size();
    for (int i = 0; i < n - 1; ++i) {
        min_index = i;
        for (int j = i + 1; j < n; ++j) {
            if (a[min_index] > a[j]) {
                min_index = j;
            }
        }
        temp = a[i];
        a[i] = a[min_index];
        a[min_index] = temp;
    }
}


int main() {
    testSortingAlgorithm(selectionSort);
    
    return 0;
}