Use induction to prove that radix sort works. Where does your proof need the
assumption that the intermediate sort is stable?

----

Certainly! Let's provide a rigorous inductive proof to demonstrate that Radix Sort correctly sorts a list of non-negative integers. Additionally, we'll identify precisely where the **stability** of the intermediate sorting steps is crucial in the proof.

## **Radix Sort Overview**

Radix Sort processes each digit of the numbers, starting from the least significant digit (LSD) to the most significant digit (MSD). At each step, it uses a stable sorting algorithm (like Counting Sort) to sort the numbers based on the current digit.

## **Inductive Proof That Radix Sort Works**

### **Objective**

Prove that after applying Radix Sort, the list of non-negative integers is sorted in non-decreasing order.

### **Definitions**

- **Stable Sort**: A sorting algorithm is stable if it preserves the relative order of records with equal keys (i.e., if two elements have the same key, they appear in the same order in the sorted output as they do in the input).
  
- **Digit Position (`d`)**: Position of the digit being processed, where `d = 1` corresponds to the least significant digit (units place), `d = 2` to the tens place, and so on.

### **Proof by Mathematical Induction**

We will use induction on the number of digits processed.

#### **Base Case (`d = 1`)**

**Claim:** After sorting based on the least significant digit (units place), the list is sorted with respect to the units digit.

**Proof:**

- **Step:** Perform a stable sort (e.g., Counting Sort) based on the units digit.
  
- **Outcome:** The list is ordered such that numbers are sorted in non-decreasing order based on their units digit.

- **Conclusion:** The base case holds as the list is correctly sorted concerning the first digit.

#### **Inductive Hypothesis**

Assume that after sorting based on the first `k` digits (`d = 1` to `d = k`), the list is correctly sorted in non-decreasing order considering these `k` digits.

#### **Inductive Step (`d = k + 1`)**

**Goal:** Show that after sorting based on the `(k + 1)`-th digit, the list remains correctly sorted considering the first `k + 1` digits.

**Proof:**

1. **Before Sorting:**
   - By the inductive hypothesis, after sorting the first `k` digits, the list is correctly sorted based on these digits.

2. **Sorting on the `(k + 1)`-th Digit:**
   - Apply a stable sort based on the `(k + 1)`-th digit.

3. **Effect of Stable Sort:**
   - **Stability ensures** that if two numbers have the same `(k + 1)`-th digit, their relative order (sorted by the first `k` digits) is preserved.
   
   - **Result:**
     - Numbers are first ordered by the `(k + 1)`-th digit.
     - For numbers with the same `(k + 1)`-th digit, they remain ordered based on the first `k` digits.

4. **Combined Ordering:**
   - The list is now sorted based on the first `k + 1` digits because:
     - The primary key is the `(k + 1)`-th digit.
     - The secondary key (for ties) is the ordering from the first `k` digits.

5. **Conclusion:**
   - After sorting on the `(k + 1)`-th digit, the list is correctly sorted considering the first `k + 1` digits.

6. **Final Step:**
   - By induction, the list is correctly sorted after processing all digits from least significant to most significant.

### **Conclusion of the Inductive Proof**

By mathematical induction, Radix Sort correctly sorts a list of non-negative integers in non-decreasing order.

## **Role of Stability in the Proof**

The **stability** of the intermediate sorting steps (i.e., sorting by each digit) is crucial in the **inductive step**. Here's why:

- **Preservation of Order for Lower Digits:**
  - When sorting by the `(k + 1)`-th digit, stability ensures that among numbers sharing the same digit in this position, their relative order based on the first `k` digits remains unchanged.
  
- **Maintaining Correct Ordering:**
  - Without stability, sorting by a higher digit could disrupt the ordering established by sorting on lower digits, leading to an incorrectly sorted list.

- **Example Illustration:**
  - Consider two numbers: `123` and `223`.
    - After sorting by the units and tens digits, suppose they are ordered as `[123, 223]`.
    - When sorting by the hundreds digit:
      - Both have the same hundreds digit (`1` vs. `2`).
      - Stability ensures that `123` remains before `223` if their `(k + 1)`-th digits are the same.

- **Necessity in the Inductive Step:**
  - The inductive step relies on the assumption that previous digit-based orderings are preserved when sorting on the next digit. Stability guarantees this preservation, ensuring the correctness of the entire Radix Sort.

## **Summary**

- **Inductive Basis:** Correct sorting after the first digit.
  
- **Inductive Step:** Assuming correct sorting after `k` digits, a stable sort on the `(k + 1)`-th digit maintains correct ordering.

- **Stability's Role:** Essential in the inductive step to preserve the order established by previous sorts, ensuring that the entire list is correctly sorted after processing all digits.

Thus, Radix Sort works correctly because each step maintains the ordering established by previous steps through the use of stable sorting algorithms.