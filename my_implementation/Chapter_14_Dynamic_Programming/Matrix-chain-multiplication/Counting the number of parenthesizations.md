# page 375

To solve the given recurrence relation for \( P(n) \):

\[
P(n) = \begin{cases}
1 & \text{if } n = 1, \\
\sum_{k=1}^{n-1} P(k)P(n-k) & \text{if } n \geq 2,
\end{cases}
\]
we recognize that this is the recurrence relation for the **Catalan numbers**.

The general formula for the \( n \)-th Catalan number is:

\[
C_n = \frac{1}{n+1} \binom{2n}{n}
\]

Thus, the solution to the recurrence is:

\[
P(n) = C_{n-1} = \frac{1}{n} \binom{2(n-1)}{n-1}
\]

### Explanation:

1. **Recurrence Relation**: The given recurrence resembles the well-known recursive form for Catalan numbers:
   \[
   C_n = \sum_{k=0}^{n-1} C_k C_{n-1-k}
   \]
   In the given recurrence, we have a similar sum structure but it is shifted by 1. This means \( P(n) \) is equivalent to the \( (n-1) \)-th Catalan number.

2. **Closed Form of Catalan Numbers**: The closed form for Catalan numbers is derived from the recurrence and is:
   \[
   C_n = \frac{1}{n+1} \binom{2n}{n}
   \]
   Thus, for the \( P(n) \) recurrence, which corresponds to \( C_{n-1} \), the solution becomes:
   \[
   P(n) = \frac{1}{n} \binom{2(n-1)}{n-1}
   \]

This is the closed-form solution to the recurrence you provided.