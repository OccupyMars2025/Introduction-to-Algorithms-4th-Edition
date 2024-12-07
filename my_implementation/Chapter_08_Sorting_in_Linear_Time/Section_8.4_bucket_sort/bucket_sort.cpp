#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

#include "vector_utils.hpp"

void bucket_sort(std::vector<double>& v) {
    int n = static_cast<int>(v.size());
    std::vector<std::vector<double>> buckets(n);
    for (auto& x : v) {
        buckets[static_cast<int>(floor(x * double(n)))].push_back(x);
    }
    int i = 0;
    for (auto& bucket : buckets) {
        if (bucket.empty()) {
            continue;
        }
        std::sort(bucket.begin(), bucket.end());
        for (auto& x : bucket) {
            v[i++] = x;
        }
    }
}

int main() {
    testSortingAlgorithm<double>(bucket_sort, 2000, 0.0, 0.99999, "bucket sort");
}