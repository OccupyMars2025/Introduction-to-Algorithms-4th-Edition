### **Understanding the Running Time of Bucket Sort**

**Bucket Sort** is an efficient sorting algorithm that distributes elements into a number of buckets, sorts each bucket individually, and then concatenates the sorted buckets to produce the final sorted array. While **Bucket Sort** can achieve excellent average-case performance, its worst-case running time can degrade significantly under certain conditions.

#### **1. Worst-Case Running Time of Bucket Sort: \(\Theta(n^2)\)**

**Why is the Worst-Case Running Time \(\Theta(n^2)\)?**

- **Distribution of Elements into Buckets:**
  - In an ideal scenario, elements are uniformly distributed across all buckets, ensuring that each bucket contains a small number of elements. This allows each bucket to be sorted quickly, often in constant or linear time.
  - **However**, in the **worst case**, all \( n \) elements can end up in a single bucket. This scenario typically arises when the input data is not uniformly distributed, leading to highly imbalanced buckets.

- **Sorting the Buckets:**
  - If all elements reside in one bucket, the sorting algorithm used for that bucket must handle \( n \) elements.
  - **Common Sorting Algorithms in Buckets:**
    - **Insertion Sort:** Often used for its efficiency with small datasets. Its average and worst-case time complexities are \( O(n) \) and \( O(n^2) \) respectively.
    - **Other Quadratic Sorts:** Algorithms like **Bubble Sort** or **Selection Sort** also exhibit \( O(n^2) \) worst-case performance.

- **Total Running Time:**
  - **Bucket Distribution:** \( O(n) \) time to distribute all elements into buckets.
  - **Sorting Buckets:** In the worst case, one bucket contains all \( n \) elements, requiring \( O(n^2) \) time to sort.
  - **Concatenation:** \( O(n) \) time to merge the sorted buckets.
  - **Overall Worst-Case Time Complexity:** \( O(n) + O(n^2) + O(n) = O(n^2) \), which simplifies to \(\Theta(n^2)\).

**Illustrative Example:**

Consider sorting the array \( A = [1, 1, 1, \ldots, 1] \) (all elements are identical):

1. **Bucket Distribution:** All \( n \) elements are placed into a single bucket.
2. **Sorting the Bucket:** Using Insertion Sort on this bucket results in \( O(n^2) \) comparisons and shifts.
3. **Concatenation:** Merging the single bucket back into the main array takes \( O(n) \) time.

Thus, the total running time is dominated by the \( O(n^2) \) sorting step.

#### **2. Improving Worst-Case Running Time to \( O(n \log n) \) While Preserving Linear Average-Case Time**

To mitigate the worst-case scenario without compromising the average-case efficiency, a **simple modification** can be applied to the Bucket Sort algorithm:

**Change: Use a More Efficient Sorting Algorithm for Each Bucket**

- **Replace Insertion Sort with a \( O(k \log k) \) Time Sorting Algorithm:**
  - **Examples:**
    - **Merge Sort:** A stable, comparison-based sorting algorithm with \( O(k \log k) \) worst-case time.
    - **Heap Sort:** An in-place, comparison-based sorting algorithm with \( O(k \log k) \) worst-case time.
    - **Quick Sort with Good Pivot Selection:** Ensures \( O(k \log k) \) average and \( O(k \log k) \) worst-case time when implemented with techniques like median-of-medians for pivot selection.
  
- **Benefits:**
  - **Balanced Buckets:** Even if all \( n \) elements end up in a single bucket, using Merge Sort or Heap Sort ensures that sorting this bucket takes \( O(n \log n) \) time instead of \( O(n^2) \).
  - **Preserved Average-Case Efficiency:** When elements are uniformly distributed, each bucket contains \( O(1) \) or \( O(\log n) \) elements, making the sorting of each bucket still efficient (linear or near-linear time).

**Modified Bucket Sort Procedure:**

1. **Initialize Buckets:**
   - Create \( m \) buckets based on the range of input data.

2. **Distribute Elements into Buckets:**
   - Iterate through the input array and place each element into its corresponding bucket.
   - **Time Complexity:** \( O(n) \)

3. **Sort Each Bucket Using an Efficient Algorithm (e.g., Merge Sort):**
   - Iterate through each bucket and apply Merge Sort.
   - **Time Complexity per Bucket:** \( O(k \log k) \), where \( k \) is the number of elements in the bucket.
   - **Total Time for Sorting All Buckets:** \( O(n \log k) \) where \( k \) is the average number of elements per bucket.

4. **Concatenate Sorted Buckets:**
   - Merge all the sorted buckets into a single sorted array.
   - **Time Complexity:** \( O(n) \)

5. **Overall Time Complexity:**
   - **Worst-Case:** \( O(n \log n) \) (all elements in one bucket)
   - **Average-Case:** \( O(n) \) (assuming uniform distribution and small \( k \))

**Why This Change Works:**

- **Preserving Linear Average-Case Time:**
  - When the input elements are uniformly distributed, each bucket contains a small number of elements (\( k \approx n/m \)), keeping the sorting time per bucket minimal.
  - The total sorting time remains \( O(n) \) since \( m \) is proportional to \( n \).

- **Handling Worst-Case Scenarios:**
  - Even if all \( n \) elements fall into a single bucket, using Merge Sort ensures that the sorting step takes \( O(n \log n) \) time instead of \( O(n^2) \).

**Alternative Approach: Hybrid Bucket Sort**

Another approach to ensuring \( O(n \log n) \) worst-case time is to:

- **Use a Dynamic Structure for Buckets:**
  - Implement each bucket as a balanced binary search tree (e.g., Red-Black Tree) or another data structure that guarantees \( O(\log k) \) insertion time.
  - This ensures that even if all elements end up in one bucket, insertion and sorting operations remain efficient.

### **Summary**

- **Original Bucket Sort:**
  - **Worst-Case Running Time:** \(\Theta(n^2)\) when all elements are concentrated in a single bucket.
  
- **Modified Bucket Sort:**
  - **Change:** Replace the sorting algorithm used within each bucket (e.g., switch from Insertion Sort to Merge Sort).
  - **Resulting Worst-Case Running Time:** \( O(n \log n) \) even in the worst case.
  - **Average-Case Running Time:** Preserved at \( O(n) \) due to efficient sorting when buckets are balanced.

### **Final Recommendations**

For applications where the worst-case performance of Bucket Sort is a concern, implementing the modified version with a more efficient sorting algorithm for each bucket is advisable. This simple change ensures robust performance across all input scenarios without sacrificing the linear average-case efficiency that makes Bucket Sort attractive for large datasets with uniformly distributed elements.