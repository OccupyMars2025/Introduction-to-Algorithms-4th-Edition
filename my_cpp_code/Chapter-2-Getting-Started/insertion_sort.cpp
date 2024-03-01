#include <iostream>
#include <cassert>

using namespace std;


template <typename T>
void insertion_sort(T *a, int start, int stop)
{
    /* sort a[start, stop) */
    if (start >= stop - 1)
        return;
    for (int i = start + 1; i < stop; ++i) {
        int j = i - 1;
        T temp = a[i];
        while (j >= start && temp < a[j])
        {
            a[j + 1] = a[j];
            j -= 1;
        }
        a[j + 1] = temp;
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

        insertion_sort(a, 0, n);

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