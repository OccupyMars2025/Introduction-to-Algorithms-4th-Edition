
import random
from typing import List, Tuple, Dict


def find_optimal_parenthesization_helper(dimensions: List[int], range_of_chain: Tuple[int, int], least_scalar_multiplications: Dict[Tuple[int, int], int] = {}, optimal_first_cut: Dict[Tuple[int, int], int] = {}) -> int:
    """
    dynamic programming approach (top-down with memoization) to the matrix chain multiplication problem:
    A1 * A2 * A3 * ... * An
    where
    A1, A2, A3, ..., An
    , a chain of n matrices is given, find the optimal parenthesization that minimizes the number of scalar multiplications

    Args:
        dimensions (List[int]): the first matrix is of dimensions dimensions[0] x dimensions[1], the second matrix is of dimensions dimensions[1] x dimensions[2], and so on
        range_of_chain (Tuple[int, int]): the range of the chain to consider, inclusive. For example, if range_of_chain = (1, 3), then we are considering the chain of matrices A1, A2, A3
        least_scalar_multiplications (Dict[Tuple[int, int], int]): 
            key: the range of the chain to consider, inclusive. 
            value: the minimum number of scalar multiplications required to multiply the chain of matrices in this range
            for example, {(1, 3): 5, (2, 6): 7}
        optimal_first_cut (Dict[Tuple[int, int], int]): 
            key: the range of the chain to consider, inclusive. 
            value: the index at which to cut the chain , and it is the optimal first cut
            for example, {(1, 3): 2, (2, 6): 4}, where for the chain A1, A2, A3, the optimal first cut divides the chain into two chains, (A1, A2), and (A3)

    Returns:
        int: the minimum number of scalar multiplications required to multiply the chain of matrices in the specified range
    """
    if range_of_chain in least_scalar_multiplications:
        return least_scalar_multiplications[range_of_chain]
    if range_of_chain[0] == range_of_chain[1]:
        return 0
    if 1 == range_of_chain[1] - range_of_chain[0]:
        scalar_multiplications: int = dimensions[range_of_chain[0] - 1] * dimensions[range_of_chain[0]] * dimensions[range_of_chain[0] + 1]
        least_scalar_multiplications[range_of_chain] = scalar_multiplications
        return scalar_multiplications
        
    current_least_scalar_multipications = float('inf')
    current_optimal_first_cut = -1
    for cut_index in range(*range_of_chain):
        left_side_least_scalar_multiplications = find_optimal_parenthesization_helper(dimensions, (range_of_chain[0], cut_index), least_scalar_multiplications, optimal_first_cut)
        right_side_least_scalar_multiplications = find_optimal_parenthesization_helper(dimensions, (cut_index + 1, range_of_chain[1]), least_scalar_multiplications, optimal_first_cut)
        total_scalar_multipications = left_side_least_scalar_multiplications + right_side_least_scalar_multiplications + \
            dimensions[range_of_chain[0] - 1] * dimensions[cut_index] * dimensions[range_of_chain[1]]
        if total_scalar_multipications < current_least_scalar_multipications :
            current_least_scalar_multipications = total_scalar_multipications
            current_optimal_first_cut = cut_index
    least_scalar_multiplications[range_of_chain] = current_least_scalar_multipications
    optimal_first_cut[range_of_chain] = current_optimal_first_cut
    
    return current_least_scalar_multipications


def insert_parentheses(start_index:int, end_index: int, optimal_first_cut: Dict[Tuple[int, int], int], optimal_parenthesization: List[str | int]):
    """_summary_

    Args:
        start_index (int): _description_
        end_index (int): _description_
        optimal_first_cut (Dict[Tuple[int, int], int]): _description_
        optimal_parenthesization (List[str  |  int]): 
            the initial optimal parenthesization provided by the user must be a list of integers, [start_index, start_index + 1, ... , end_index]

    Raises:
        Exception: _description_
    """
    if start_index > end_index:
        raise Exception("start_index > end_index")
    if end_index - start_index in {0, 1}:
        return
    
    cut_index = optimal_first_cut[(start_index, end_index)]
    # add the parentheses in the left side 
    if start_index < cut_index:
        optimal_parenthesization.insert(optimal_parenthesization.index(start_index), '(')
        optimal_parenthesization.insert(optimal_parenthesization.index(cut_index) + 1, ')')
        insert_parentheses(start_index, cut_index, optimal_first_cut, optimal_parenthesization)
    # add the parentheses in the right side
    if cut_index + 1 < end_index:
        optimal_parenthesization.insert(optimal_parenthesization.index(cut_index + 1), '(')
        optimal_parenthesization.insert(optimal_parenthesization.index(end_index) + 1, ')')
        insert_parentheses(cut_index + 1, end_index, optimal_first_cut, optimal_parenthesization)


