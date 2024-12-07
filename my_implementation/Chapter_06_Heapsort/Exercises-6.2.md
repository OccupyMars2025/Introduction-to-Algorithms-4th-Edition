## 6.2-1

> Using figure 6.2 as a model, illustrate the operation of $\text{MAX-HEAPIFY}(A, 3)$ on the array $A = \langle 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 \rangle$.

$$
\begin{aligned}
\langle 27, 17, 3,  16, 13, 10,1, 5, 7, 12, 4, 8, 9, 0 \rangle \\\\
\langle 27, 17, 10, 16, 13, 3, 1, 5, 7, 12, 4, 8, 9, 0 \rangle \\\\
\langle 27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0 \rangle \\\\
\end{aligned}
$$


## 6.2-2
![alt text](Exercise-6.2-2.png)

## 6.2-3
refer to my_implementation/Chapter_06_Heapsort/Section-6.2-Maintaining-the-heap-property/min_heap.py


## 6.2-5

> What is the effect of calling $\text{MAX-HEAPIFY}(A, i)$ for $i > A.heap\text-size / 2$?

No effect. In that case, it is a leaf. Both $\text{LEFT}$ and $\text{RIGHT}$ return values that fail the comparison with the heap size and $i$ is stored in largest. Afterwards the procedure just returns.


## 6.2-6
refer to my_implementation/Chapter_06_Heapsort/Section-6.2-Maintaining-the-heap-property/max_heap.py  
    def max_heapify_iterative_version(self, i: int) -> None

## 6.2-7

> Show that the worst-case running time of $\text{MAX-HEAPIFY}$ on a heap of size $n$ is $\Omega(\lg n)$. ($\textit{Hint:}$ For a heap with $n$ nodes, give node values that cause $\text{MAX-HEAPIFY}$ to be called recursively at every node on a simple path from the root down to a leaf.)

Consider the heap resulting from $A$ where $A[1] = 1$ and $A[i] = 2$ for $2 \le i \le n$. Since $1$ is the smallest element of the heap, it must be swapped through each level of the heap until it is a leaf node. Since the heap has height $\lfloor \lg n\rfloor$, $\text{MAX-HEAPIFY}$ has worst-case time $\Omega(\lg n)$.
