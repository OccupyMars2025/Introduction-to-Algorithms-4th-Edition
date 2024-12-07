
> A **_probability distribution function_** $P(x)$ for a random variable $X$ is defined by $P(x) = \Pr\\{X \le x\\}$. Suppose that we draw a list of $n$ random variables $X_1, X_2, \ldots, X_n$ from a continuous probability distribution function $P$ that is computable in $O(1)$ time. Give an algorithm that sorts these numbers in linear average-case time.

Bucket sort by $p_i$, so we have $n$ buckets: $[p_0, p_1), [p_1, p_2), \dots, [p_{n - 1}, p_n)$. Note that not all buckets are the same size, which is ok as to ensure linear run time, the inputs should on average be uniformly distributed amongst all buckets, of which the intervals defined with $p_i$ will do so.

$p_i$ is defined as follows:

$$P(p_i) = \frac{i}{n}.$$
