### **Stability of Sorting Algorithms**

**Stability** in sorting algorithms refers to the preservation of the relative order of records with equal keys (i.e., values). A stable sort ensures that if two elements are equal, the one that appeared first in the input list remains first in the sorted output.

Let's evaluate the stability of the given sorting algorithms:

1. **Insertion Sort**: **Stable**
   - **Reason**: Insertion sort builds the final sorted array one item at a time. It inserts each element into its proper position by comparing it with the elements before it and shifting larger elements to the right. Since it does not swap equal elements, the original order of equal elements is preserved.

2. **Merge Sort**: **Stable** (in typical implementations)
   - **Reason**: Merge sort divides the array into halves, recursively sorts them, and then merges the sorted halves. During the merge process, when two elements are equal, the element from the left subarray (which appeared earlier in the original array) is chosen first, maintaining their original order.

3. **Heapsort**: **Not Stable**
   - **Reason**: Heapsort builds a heap data structure and repeatedly extracts the maximum (or minimum) element. During the heap construction and extraction, equal elements can be reordered based on their positions in the heap, disrupting their original order.

4. **Quicksort**: **Not Stable**
   - **Reason**: Quicksort selects a pivot and partitions the array such that elements less than the pivot come before it and elements greater come after. Depending on the implementation and the choice of pivot, equal elements can be reordered, leading to instability.

### **Summary of Stability**

| Sorting Algorithm | Stable?  |
|-------------------|----------|
| Insertion Sort    | **Yes**  |
| Merge Sort        | **Yes**  |
| Heapsort          | **No**   |
| Quicksort         | **No**   |

---

### **Making Any Comparison Sort Stable**

To transform any comparison-based sorting algorithm into a **stable** sort, you can employ the following **scheme**:

#### **Scheme: Augment Elements with Original Indices**

1. **Augment Each Element**:
   - Pair each element with its original index in the input array.
   - For example, transform an element `A[j]` into a pair `(A[j], j)`, where `j` is the original position.

2. **Modify the Comparison Function**:
   - When comparing two elements `(key1, index1)` and `(key2, index2)`:
     - **Primary Comparison**: Compare `key1` and `key2`.
     - **Secondary Comparison**: If `key1 == key2`, compare `index1` and `index2`.
   - This ensures that if two keys are equal, the element with the smaller original index (i.e., appeared earlier) is considered "smaller."

3. **Apply the Sorting Algorithm**:
   - Use the modified elements and comparison function with your chosen comparison-based sorting algorithm.
   - The algorithm will now sort primarily by key and secondarily by original index, preserving the original order of equal elements.

#### **Example Pseudocode**

```plaintext
// Augment the array with original indices
for j = 1 to n
    A_augmented[j] = (A[j], j)

// Define a comparison function
function compare(a, b):
    if a.key < b.key:
        return -1
    elif a.key > b.key:
        return 1
    else:
        if a.index < b.index:
            return -1
        elif a.index > b.index:
            return 1
        else:
            return 0

// Apply any comparison-based sort using the compare function
Sort(A_augmented, compare)

// Extract the sorted keys from the augmented array
for j = 1 to n
    B[j] = A_augmented[j].key
```

### **Analysis of the Scheme**

1. **Additional Space**:
   - **Space Complexity**: **O(n)**
   - **Reason**: You need to store the original indices alongside each element, effectively doubling the storage requirements for the keys. However, since only a constant additional piece of information (the index) is stored per element, the space complexity remains linear.

2. **Additional Time**:
   - **Time Complexity**: **O(1)** per comparison (constant overhead)
   - **Reason**: The comparison function now performs an extra check when keys are equal. This introduces a constant factor increase in the time per comparison but does not change the overall asymptotic time complexity of the sorting algorithm, which remains **O(n log n)** for most comparison-based sorts.

3. **Overall Impact**:
   - **Time**: The sorting algorithm retains its original time complexity, with a slight constant-factor overhead due to the enhanced comparison.
   - **Space**: Requires linear additional space to store the original indices.

### **Benefits of the Scheme**

- **Generality**: This method can be applied to any comparison-based sorting algorithm, making it a versatile solution for ensuring stability.
- **Simplicity**: The augmentation and modification of the comparison function are straightforward to implement.
- **Effectiveness**: Guarantees that the relative order of equal elements is preserved, ensuring a stable sort.

### **Alternative Scheme: Decorate-Sort-Undecorate (Schwartzian Transform)**

Another common approach to achieving stability is the **Decorate-Sort-Undecorate** (DSU) pattern, also known as the **Schwartzian Transform**. The scheme described above is essentially a form of DSU.

#### **Steps:**

1. **Decorate**: Pair each element with its original index.
2. **Sort**: Sort the augmented elements using a comparison that considers both the key and the original index.
3. **Undecorate**: Extract the sorted keys from the augmented pairs.

This approach is widely used in programming languages that support stable sorting functions by default, such as Python's `sorted()` with the `key` parameter.

### **Conclusion**

- **Stable Sorting Algorithms**:
  - **Insertion Sort** and **Merge Sort** are inherently stable.
  - **Heapsort** and **Quicksort** are not stable but can be modified to be stable.

- **Making Any Comparison Sort Stable**:
  - **Scheme**: Augment each element with its original index and modify the comparison function to use the index as a tiebreaker.
  - **Additional Requirements**: Requires **O(n)** extra space and introduces a **constant-factor** overhead in comparisons, while maintaining the original **time complexity** of the sorting algorithm.

This scheme provides a general and effective method to ensure stability across any comparison-based sorting algorithm, making it a valuable tool in scenarios where the preservation of element order is crucial.