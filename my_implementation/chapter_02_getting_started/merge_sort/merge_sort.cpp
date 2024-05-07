#include <iostream>
#include <vector>
#include <cassert>
#include "vector_utils.hpp"


void merge(std::vector<int>& left, std::vector<int>& right, std::vector<int>& vec){
    std::size_t i = 0;
    std::size_t j = 0;
    std::size_t k = 0;

    while (i < left.size() && j < right.size()) {
        if(left[i] <= right[j]){
            vec[k++] = left[i++];
        }else{
            vec[k++] = right[j++];
        }
    }

    while (i < left.size()) {
        vec[k++] = left[i++];
    }

    while (j < right.size()) {
        vec[k++] = right[j++];
    }
}


void countInversions(std::vector<int>& vec){
    if(vec.size() <= 1){
        return;
    }
    std::vector<int> left(vec.begin(), vec.begin() + (vec.size()/2));
    std::vector<int> right(vec.begin() + (vec.size()/2), vec.end());
    countInversions(left);
    countInversions(right);
    merge(left, right, vec);
}


int main(int argc, char const *argv[])
{
    testSortingAlgorithm(countInversions, "mergeSort");

    return 0;
}