def find_optimal_parenthesization(dimensions: List[int]) -> Tuple[int, List[str | int]]:
    """

    Returns:
        Tuple[int, List[str | int]]: 
            int: the minimum number of scalar multiplications required to multiply the chain of matrices 
            List[str | int]: the optimal parenthesization,
                for example, [1, '(', 2, 3, ')'] means A1 * (A2 * A3)
    """
    assert len(dimensions) >= 2
    range_of_chain = (1, len(dimensions) - 1)
    least_scalar_multiplications: Dict[Tuple[int, int], int] = {}
    optimal_first_cut: Dict[Tuple[int, int], int] = {}
    total_scalar_multiplications = find_optimal_parenthesization_helper(dimensions, range_of_chain, least_scalar_multiplications, optimal_first_cut)
    if range_of_chain[1] - range_of_chain[0] >= 2:
        assert least_scalar_multiplications[range_of_chain] == total_scalar_multiplications
    
    optimal_parenthesization: List[str | int] = list(range(range_of_chain[0], range_of_chain[1]+1))
    insert_parentheses(range_of_chain[0], range_of_chain[1], optimal_first_cut, optimal_parenthesization)

    return total_scalar_multiplications, optimal_parenthesization

######################################
def find_optimal_parenthesization_helper_v2(dimensions: List[int]) -> Tuple[Dict[Tuple[int, int], int], Dict[Tuple[int, int], int]]:
    """
    dynamic programming approach (bottom-up) to the matrix chain multiplication problem:
    A1 * A2 * A3 * ... * An

    Args:
        dimensions (List[int]): 
        
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


def find_optimal_parenthesization_v2(dimensions: List[int]) -> Tuple[int, List[str | int]]:
    """

    Returns:
        Tuple[int, List[str | int]]: 
            int: the minimum number of scalar multiplications required to multiply the chain of matrices 
            List[str | int]: the optimal parenthesization,
                for example, [1, '(', 2, 3, ')'] means A1 * (A2 * A3)
    """
    assert len(dimensions) >= 2
    least_scalar_multiplications: Dict[Tuple[int, int], int] = {}
    optimal_first_cut: Dict[Tuple[int, int], int] = {}
    least_scalar_multiplications, optimal_first_cut = find_optimal_parenthesization_helper_v2(dimensions)
    
    optimal_parenthesization: List[str | int] = list(range(1, len(dimensions)))
    insert_parentheses(1, len(dimensions)-1, optimal_first_cut, optimal_parenthesization)

    return least_scalar_multiplications[(1, len(dimensions)-1)], optimal_parenthesization


def test():
    for num_matrices in range(1, 100):
        # make sure the elements in dimensions are unique
        dimensions = random.sample(range(1, 1000), k=num_matrices + 1)
        total_scalar_multiplications, optimal_parenthesization = find_optimal_parenthesization(dimensions)
        total_scalar_multiplications_v2, optimal_parenthesization_v2 = find_optimal_parenthesization_v2(dimensions)
        assert total_scalar_multiplications == total_scalar_multiplications_v2
        assert optimal_parenthesization == optimal_parenthesization_v2
        
        print(f"{dimensions=}")
        print(f"{total_scalar_multiplications=}")
        print(f"{optimal_parenthesization=}")
        for c in optimal_parenthesization:
            if type(c) == str:
                print(c, end='')
            else:
                print(f"A{c},", end='')
        print("\n\n")
        
if __name__ == '__main__':
    test()