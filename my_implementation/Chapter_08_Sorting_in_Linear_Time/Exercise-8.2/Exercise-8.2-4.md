To **delve** into the proof of the loop invariant for **COUNTING-SORT**, consider the following:

**Invariant Statement:** *At the start of each iteration of the `for` loop (lines 11–13), the last element in \( A \) with value \( i \) that has not yet been copied into \( B \) belongs in \( B[C[i]] \).*

**Proof by Induction:**

1. **Base Case:** Before the loop begins (i.e., before the first iteration), no elements have been copied. Therefore, the last element with value \( i \) in \( A \) should indeed be placed at position \( C[i] \) in \( B \), which holds the correct position based on the count array.

2. **Inductive Step:** Assume the invariant holds at the start of the \( m \)-th iteration for some \( i = m \). During this iteration, the algorithm places the last unplaced element with value \( m \) into \( B[C[m]] \) and decrements \( C[m] \). After this step, the next unplaced element with value \( m \) will correctly correspond to the updated \( C[m] \), maintaining the invariant for the next iteration.

3. **Termination:** After the final iteration, all elements have been placed correctly in \( B \), and the invariant ensures that each element is positioned at its ultimate correct index, preserving stability.

Thus, by **induction**, the loop invariant holds true throughout the execution of the loop, ensuring that each element is placed in its rightful position in the output array \( B \).