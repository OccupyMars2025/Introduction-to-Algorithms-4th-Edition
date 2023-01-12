#include <iostream>
#include <cassert>

using namespace std;

template <typename T>
void merge(T *a, int start, int middle, int stop)
{
    /*
    merge two sorted lists a[start, middle), a[middle, stop)
    into a sorted list a[start, stop)
    */
    T *temp = (T*) malloc((stop - start) * sizeof(T));
    for (int i = start, j = 0; i < stop; ++i, ++j)
    {
        temp[j] = a[i];
    }
    T *left = temp;
    T *right = temp + middle - start;
    int length_1 = middle - start;
    int length_2 = stop - middle;

    int i = 0, j = 0, k = start;
    while (i < length_1 && j < length_2)
    {
        if (left[i] < right[j])
        {
            a[k++] = left[i++];
        }
        else
        {
            a[k++] = right[j++];
        }
    }

    while (i < length_1)
    {
        a[k++] = left[i++];
    }

    while (j < length_2)
    {
        a[k++] = right[j++];
    }

    delete temp;
}

template <typename T>
void merge_sort(T *a, int start, int stop)
{
    /* sort a[start, stop) */
    if (start >= stop - 1)
        return;
    int middle = (start + stop) / 2;
    merge_sort(a, start, middle);
    merge_sort(a, middle, stop);
    merge(a, start, middle, stop);
}


void test_merge_sort()
{
    int n;
    cout << "how many integers:";
    cin >> n;
    while (n > 0)
    {
        int *a = (int *)malloc(n * sizeof(int));
        for (int i = 0; i < n; ++i)
        {
            a[i] = rand() % 200 - 100;
            cout << a[i] << ", ";
        }
        cout << endl;

        merge_sort(a, 0, n);

        cout << "After sorting:" << endl;
        for (int i = 0; i < n; ++i)
        {
            if (i < n-1) {
                assert(a[i] <= a[i+1]);
            }
            cout << a[i] << ", ";
        }
        cout << endl;

        delete a;

        cout << "how many integers:";
        cin >> n;
    }
}