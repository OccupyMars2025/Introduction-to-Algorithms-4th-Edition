#include <vector>
#include <iostream>
#include <algorithm>
#include <random>

/*
Sort the array using quicksort algorithm.
:param arr: the array to be sorted
:param left: the left index of the array, inclusive
:param right: the right index of the array, inclusive
*/
void quicksort(std::vector<int>& arr, int left, int right) {
    if (left >= right) {
        return;
    }

    int pivot = arr[left];
    int i = left + 1;
    int j = right;

    while (i <= j) {
        while (i <= j && arr[i] < pivot) {
            i++;
        }
        while (i <= j && arr[j] >= pivot) {
            j--;
        }
        if (i < j) {
            std::swap(arr[i], arr[j]);
        }
    }

    std::swap(arr[left], arr[j]);

    quicksort(arr, left, j - 1);
    quicksort(arr, j + 1, right);
}


// Function to generate a random vector of integers
std::vector<int> generate_random_vector(int n, int min_value = 0, int max_value = 100) {
    // Initialize a random device and random engine
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(min_value, max_value);

    // Generate the random vector
    std::vector<int> random_vector(n);
    for (int i = 0; i < n; ++i) {
        random_vector[i] = dis(gen);
    }
    return random_vector;
}

int main() {
    int min_value = 0; // Minimum value for random numbers
    int max_value = 100; // Maximum value for random numbers

    for (int n = 1; n <= 1000; n++) {
        std::vector<int> random_vector = generate_random_vector(n, min_value, max_value);

        quicksort(random_vector, 0, random_vector.size() - 1);

        if(std::is_sorted(random_vector.begin(), random_vector.end()) == false) {
            std::cout << "Error: The array is not sorted." << std::endl;
            exit(1);
        }
    }

    std::cout << "All tests passed." << std::endl;
    return 0;
}
