#include <iostream>
#include <vector>
#include <cassert>
#include "vector_utils.hpp"


int mergeInversions(std::vector<int>& left, std::vector<int>& right, std::vector<int>& vec){
    std::size_t i = 0;
    std::size_t j = 0;
    std::size_t k = 0;

    int num_inversions = 0;

    while (i < left.size() && j < right.size()) {
        if(left[i] < right[j]){
            vec[k++] = left[i++];
        }else if(left[i] > right[j]){
            num_inversions += left.size() - i;
            vec[k++] = right[j++];
        } else {
            assert(false);
        }
    }

    while (i < left.size()) {
        vec[k++] = left[i++];
    }

    while (j < right.size()) {
        vec[k++] = right[j++];
    }

    return num_inversions;
}


int countInversions(std::vector<int>& vec){
    if(vec.size() <= 1){
        return 0;
    }
    int num_inversions = 0;
    std::vector<int> left(vec.begin(), vec.begin() + (vec.size()/2));
    std::vector<int> right(vec.begin() + (vec.size()/2), vec.end());
    num_inversions += countInversions(left);
    num_inversions += countInversions(right);
    num_inversions += mergeInversions(left, right, vec);

    return num_inversions;
}


int countInversionsBruteForce(std::vector<int>& vec){
    int num_inversions = 0;
    for(std::size_t i=0; i<vec.size(); ++i){
        for(std::size_t j=i+1; j<vec.size(); ++j){
            if(vec[i] > vec[j]){
                num_inversions++;
            }
        }
    }

    return num_inversions;
}


int main(int argc, char const *argv[])
{
    for(int n = 1; n <= 300; ++n){
        std::vector<int> vec = generateRandomVectorWithDistinctValues(n, -1000, 1000);
        std::vector<int> vec_copy = vec;
        assert(countInversionsBruteForce(vec) == countInversions(vec_copy));
        // std::cout << "size = " << n << std::endl;
        // printVector(vec);
        // printVector(vec_copy);
    }
    std::cout << "All tests passed!" << std::endl;

    return 0;
}
