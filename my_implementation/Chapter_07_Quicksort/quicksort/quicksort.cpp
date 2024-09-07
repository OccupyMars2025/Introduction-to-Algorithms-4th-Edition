#include <iostream>
#include <vector>

#include <algorithm>
#include "vector_utils.hpp"


/**
 * rearrange the elements in the vector.
 * 
 * @param vec : The vector to be rearranged.
 * @param left : The left index of the vector. inclusive.
 * @param right : The right index of the vector. inclusive.
 * 
 * @return the pivot index such that all elements in the left part are less than or equal to vec[pivot_index],
 *         and all elements in the right part are greater than or equal to vec[pivot_index].
*/
int partition(std::vector<int> &vec, int left, int right) {
    int pivot_index = left + rand() % (right - left + 1);
    std::swap(vec[right], vec[pivot_index]);

    int pivot = vec[right];

    int i = left - 1;
    for (int j = left; j < right; ++j) {
        if (vec[j] <= pivot) {
            i++;
            std::swap(vec[i], vec[j]);
        }
    }
    std::swap(vec[i + 1], vec[right]);
    return i + 1;
}

/**
 * quick sort in place.
 *
 * @param left : The left index of the vector. inclusive.
 * @param right : The right index of the vector. inclusive.
 * @return void
 */
void quickSort(std::vector<int> &vec, int left, int right)
{
    if (left >= right) return;

    int pivot_index = partition(vec, left, right);
    quickSort(vec, left, pivot_index - 1);
    quickSort(vec, pivot_index + 1, right);
}

void quickSort(std::vector<int> &vec)
{
    quickSort(vec, 0, vec.size() - 1);
}

int main(int argc, char const *argv[])
{
    testSortingAlgorithm(quickSort, "quick sort");

    return 0;
}
