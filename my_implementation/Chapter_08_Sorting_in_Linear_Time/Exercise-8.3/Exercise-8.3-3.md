### **Proof of Radix Sort Correctness Using Induction**

Radix Sort is an efficient, non-comparative sorting algorithm that sorts data by processing individual digits. Typically, it operates either from the **Least Significant Digit (LSD)** to the **Most Significant Digit (MSD)** or vice versa. For this proof, we'll focus on the **LSD Radix Sort**, which is more commonly discussed in the context of stable intermediate sorts.

#### **Overview of Radix Sort (LSD Variant)**

1. **Digit Processing Order**: 
   - Start sorting from the least significant digit (rightmost) to the most significant digit (leftmost).
   
2. **Stable Intermediate Sort**:
   - At each digit level, a **stable** sorting algorithm (like Counting Sort) is used to sort the array based on the current digit.
   
3. **Final Output**:
   - After processing all digits, the array is fully sorted.

#### **Objective**

Prove that **Radix Sort correctly sorts an array of integers** using induction, and identify where the **stability of the intermediate sort** is essential in the proof.

#### **Inductive Proof Structure**

1. **Base Case**: Show that Radix Sort correctly sorts the array when only the least significant digit is considered.
   
2. **Inductive Hypothesis**: Assume that after sorting the array based on the first \( d \) digits, the array is correctly sorted with respect to these \( d \) digits.
   
3. **Inductive Step**: Prove that sorting the array based on the \( (d+1) \)-th digit, using a stable sort, results in the array being correctly sorted with respect to the first \( d+1 \) digits.

#### **Detailed Proof**

##### **1. Base Case (\( d = 1 \))**

- **Scenario**: Only the least significant digit is considered.
  
- **Action**: Apply a stable sort (e.g., Counting Sort) to sort the array based on the first digit.
  
- **Correctness**: Since the sort is stable, elements with the same least significant digit maintain their original relative order from the input array.
  
- **Conclusion**: After the first pass, the array is correctly sorted based on the least significant digit.

##### **2. Inductive Hypothesis**

- **Assumption**: After sorting the array based on the first \( d \) digits, the array is **correctly sorted** with respect to these \( d \) digits. That is, for any two elements \( A \) and \( B \):
  
  - If the first \( d \) digits of \( A \) are less than those of \( B \), then \( A \) precedes \( B \) in the array.
  
  - If the first \( d \) digits of \( A \) are equal to those of \( B \), then \( A \) and \( B \) maintain their original relative order from the input array.

##### **3. Inductive Step**

- **Goal**: Show that after sorting based on the \( (d+1) \)-th digit, the array is correctly sorted with respect to the first \( d+1 \) digits.
  
- **Action**: Apply a stable sort to sort the array based on the \( (d+1) \)-th digit.
  
- **Analysis**:
  
  - **Primary Sorting Criterion**: The \( (d+1) \)-th digit.
    
  - **Secondary Sorting Criterion**: The first \( d \) digits (already sorted from the inductive hypothesis).
    
- **Why Stability Matters**:
  
  - **Preservation of Order**: Since the sort is stable, elements with the same \( (d+1) \)-th digit retain their relative order based on the first \( d \) digits.
    
  - **Correct Ordering**: This ensures that within each group of elements sharing the same \( (d+1) \)-th digit, the order established by the first \( d \) digits remains intact.
    
- **Conclusion**:
  
  - After sorting by the \( (d+1) \)-th digit, the array is now correctly sorted based on the first \( d+1 \) digits.
  
  - The stability of the intermediate sort is **crucial** here to maintain the correct ordering established by the previous \( d \) digits.

##### **4. Termination and Overall Correctness**

- **Completion**: Repeat the inductive step for each digit, from \( d = 1 \) up to the maximum number of digits \( D \) in the largest number.
  
- **Final State**: After processing all \( D \) digits, the array is correctly sorted based on all digits.
  
- **By Induction**: Since the base case holds and the inductive step maintains the invariant, Radix Sort correctly sorts the array.

#### **Role of Stability in the Proof**

The **stability** of the intermediate sort is essential in the **inductive step**. Specifically:

- **Preservation of Previous Orderings**: When sorting by the \( (d+1) \)-th digit, a stable sort ensures that elements with the same \( (d+1) \)-th digit maintain their relative order based on the first \( d \) digits.

- **Maintaining Invariant**: This preservation is crucial for the inductive hypothesis to hold after each sorting pass, ensuring that the array remains correctly sorted with respect to all processed digits.

- **Without Stability**: If the intermediate sort were unstable, sorting by the \( (d+1) \)-th digit could disrupt the ordering established by the first \( d \) digits, violating the inductive hypothesis and leading to an incorrectly sorted array.

#### **Summary**

- **Induction Basis**: Correctness after the first digit sort.

- **Inductive Step**: Assuming correctness after \( d \) digits, applying a stable sort on the \( (d+1) \)-th digit maintains correctness.

- **Stability Dependency**: The proof relies on the stability of the intermediate sort to ensure that previous digit orderings are preserved when sorting by subsequent digits.

- **Conclusion**: By induction, Radix Sort correctly sorts the array, provided that each intermediate sort is stable.

#### **Visual Illustration**

Consider sorting the array `[329, 457, 657, 839, 436, 720, 355]` using LSD Radix Sort:

1. **First Pass (Unit Place)**:
   
   - Sort based on the least significant digit.
   
   - Result: `[720, 355, 436, 657, 329, 457, 839]`
   
   - *Note*: Relative order of elements with the same unit digit is preserved.

2. **Second Pass (Tens Place)**:
   
   - Sort based on the tens digit.
   
   - Result: `[720, 329, 436, 839, 355, 657, 457]`
   
   - *Note*: Stability ensures that among elements with the same tens digit, the order from the previous pass is maintained.

3. **Third Pass (Hundreds Place)**:
   
   - Sort based on the hundreds digit.
   
   - Final Sorted Array: `[329, 355, 436, 457, 657, 720, 839]`

Throughout the sorting process, the stability of each intermediate sort ensures that the final array is correctly sorted.

### **Conclusion**

Using induction, we've demonstrated that Radix Sort correctly sorts an array of integers by processing each digit from least to most significant. The **stability of the intermediate sort** is a critical assumption in the inductive step, ensuring that previously established orderings are preserved as new digits are processed. Without this stability, the correctness of Radix Sort cannot be guaranteed.