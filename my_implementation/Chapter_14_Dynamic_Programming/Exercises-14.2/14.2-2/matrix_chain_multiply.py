from typing import List, Tuple, Dict
import random


def find_optimal_parenthesization_helper_v2(dimensions: List[int]) -> Tuple[Dict[Tuple[int, int], int], Dict[Tuple[int, int], int]]:
    """
    dynamic programming approach (bottom-up) to the matrix chain multiplication problem:
    A1 * A2 * A3 * ... * An

    Args:
        dimensions (List[int]): len(dimensions) is n + 1
        
    Returns:
        Tuple[Dict[Tuple[int, int], int], Dict[Tuple[int, int], int]]: 
            Dict[Tuple[int, int], int]: least_scalar_multiplications
                key: the range of the chain to consider, inclusive. 
                value: the minimum number of scalar multiplications required to multiply the chain of matrices in this range
            Dict[Tuple[int, int], int]: optimal_first_cut
                key: the range of the chain to consider, inclusive. 
                value: the index at which to cut the chain , and it is the optimal first cut
    """
    least_scalar_multiplications: Dict[Tuple[int, int], int] = {}
    optimal_first_cut: Dict[Tuple[int, int], int] = {}
    
    # base case: 1 matrix
    for i in range(1, len(dimensions)):
        least_scalar_multiplications[(i, i)] = 0
        
    # base case: 2 matrices
    for i in range(1, len(dimensions) - 1):
        least_scalar_multiplications[(i, i+1)] = dimensions[i-1] * dimensions[i] * dimensions[i+1]
        
    for num_matrices in range(3, len(dimensions)):
        for start_index in range(1, len(dimensions) - num_matrices + 1):
            end_index = start_index + num_matrices - 1
            
            current_least_scalar_multipications = float('inf')
            current_optimal_first_cut = -1
            for cut_index in range(start_index, end_index):
                left_side_least_scalar_multiplications = least_scalar_multiplications[(start_index, cut_index)]
                right_side_least_scalar_multiplications = least_scalar_multiplications[(cut_index + 1, end_index)]
                total_scalar_multipications = left_side_least_scalar_multiplications + right_side_least_scalar_multiplications + \
                    dimensions[start_index - 1] * dimensions[cut_index] * dimensions[end_index]
                if total_scalar_multipications < current_least_scalar_multipications :
                    current_least_scalar_multipications = total_scalar_multipications
                    current_optimal_first_cut = cut_index
            least_scalar_multiplications[(start_index, end_index)] = current_least_scalar_multipications
            optimal_first_cut[(start_index, end_index)] = current_optimal_first_cut
    
    return least_scalar_multiplications, optimal_first_cut


def multiply_two_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    rows_a = len(A)
    cols_a = len(A[0])
    rows_b = len(B)
    cols_b = len(B[0])
    
    assert cols_a == rows_b
    
    C = [[0]*cols_b for _ in range(rows_a)]
    
    for row in range(rows_a):
        for col in range(cols_b):
            for k in range(cols_a):
                C[row][col] += A[row][k] * B[k][col]
                
    return C


def matrix_chain_multiply_stupid(matrices: Tuple[List[List[int]]]) -> List[List[int]]:
    for i in range(len(matrices)-1):
        assert len(matrices[i][0]) == len(matrices[i+1])
        
    product = matrices[0]
    for i in range(1, len(matrices)):
        product = multiply_two_matrices(product, matrices[i])
        
    return product


def matrix_chain_multiply_optimal(matrices: Tuple[List[List[int]]], optimal_first_cuts: Dict[Tuple[int, int], int], start_index: int, end_index: int) -> List[List[int]]:
    if start_index == end_index:
        return matrices[start_index - 1]
    
    if end_index - start_index == 1:
        return multiply_two_matrices(matrices[start_index - 1], matrices[end_index - 1])
    
    assert end_index - start_index >= 2
    
    optimal_cut = optimal_first_cuts[(start_index, end_index)]
    
    left_matrix = matrix_chain_multiply_optimal(matrices, optimal_first_cuts, start_index, optimal_cut)
    right_matrix = matrix_chain_multiply_optimal(matrices, optimal_first_cuts, optimal_cut + 1, end_index)
    
    return multiply_two_matrices(left_matrix, right_matrix)


def generate_matrix_chain(dimensions: List[int]) -> Tuple[List[List[int]]]:
    matrices = []
    for i in range(1, len(dimensions)):
        matrix = [random.choices(range(-100, 100), k=dimensions[i]) for _ in range(dimensions[i-1])]
        matrices.append(matrix)
    return tuple(matrices)


def test():
    for num_matrices in range(1, 30):
        print("num_matrices", num_matrices)
        dimensions = random.choices(range(1, 100), k=num_matrices + 1)
        print(f"{dimensions=}")
        matrices = generate_matrix_chain(dimensions)
        least_scalar_multiplications, optimal_first_cuts = find_optimal_parenthesization_helper_v2(dimensions)
        result_matrix = matrix_chain_multiply_optimal(matrices, optimal_first_cuts, 1, num_matrices)
        # print(f"least_scalar_multiplications={least_scalar_multiplications}, optimal_first_cuts={optimal_first_cuts}")
        
        result_matrix_stupid = matrix_chain_multiply_stupid(matrices)
        # print(f"result_matrix={result_matrix}, result_matrix_stupid={result_matrix_stupid}")
        assert result_matrix == result_matrix_stupid
        assert len(result_matrix) == dimensions[0]
        assert len(result_matrix[0]) == dimensions[-1]
        for row in range(1, len(result_matrix)):
            assert len(result_matrix[row]) == dimensions[-1]

        print("\n")
        
        
if __name__ == "__main__":
    test()