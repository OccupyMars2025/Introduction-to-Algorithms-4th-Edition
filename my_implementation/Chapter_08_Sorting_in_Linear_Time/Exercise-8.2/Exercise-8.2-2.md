
- **Assume** two elements \( A[i] \) and \( A[j] \) have the same key \( x \) with \( i < j \).
- During the **right-to-left** iteration:
  - \( A[j] \) is placed **first** at position \( C[x] \).
  - \( C[x] \) is decremented, so \( A[i] \) is placed **before** \( A[j] \) 
- Therefore, \( A[i] \) appears **before** \( A[j] \) in the output array \( B \), preserving the original order.

