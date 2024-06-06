'''
page 161
Problem 5.3-3:
Consider the PERMUTE-WITH-ALL procedure on the facing page, which instead
of swapping element A[i] with a random element from the subarray A[i:n], swaps
it with a random element from anywhere in the array. Does PERMUTE-WITH-ALL
produce a uniform random permutation? Why or why not?

https://walkccc.me/CLRS/Chap05/5.3/
https://www.quora.com/Why-does-shuffling-array-by-iterating-over-it-and-swapping-it-with-a-random-element-between-0-to-the-last-element-of-the-array-not-produce-a-uniformly-distributed-shuffle

'''

import numpy as np
import sympy as sp


def generate_final_transition_matrix(n:int) -> np.ndarray:
    '''
    https://www.quora.com/Why-does-shuffling-array-by-iterating-over-it-and-swapping-it-with-a-random-element-between-0-to-the-last-element-of-the-array-not-produce-a-uniformly-distributed-shuffle
    
    generate the final transition matrix for n-element array
    '''
    final_transition_matrix = np.eye(n)
    
    for iteration in range(n):
        transition_matrix = np.zeros((n, n))
        for j in range(n):
            transition_matrix[iteration, j] = 1.0 / n
        for i in range(n):  
            if i == iteration:
                continue
            for j in range(n):
                if j == iteration:
                    transition_matrix[i, j] = 1.0 / n
                elif j == i:
                    transition_matrix[i, j] = 1 - 1.0 / n
        final_transition_matrix = np.matmul(final_transition_matrix, transition_matrix)
    
    return final_transition_matrix


def generate_final_transition_matrix_sympy(n: int) -> sp.Matrix:
    '''
    generate the final transition matrix for n-element array using sympy

    '''
    final_transition_matrix = sp.eye(n)
    
    one_over_n = sp.Rational(1, n)
    
    for iteration in range(n):
        transition_matrix = sp.zeros(n, n)
        
        for j in range(n):
            transition_matrix[iteration, j] = one_over_n
        
        for i in range(n):
            if i == iteration:
                continue
            for j in range(n):
                if j == iteration:
                    transition_matrix[i, j] = one_over_n
                elif j == i:
                    transition_matrix[i, j] = 1 - one_over_n
        
        final_transition_matrix = final_transition_matrix * transition_matrix
    
    return final_transition_matrix


if __name__ == '__main__':
    n = 3
    final_transition_matrix = generate_final_transition_matrix(n)
    print(f'final transition matrix:\n {final_transition_matrix}')
    
    final_transition_matrix_sympy = generate_final_transition_matrix_sympy(n)
    sp.pprint(final_transition_matrix_sympy) 