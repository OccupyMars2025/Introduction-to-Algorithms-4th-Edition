## 6.4-1

> Using figure 6.4 as a model, illustrate the operation of $\text{HEAPSORT}$ on the array $A = \langle 5, 13, 2, 25, 7, 17, 20, 8, 4 \rangle$.

$$
\begin{aligned}
\langle  5, 13,  2, 25, 7, 17, 20,  8,  4 \rangle \\\\
\langle  5, 13, 20, 25, 7, 17,  2,  8,  4 \rangle \\\\
\langle  5, 25, 20, 13, 7, 17,  2,  8,  4 \rangle \\\\
\langle 25,  5, 20, 13, 7, 17,  2,  8,  4 \rangle \\\\
\langle 25, 13, 20,  5, 7, 17,  2,  8,  4 \rangle \\\\
\langle 25, 13, 20,  8, 7, 17,  2,  5,  4 \rangle \\\\
\langle  4, 13, 20,  8, 7, 17,  2,  5, 25 \rangle \\\\
\langle 20, 13,  4,  8, 7, 17,  2,  5, 25 \rangle \\\\
\langle 20, 13, 17,  8, 7,  4,  2,  5, 25 \rangle \\\\
\langle  5, 13, 17,  8, 7,  4,  2, 20, 25 \rangle \\\\
\langle 17, 13,  5,  8, 7,  4,  2, 20, 25 \rangle \\\\
\langle  2, 13,  5,  8, 7,  4, 17, 20, 25 \rangle \\\\
\langle 13,  2,  5,  8, 7,  4, 17, 20, 25 \rangle \\\\
\langle 13,  8,  5,  2, 7,  4, 17, 20, 25 \rangle \\\\
\langle  4,  8,  5,  2, 7, 13, 17, 20, 25 \rangle \\\\
\langle  8,  4,  5,  2, 7, 13, 17, 20, 25 \rangle \\\\
\langle  8,  7,  5,  2, 4, 13, 17, 20, 25 \rangle \\\\
\langle  4,  7,  5,  2, 8, 13, 17, 20, 25 \rangle \\\\
\langle  7,  4,  5,  2, 8, 13, 17, 20, 25 \rangle \\\\
\langle  2,  4,  5,  7, 8, 13, 17, 20, 25 \rangle \\\\
\langle  5,  4,  2,  7, 8, 13, 17, 20, 25 \rangle \\\\
\langle  2,  4,  5,  7, 8, 13, 17, 20, 25 \rangle \\\\
\langle  4,  2,  5,  7, 8, 13, 17, 20, 25 \rangle \\\\
\langle  2,  4,  5,  7, 8, 13, 17, 20, 25 \rangle
\end{aligned}
$$


## 6.4-2

> Argue the correctness of $\text{HEAPSORT}$ using the following loop invariant:
>
> At the start of each iteration of the **for** loop of lines 2-5, the subarray $A[1..i]$ is a max-heap containing the $i$ smallest elements of $A[1..n]$, and the subarray $A[i + 1..n]$ contains the $n - i$ largest elements of $A[1..n]$, sorted.

**Initialization:** The subarray $A[i + 1..n]$ is empty, thus the invariant holds.

**Maintenance:** $A[1]$ is the largest element in $A[1..i]$ and it is smaller than the elements in $A[i + 1..n]$. When we put it in the $i$th position, then $A[i..n]$ contains the largest elements, sorted. Decreasing the heap size and calling $\text{MAX-HEAPIFY}$ turns $A[1..i - 1]$ into a max-heap. Decrementing $i$ sets up the invariant for the next iteration.

**Termination:** After the loop $i = 1$. This means that $A[2..n]$ is sorted and $A[1]$ is the smallest element in the array, which makes the array sorted.


## 6.4-3

---

**Short Answer:**  
For both an array already sorted in increasing order and an array already sorted in decreasing order, the running time of HEAPSORT remains \( O(n \log n) \).

**Detailed Explanation:**  
The HEAPSORT algorithm consists of two main phases:

1. **Building the Heap:**  
   This phase constructs a max-heap from the input array. The standard heap-building procedure (using the bottom-up approach) takes \( O(n) \) time regardless of the initial order of the elements. This is because the heap construction algorithm "heapifies" subtrees starting from the lowest-level internal nodes up to the root, and the amount of work done at each node is proportional to the height of the subtree. Summing this work across all nodes results in a linear time complexity for building the heap.

2. **Extracting Elements to Sort:**  
   After the heap is built, HEAPSORT repeatedly extracts the maximum element and places it at the end of the array, then reduces the heap size by one and calls `heapify` to restore the heap property. Each extraction involves:
   - Removing the root (maximum element) and swapping it with the last element in the heap.
   - Calling `heapify` on the root to maintain the max-heap property.

   Each `heapify` call runs in \( O(\log n) \) time because it may need to "percolate" down through a path in the heap of height \(\log n\).

   Since we perform approximately \( n \) extractions, and each extraction involves an \( O(\log n) \) `heapify` operation, the total time for this phase is \( O(n \log n) \).

**Impact of Initial Order on Running Time:**
- **If the array is already sorted in increasing order:**  
  Even though the input appears sorted, once you build a heap, the data is rearranged into a heap structure. The subsequent steps of extracting the max and `heapify` operations do not become significantly cheaper just because the original input was sorted. The heap does not leverage the "sortedness" of the input in a way that reduces `heapify` operations. Thus, the time complexity remains \( O(n \log n) \).

- **If the array is already sorted in decreasing order:**  
  A similar argument applies. Although the array is in "reverse-sorted" order (which might be intuitive if you think of a max-heap structure), the heap-building process and subsequent extraction steps still perform the same amount of asymptotic work. Each extraction and heapify remains \( O(\log n) \), repeated \( n \) times, resulting again in \( O(n \log n) \).

**Conclusion:**  
HEAPSORT’s runtime complexity does not improve when given a sorted or reverse-sorted array as input. In all cases, its time complexity is dominated by the \( O(n \log n) \) sorting phase.


--- 

# I think the following answer is incorrect. 

## 6.4-3

> What is the running time of $\text{HEAPSORT}$ on an array $A$ of length $n$ that is already sorted in increasing order? What about decreasing order?

Both of them are $\Theta(n\lg n)$.

If the array is sorted in increasing order, the algorithm will need to convert it to a heap that will take $O(n)$. Afterwards, however, there are $n - 1$ calls to $\text{MAX-HEAPIFY}$ and each one will perform the full $\lg k$ operations. Since:

$$\sum_{k = 1}^{n - 1}\lg k = \lg((n - 1)!) = \Theta(n\lg n).$$

Same goes for decreasing order. $\text{BUILD-MAX-HEAP}$ will be faster (by a constant factor), but the computation time will be dominated by the loop in $\text{HEAPSORT}$, which is $\Theta(n\lg n)$.

---

### The result is amazing !!!  We should study "the Best Case of HeapSort"

#### https://en.wikipedia.org/wiki/Heapsort
#### There are 2 links on the wikipedia page that I think are very interesting.
https://www.math.cmu.edu/~af1p/Texfiles/Best.pdf
https://www.cs.princeton.edu/techreports/1990/293.pdf

---

# TODO:
## 6.4-3
## 6.4-4
## 6.4-5

