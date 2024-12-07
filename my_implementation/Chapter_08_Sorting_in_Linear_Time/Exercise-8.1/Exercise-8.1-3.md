**Short Answer:**  
No comparison-based sorting algorithm can run in linear time on at least half of all \( n! \) permutations. In fact, for any fraction that does not vanish super-exponentially fast with \( n \), no comparison sort can run in linear time on that fraction of the inputs. In particular:

- For a fixed positive fraction such as \(1/2\) (half the inputs), or even as small as \(1/n\), no comparison sort can run in \(O(n)\) time on that fraction of the permutations.
- Even for a fraction as small as \(1/2^n\), no comparison sort can achieve linear time on that fraction of permutations for sufficiently large \(n\).

**Detailed Explanation and Proof:**

1. **Background: Comparison Sorts and Decision Trees**  
   Any comparison-based sorting algorithm can be modeled as a binary decision tree. Each internal node corresponds to a comparison between two elements, and each leaf corresponds to a possible outcome (a particular ordering of the input). Since we must distinguish among all \( n! \) permutations, the decision tree must have at least \( n! \) leaves.

2. **Depth of Leaves and Running Time**  
   The worst-case running time of the sorting algorithm corresponds to the maximum depth of any leaf in the decision tree. More importantly, the time to produce the correct sorted order for a particular permutation corresponds to the depth of the leaf representing that permutation. A leaf at depth \( d \) means that on that particular input, the algorithm performed \( d \) comparisons.

   If we want a comparison sort to run in linear time (say at most \( c n \) comparisons for some constant \( c \)) on a fraction of the inputs, we are essentially saying that a large fraction of the leaves must lie at depth at most \( c n \).

3. **Counting Leaves at Small Depth**  
   The total number of leaves at depth at most \( c n \) is at most \( 2^{c n}\). (Based on the fact that a binary tree of height h has at most \( 2^{n}\) leaves. This fact can be shown by induction on the depth of the tree)

   Thus, if an algorithm runs in \( O(n) \) time on a set \( S \) of permutations, the leaves corresponding to those permutations are all at depth \(\leq c n\), and hence:
   \[
   |S| \leq 2^{c n}.
   \]

4. **Comparing to the Total Number of Permutations \( n! \)**  
   We know that \( n! \) grows super-exponentially in \( n \). Using Stirling’s approximation:
   \[
   n! \approx \sqrt{2 \pi n} \left(\frac{n}{e}\right)^n.
   \]
   For large \( n \), \(\left(\frac{n}{e}\right)^n\) grows much faster than \( 2^{c n} \). Indeed, comparing \( (n/e)^n \) and \( 2^{c n} \):
   \[
   \frac{n!}{2^{c n}} \approx \frac{\sqrt{2 \pi n} (n/e)^n}{2^{c n}} = \sqrt{2 \pi n} \left(\frac{n}{e \cdot 2^c}\right)^n.
   \]

   As \( n \to \infty \), since \( n/(e \cdot 2^c) \to \infty \), the ratio \((n/(e \cdot 2^c))^n\) grows without bound. Thus:
   \[
   n! \gg 2^{c n} \quad \text{as } n \to \infty.
   \]

5. **Implications for Large Fractions of Inputs:**

   - **Half the Inputs (Fraction = 1/2):**  
     Suppose we wanted at least half of the permutations to be sorted in \( O(n) \) time. That would mean:
     \[
     |S| \geq \frac{n!}{2}.
     \]
     But we know \( |S| \leq 2^{c n} \). Combining these:
     \[
     2^{c n} \geq \frac{n!}{2}.
     \]
     For large \( n \), this is impossible because \( n! \) grows too quickly. Thus, no comparison sort can achieve linear time on at least half of the inputs.

   - **A Smaller Fraction, Such as \( 1/n \):**  
     Even if we ask for only \( n!/n \) permutations to be sorted in \( O(n) \) time, we get:
     \[
     2^{c n} \geq \frac{n!}{n}.
     \]
     Using the same growth argument, \( n! \) dominates \( 2^{c n} \) by an enormous margin, making this equality impossible for large \( n \).

   - **An Even Smaller Fraction, Such as \( 1/2^n \):**  
     Let’s try \( |S| \geq \frac{n!}{2^n} \). Then:
     \[
     2^{c n} \geq \frac{n!}{2^n}.
     \]
     Rearranging:
     \[
     n! \leq 2^{(c+1) n}.
     \]
     impossible for large \( n \).

6. **Conclusion:**
   The key point is the disparity in growth rates. The factorial \( n! \) grows super-exponentially, while the number of leaves at a given linear depth \( c n \) grows only exponentially. No matter how we choose a fraction that does not vanish extremely fast (faster than any function like \( (n/(e \cdot 2^c))^{-n} \)), we cannot accommodate that many permutations at linear depth.

   **In summary:**
   - No comparison sort can be linear-time for at least half of the inputs.
   - Nor can it be linear-time for a fraction like \( 1/n \) of the inputs.
   - Nor even for a fraction as small as \( 1/2^n \) of the inputs, for sufficiently large \( n \).

   Hence, any “fast on a large fraction of all permutations” property must fail for comparison-based sorting if we demand a truly linear-time behavior.