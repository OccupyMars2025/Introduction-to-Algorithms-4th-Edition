## 6.1-1

> What are the minimum and maximum numbers of elements in a heap of height $h$?

At least $2^h$ and at most $2^{h + 1} − 1$. Can be seen because a complete binary tree of depth $h − 1$ has $\sum_{i = 0}^{h - 1} 2^i = 2^h - 1$ elements, and the number of elements in a heap of depth $h$ is between the number for a complete binary tree of depth $h − 1$ exclusive and the number in a complete binary tree of depth $h$ inclusive.


## 6.1-2

> Show that an $n$-element heap has height $\lfloor \lg n \rfloor$.

Write $n = 2^m − 1 + k$ where $m$ is as large as possible. Then the heap consists of a complete binary tree of height $m − 1$, along with $k$ additional leaves along the bottom. The height of the root is the length of the longest simple path to one of these $k$ leaves, which must have length $m$. It is clear from the way we defined $m$ that $m = \lfloor \lg n\rfloor$.


## 6.1-3

> Show that in any subtree of a max-heap, the root of the subtree contains the largest value occuring anywhere in the subtree.

If the largest element in the subtree were somewhere other than the root, it has a parent that is in the subtree. So, it is larger than it's parent, so, the heap property is violated at the parent of the maximum element in the subtree.


## 6.1-4

> Where in a max-heap might the smallest element reside, assuming that all elements are distinct?

In any of the leaves, that is, elements with index $\lfloor n / 2 \rfloor + k$, where $k \geq 1$ (see exercise 6.1-7), that is, in the second half of the heap array.


## 6.1-5

# TODO


## 6.1-6


> Is an array that is in sorted order a min-heap?

Yes. For any index $i$, both $\text{LEFT}(i)$ and $\text{RIGHT}(i)$ are larger and thus the elements indexed by them are greater or equal to $A[i]$ (because the array is sorted.)


## 6.1-7

> Is the array with values $\langle 23, 17, 14, 6, 13, 10, 1, 5, 7, 12 \rangle$ a max-heap?

No. Since $\text{PARENT}(7)$ is $6$ in the array. This violates the max-heap property.


## 6.1-8

> Show that, with the array representation for sorting an $n$-element heap, the leaves are the nodes indexed by $\lfloor n / 2 \rfloor + 1, \lfloor n / 2 \rfloor + 2, \ldots, n$.


The last internal node is at the index $Parent(n) = \lfloor n / 2 \rfloor$. Amazingly easy !