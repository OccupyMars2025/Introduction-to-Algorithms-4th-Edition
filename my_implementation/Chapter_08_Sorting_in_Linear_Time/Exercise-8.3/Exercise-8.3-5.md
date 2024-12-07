To sort \( n \) integers within the range \( 0 \) to \( n^3 - 1 \) in \( O(n) \) time, we can employ a specialized **Radix Sort** approach. This method leverages the properties of the input range and the efficiency of radix-based sorting to achieve linear time complexity.

### **Overview**

- **Radix Sort** is a non-comparative sorting algorithm that sorts integers by processing individual digits.
- By choosing an appropriate **base** (radix), we can minimize the number of passes needed and ensure that each pass operates in linear time.
- Given the range \( 0 \) to \( n^3 - 1 \), we can design a radix sort with a fixed number of digits, enabling \( O(n) \) sorting time.

### **Detailed Approach**

#### **1. Understanding the Input Range**

- **Range**: \( 0 \) to \( n^3 - 1 \)
- **Number Representation**: Each integer can be represented in base \( n \) with exactly 3 digits:
  \[
  \text{Number} = d_2 \times n^2 + d_1 \times n + d_0
  \]
  where \( 0 \leq d_0, d_1, d_2 < n \).

#### **2. Choosing the Radix and Number of Passes**

- **Radix (Base)**: \( n \)
- **Number of Digits**: \( 3 \) (since \( n^3 - 1 \) requires 3 digits in base \( n \))
- **Sorting Passes**: Perform **3 passes**, one for each digit (from least significant digit to most significant digit).

#### **3. Implementing Radix Sort with Base \( n \)**

**Step-by-Step Procedure:**

1. **Initialization**:
   - Let \( A[1 \ldots n] \) be the input array containing integers in the range \( 0 \) to \( n^3 - 1 \).
   - Let \( B[1 \ldots n] \) be the output array.
   - We will perform three **stable** sorting passes, one for each digit \( d_0 \), \( d_1 \), and \( d_2 \).

2. **Define a Stable Sorting Subroutine**:
   - Use **Counting Sort** as the stable sorting algorithm for each digit.
   - Since the radix is \( n \), Counting Sort will operate in \( O(n) \) time for each pass.

3. **Extract Digits**:
   - For each number \( x \) in \( A \), extract the digits:
     \[
     d_0 = x \mod n
     \]
     \[
     d_1 = \left( \left\lfloor \frac{x}{n} \right\rfloor \right) \mod n
     \]
     \[
     d_2 = \left\lfloor \frac{x}{n^2} \right\rfloor
     \]
   - These digits correspond to the units, \( n \)'s place, and \( n^2 \)'s place, respectively.

4. **Perform Sorting Passes**:

   **Pass 1: Sort by Least Significant Digit (\( d_0 \))**
   
   - Apply Counting Sort to sort the array based on \( d_0 \).
   - Since Counting Sort is stable, the relative order of elements with the same \( d_0 \) is preserved.
   
   **Pass 2: Sort by Middle Digit (\( d_1 \))**
   
   - Apply Counting Sort to the output of Pass 1, sorting based on \( d_1 \).
   - Stability ensures that the ordering from Pass 1 (\( d_0 \)) is maintained within groups of identical \( d_1 \).
   
   **Pass 3: Sort by Most Significant Digit (\( d_2 \))**
   
   - Apply Counting Sort to the output of Pass 2, sorting based on \( d_2 \).
   - Stability ensures that both \( d_1 \) and \( d_0 \) orderings are preserved within groups of identical \( d_2 \).

5. **Final Output**:
   - After the third pass, the array \( B \) is fully sorted in ascending order.

#### **4. Pseudocode Implementation**

Below is the pseudocode for sorting \( n \) integers in the range \( 0 \) to \( n^3 - 1 \) using Radix Sort with base \( n \):

```plaintext
RADIX-SORT-BASE-N(A, n)

Input:
    A[1 .. n] - array of integers, 0 ≤ A[j] < n^3

Output:
    B[1 .. n] - sorted array in ascending order

Procedure:
    // Initialize output array
    let B[1 .. n] be a new array

    // Define a stable counting sort for a specific digit
    PROCEDURE COUNTING-SORT-DIGIT(A, B, n, digit, base)
        // Initialize count array
        let C[0 .. base - 1] be an array of zeros

        // Count occurrences of each digit
        for j = 1 to n
            d = (A[j] // base^digit) % base
            C[d] = C[d] + 1

        // Compute cumulative counts
        for i = 1 to base - 1
            C[i] = C[i] + C[i - 1]

        // Place elements into output array in reverse to maintain stability
        for j = n downto 1
            d = (A[j] // base^digit) % base
            B[C[d]] = A[j]
            C[d] = C[d] - 1
    END PROCEDURE

    // Perform 3 passes for digits 0, 1, 2
    for digit = 0 to 2
        COUNTING-SORT-DIGIT(A, B, n, digit, n)
        // Prepare for next pass
        // Swap A and B for next iteration
        let temp = A
        A = B
        B = temp
    end for

    // After final pass, A contains the sorted array
    return A
```

