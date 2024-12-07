#include <iostream>
#include <vector>

#include "vector_utils.hpp"

std::vector<int> countingSortStableVersion(const std::vector<int>& array, int upperBound) {
    std::vector<int> sorted_array(array.size());
    // Count the number of occurrences for each element in the array
    std::vector<int> count(upperBound + 1);
    for (auto& elem : array) {
        count[elem]++;
    }
    for(int i = 1; i <= upperBound; ++i) {
        count[i] += count[i - 1];
    }
    // Fill the sorted array with elements in reverse order 
    for (int i = array.size() - 1; i >= 0; --i) {
        sorted_array[count[array[i]] - 1] = array[i];
        --count[array[i]];
    }

    return sorted_array;
}

int main(int argc, char const *argv[])
{
    SortingFunctionNotInPlace countingSortLambda = [](const std::vector<int>& array) -> std::vector<int> {
        return countingSortStableVersion(array, 500);
    };
    testSortingAlgorithm(countingSortLambda, 1000, 0, 500, "Counting Sort");
    return 0;
}
