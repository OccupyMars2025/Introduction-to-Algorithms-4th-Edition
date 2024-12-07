from math import floor
from typing import List
import numpy as np
import copy


def bucket_sort(arr: List[float]):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for e in arr:
        buckets[int(np.floor(e * n))].append(e)
    sorted_arr = []
    for bucket in buckets:
        if len(bucket) > 0:
            bucket.sort()
            sorted_arr.extend(bucket)
    return sorted_arr


if __name__ == '__main__':
    for size in range(1, 2000):
        arr = np.random.rand(size).tolist()
        arr_copy = copy.deepcopy(arr)
        arr_copy.sort()
        assert  bucket_sort(arr) == arr_copy
    print('Tests passed')