**Explanation of the Pseudocode:**

- **COUNTING-SORT-DIGIT**:
  - **digit**: Specifies which digit to sort by (0 for least significant, 1 for middle, 2 for most significant).
  - **base**: Set to \( n \), aligning with our radix choice.
  - **Counting Phase**: Counts the occurrences of each digit.
  - **Cumulative Phase**: Transforms counts to cumulative counts to determine positions.
  - **Placement Phase**: Places elements into the output array \( B \) in a stable manner by iterating from the end to maintain stability.

- **Radix Sort Passes**:
  - Performs three passes, one for each digit.
  - After each pass, swaps the roles of \( A \) and \( B \) to prepare for the next digit's sorting.

#### **5. Time and Space Complexity Analysis**

- **Counting Sort per Digit**:
  - **Time**: \( O(n) \) for each pass (due to base \( n \) and \( n \) elements).
  - **Space**: \( O(n) \) for the count array \( C \) and the output array \( B \).

- **Total Passes**: 3 (constant number).

- **Overall Time Complexity**:
  \[
  O(3n) = O(n)
  \]

- **Overall Space Complexity**:
  \[
  O(n) \text{ (for auxiliary arrays)}
  \]

### **Why This Approach Achieves \( O(n) \) Time**

1. **Fixed Number of Passes**: The number of digits (3) is constant relative to \( n \), ensuring that the total number of operations scales linearly with \( n \).

2. **Linear-Time Stable Sorts**: Each Counting Sort pass operates in \( O(n) \) time due to the chosen base \( n \), and stability is maintained to preserve the ordering across digits.

3. **Efficient Digit Extraction**: Extracting digits using arithmetic operations (division and modulo) is performed in constant time per element per digit.

### **Example Walkthrough**

Let's illustrate the sorting process with a small example.

**Suppose \( n = 4 \). We want to sort the array \( A = [15, 3, 8, 7] \), where each element is in the range \( 0 \) to \( 4^3 - 1 = 63 \).**

1. **Representation in Base 4**:
   \[
   15 = 3 \times 4^1 + 3 \times 4^0 = (3, 3, 0)
   \]
   \[
   3 = 0 \times 4^2 + 0 \times 4^1 + 3 \times 4^0 = (0, 0, 3)
   \]
   \[
   8 = 0 \times 4^2 + 2 \times 4^1 + 0 \times 4^0 = (0, 2, 0)
   \]
   \[
   7 = 0 \times 4^2 + 1 \times 4^1 + 3 \times 4^0 = (0, 1, 3)
   \]

2. **Pass 1: Sort by \( d_0 \) (Units Place)**
   
   - **Digits**: \( [3, 3, 0, 3] \)
   - **After Counting Sort**: \( [8, 15, 3, 7] \)
   
   *Explanation*: Elements with \( d_0 = 0 \) come first (8), followed by elements with \( d_0 = 3 \). Stability ensures that 15 precedes 3 and 3 precedes 7 among elements with \( d_0 = 3 \).

3. **Pass 2: Sort by \( d_1 \) (Middle Place)**
   
   - **Digits**: \( [2, 3, 0, 1] \)
   - **After Counting Sort**: \( [3, 7, 8, 15] \)
   
   *Explanation*: Elements with \( d_1 = 0 \) (3) come first, followed by \( d_1 = 1 \) (7), \( d_1 = 2 \) (8), and finally \( d_1 = 3 \) (15). Stability maintains the relative order from the previous pass.

4. **Pass 3: Sort by \( d_2 \) (Most Significant Place)**
   
   - **Digits**: \( [0, 0, 0, 0] \)
   - **After Counting Sort**: \( [3, 7, 8, 15] \)
   
   *Explanation*: All elements have \( d_2 = 0 \), so the order remains unchanged from the previous pass.

5. **Final Sorted Array**: \( [3, 7, 8, 15] \)

### **Conclusion**

By utilizing **Radix Sort** with a carefully chosen base \( n \) and exploiting the fixed number of digits required to represent numbers within the specified range, we achieve an efficient \( O(n) \) sorting algorithm for \( n \) integers in the range \( 0 \) to \( n^3 - 1 \). This method ensures linear time complexity by performing a constant number of linear-time passes, leveraging the stability of intermediate sorts to maintain correct ordering across digits.