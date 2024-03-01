#include <iostream>
#include <cassert>

using namespace std;


template <typename T>
void selection_sort(T *a, int start, int stop)
{
    /* sort a[start, stop) */
    if (start >= stop - 1)
        return;
    for (int i = start; i < stop - 1; ++i) {
        int index_of_smallest_value = i;
        for (int j = i + 1; j < stop; ++j) {
            if (a[j] < a[index_of_smallest_value]) {
                index_of_smallest_value = j;
            }
        }
        swap(a[i], a[index_of_smallest_value]);
    }
}

int main()
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

        selection_sort(a, 0, n);

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

    return 0;
}