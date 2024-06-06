#include <iostream>
#include <cassert>
#include "vector_utils.hpp"


bool binarySearch(std::vector<int> const& vec, int x, int* index) {
    int low = 0;
    int high = vec.size() - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (x < vec[mid]) {
            high = mid - 1;
        } else if (x > vec[mid]) {
            low = mid + 1;
        } else {
            *index = mid;
            return true;
        }
    }
    *index = low;
    return false;
}

int main(int argc, char const *argv[])
{
    testSearchingAlgorithm(binarySearch, "binarySearch");
    
    return 0;
}
