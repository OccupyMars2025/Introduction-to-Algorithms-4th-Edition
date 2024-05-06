#include <iostream>
#include <cassert>
#include <cstring>

#include "merge_sort.h"

template <typename T>
void print_array(T* a, int length) {
    for (int i = 0; i < length; i++)
    {
        cout << a[i] << ", ";
    }
    cout << endl;
}

template<typename T>
void sequential_search(T* a, int low, int high, T& value, int& index) {
    /*
    iterative version.

    a[low, high] is in a non-decreasing order.
    Search value in a[low, high].
    If found, then set "index" 
    If not found, then set "index" as -1 
    */
    for (int i = low; i <= high; i++)
    {
        if (a[i] == value) {
            index = i;
            return;
        }
    }
    index = -1;    
}


template<typename T>
void binary_search_v1(T* a, int low, int high, T& value, bool& found, int& index) {
    /*
    iterative version.

    a[low, high] is in a non-decreasing order.
    Search value in a[low, high].
    if found, then set index and set found as true
    if not found, then set "found" as false and set "index" as a value
    such that you can insert the "value" before "index" to keep a 
    still in a non-decreasing order
    */
    int middle;
    while (low <= high)
    {
        middle = (low + high) / 2;
        if (value < a[middle]) {
            high = middle - 1;
        } 
        else if (a[middle] < value)
        {
            low = middle + 1;
        }
        else {
            found = true;
            index = middle;
            return;
        }
    }
    
    // not found
    if (high == middle - 1) {
        assert(low == middle);
        found = false;
        index = middle;
    }
    else {
        assert(low == middle + 1);
        assert(high == middle);
        found = false;
        index = middle + 1;
    }
}


template<typename T>
void binary_search_v2(T* a, int low, int high, T& value, bool& found, int& index) {
    /*
    recursive version.

    a[low, high] is in a non-decreasing order.
    Search value in a[low, high].
    if found, then set index and set found as true
    if not found, then set "found" as false and set "index" as a value
    such that you can insert the "value" before "index" to keep "a" 
    still in a non-decreasing order
    */
    int middle;
    if (low < high) {
        middle = (low + high) / 2;
        if (value < a[middle]) {
            if (low == middle) {
                found = false;
                index = middle;
                return;
            } else {
                binary_search_v2(a, low, middle - 1, value, found, index);
            }
        } else if (a[middle] < value)
        {
            if (middle == high) {
                found = false;
                index = middle + 1;
                return;
            } else {
                binary_search_v2(a, middle + 1, high, value, found, index);
            }
        } else {
            found = true;
            index = middle;
            return;
        }
    } else if (low == high)
    {
        if (value < a[low]) {
            found = false;
            index = low;
        } else if (a[low] < value)
        {
            found = false;
            index = low + 1;
        } else {
            found = true;
            index = low;
        }
    } else {
        assert(false);
    }
}


void test_binary_search_v1_and_v2()
{
    /*
    test binary_search_v1 and binary_search_v2
    */
    bool found;
    int index;
    int value;

    for (int n = 1; n < 200; ++n)
    {
        int* a = (int*)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++)
        {
            // [-100, 100]
            a[i] = rand() % 200 - 100;
        }
        merge_sort(a, 0, n);
        print_array(a, n);
        for (int i = 0; i < n; ++i)
        {
            // binary_search_v1(a, 0, n-1, a[i], found, index);
            binary_search_v2(a, 0, n-1, a[i], found, index);
            assert(found);
            assert(a[i] == a[index]);
        }

        for (int i = 0; i < 200; i++)
        {
            // [-150, 150]
            value = rand() % 300 - 150;
            // binary_search_v1(a, 0, n - 1, value, found, index);
            binary_search_v2(a, 0, n - 1, value, found, index);
            if (found) {
                assert(a[index] == value);
            } else {
                int* temp = (int*)malloc((n + 1) * sizeof(int));
                memcpy(temp, a, index * sizeof(int));
                temp[index] = value;
                memcpy(temp + index + 1, a + index, (n - index) * sizeof(int));
                for (int i = 0; i < n; i++)
                {
                    assert(temp[i] <= temp[i+1]);
                }
                delete temp;
            }
        }
        delete a;
    }
}


template<typename T>
void binary_search_v3(T* a, int low, int high, T& value, int& index) {
    /*
    iterative version.

    a[low, high] is in a non-decreasing order.
    Search value in a[low, high].
    If found, then set "index" 
    If not found, then set "index" as -1 
    */
    int middle;
    while (low <= high)
    {
        middle = (low + high) / 2;
        if (value < a[middle]) {
            high = middle - 1;
        } 
        else if (a[middle] < value)
        {
            low = middle + 1;
        }
        else {
            index = middle;
            return;
        }
    }
    
    index = -1;
}


template<typename T>
void binary_search_v4(T* a, int low, int high, T& value, int& index) {
    /*
    recursive version.

    a[low, high] is in a non-decreasing order.
    Search value in a[low, high].
    If found, then set "index" 
    If not found, then set "index" as -1 
    */
    if (low <= high) {
        int middle = (low + high) / 2;
        if (a[middle] < value) {
            binary_search_v4(a, middle + 1, high, value, index);
        } else if (value < a[middle])
        {
            binary_search_v4(a, low, middle - 1, value, index);
        } else {
            index = middle;
        }
    } else {
        index = -1;
    }
}

void test_binary_search_v3_and_v4()
{
    /*
    test binary_search_v3 and binary_search_v4
    */
    int index;
    int value;

    for (int n = 1; n < 200; ++n)
    {
        int* a = (int*)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++)
        {
            // [-100, 100]
            a[i] = rand() % 200 - 100;
        }
        merge_sort(a, 0, n);
        print_array(a, n);
        for (int i = 0; i < n; ++i)
        {
            // binary_search_v3(a, 0, n-1, a[i], index);
            binary_search_v4(a, 0, n-1, a[i], index);
            assert(0 <= index && index < n);
            assert(a[i] == a[index]);
        }

        for (int i = 0; i < 200; i++)
        {
            // [-150, 150]
            value = rand() % 300 - 150;
            // binary_search_v3(a, 0, n - 1, value, index);
            binary_search_v4(a, 0, n - 1, value, index);
            if (-1 != index) {
                assert(0 <= index && index < n);
                assert(a[index] == value);
            } else {
                int index_2;
                sequential_search(a, 0, n - 1, value, index_2);
                assert(index_2 == -1);
            }
        }
        delete a;
    }
}


int main(int argc, char const *argv[])
{
    // test_binary_search_v1_and_v2();
    test_binary_search_v3_and_v4();
    cout << "Now, test binary_search_v4()" << endl;


    return 0;
}
