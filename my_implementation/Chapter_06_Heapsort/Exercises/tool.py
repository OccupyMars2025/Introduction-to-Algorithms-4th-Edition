import numpy as np

# def compare_ceil_expressions(x):
#     # Calculate both sides of the inequality
#     lhs = 0.5 * np.ceil(x)
#     rhs = np.ceil(0.5 * x)
    
#     # Compare the two sides
#     return lhs <= rhs


# # Testing over a continuous range
# test_range = np.linspace(-10, 10, 4000)  # 400 points between -10 and 10

# # Check if all comparisons are True
# all_comparisons_true = np.all(compare_ceil_expressions(test_range))

# assert all_comparisons_true
# print(f"The inequality holds for all tested values in the range: {all_comparisons_true}")


def compare(x: float):
    lhs = np.floor((1/2) * np.floor(x/2))
    rhs = np.floor(x/4)
    # print(f"{lhs} == {rhs}")
    assert lhs == rhs

for x in np.linspace(0, 100, 1000000):
    compare(x)