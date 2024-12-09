## 6.5-7

> Argue the correctness of $\text{HEAP-INCREASE-KEY}$ using the following loop invariant:
>
> At the start of each iteration of the **while** loop of lines 4-6, the subarray $A[1 ..A.heap\text-size]$ satisfies the max-heap property, except that there may be one violation: $A[i]$ may be larger than $A[\text{PARENT}(i)]$.
>
> You may assume that the subarray $A[1..A.heap\text-size]$ satisfies the max-heap property at the time $\text{HEAP-INCREASE-KEY}$ is called.

**Initialization:** $A$ is a heap except that $A[i]$ might be larger that it's parent, because it has been modified. $A[i]$ is larger than its children, because otherwise the guard clause would fail and the loop will not be entered (the new value is larger than the old value and the old value is larger than the children).

**Maintenance:** When we exchange $A[i]$ with its parent, the max-heap property is satisfied except that now $A[\text{PARENT}(i)]$ might be larger than its parent. Changing $i$ to its parent maintains the invariant.

**Termination:** The loop terminates whenever the heap is exhausted or the max-heap property for $A[i]$ and its parent is preserved. At the loop termination, $A$ is a max-heap.

## 6.5-8

> Each exchange operation on line 5 of $\text{HEAP-INCREASE-KEY}$ typically requires three assignments. Show how to use the idea of the inner loop of $\text{INSERTION-SORT}$ to reduce the three assignments down to just one assignment.

```cpp
HEAP-INCREASE-KEY(A, i, key)
    if key < A[i]
        error "new key is smaller than current key"
    while i > 1 and A[PARENT(i)] < key
        A[i] = A[PARENT(i)]
        i = PARENT(i)
    A[i] = key
```


## 6.5-9

> Show how to implement a first-in, first-out queue with a priority queue. Show how to implement a stack with a priority queue. (Queues and stacks are defined in section 10.1).

Both are simple. For a stack we keep adding elements in increasing priority, while in a queue we add them in decreasing priority. For the stack we can set the new priority to $\text{HEAP-MAXIMUM}(A) + 1$. For the queue we need to keep track of it and decrease it on every insertion.

Both are not very efficient. Furthermore, if the priority can overflow or underflow, so will eventually need to reassign priorities.



## 6.5-10

> The operation $\text{HEAP-DELETE}(A, i)$ deletes the item in node $i$ from heap $A$. Give an implementation of $\text{HEAP-DELETE}$ that runs in $O(\lg n)$ time for an $n$-element max-heap.
> I think you had better change the location of "A.heap-size = A.heap-size - 1"

```cpp
HEAP-DELETE(A, i)
    if A[i] > A[A.heap-size]
        A[i] = A[A.heap-size]
        MAX-HEAPIFY(A, i)
    else
        HEAP-INCREASE-KEY(A, i, A[A.heap-size])
    A.heap-size = A.heap-size - 1
```

**Note:** The following algorithm is wrong. For example, given an array $A = [15, 7, 9, 1, 2, 3, 8]$ which is a max-heap, and if we delete $A[5] = 2$, then it will fail.

```cpp
HEAP-DELETE(A, i)
    A[i] = A[A.heap-size]
    A.heap-size = A.heap-size - 1
    MAX-HEAPIFY(A, i)
```

- before:

    ```
          15
        /    \
       7      9
      / \    / \
     1   2  3   8
    ```

- after (which is wrong since $8 > 7$ violates the max-heap property):

    ```
          15
        /    \
       7      9
      / \    /
     1   8  3
    ```



## 6.5-11

> Give an $O(n\lg k)$-time algorithm to merge $k$ sorted lists into one sorted list, where $n$ is the total number of elements in all the input lists. ($\textit{Hint:}$ Use a min-heap for $k$-way merging.)

We treat each sorted list as a object, in which we define the method "get_key()" which return the value of the smallest element in that list. We construct the k objects as a min-heap.

We take one element of each list and put it in a min-heap. Along with each element we have to track which list we took it from. When merging, we take the minimum element from the heap and insert another element off the list it came from (unless the list is empty). We continue until we empty the heap.

We have $n$ steps and at each step we're doing an insertion into the heap, which is $\lg k$.

Suppose that sorted lists on input are all nonempty, we have the following pseudocode.

```python
def MERGE-SORTED-LISTS(lists)
    # k = lists.size
    build_min_heap(lists)
    merged-lists = []
    while lists.heapsize > 0:
        merged-lists.append(lists[0].delete(0))
        if lists[0].size == 0:
            lists[0] = lists[lists.heapsize - 1]
            lists.heapsize -= 1
        lists.min_heapify(0)
    return merged-lists
```
