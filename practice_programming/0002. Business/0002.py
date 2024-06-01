"""
keywords: dynamic programming, 0/1 Knapsack Problem, profit maximization, project selection

To solve this problem, we need to determine the maximum profit that can be obtained by selecting projects based on their profits, durations, and deadlines. This problem is essentially a variant of the "0/1 Knapsack Problem" where we need to select projects that fit within the given time constraints to maximize profit.

Here is a Python solution using dynamic programming:

### Step-by-Step Approach

1. **Sort Projects by Deadline**:
   - This helps in considering projects that must be completed first due to tighter deadlines.

2. **Dynamic Programming Table**:
   - Use a DP table where `dp[t]` represents the maximum profit that can be achieved by time `t`.

3. **Update DP Table**:
   - Iterate through each project and update the DP table backwards to ensure that each project is considered only once.



### Explanation

1. **Sorting Projects**:
   - Projects are sorted by their deadlines using `projects.sort(key=lambda x: x[2])`.

2. **Initialization**:
   - `max_deadline` is determined as the maximum deadline among all projects.
   - A DP array `dp` of size `max_deadline + 1` is initialized to store the maximum profit up to each time `t`.

3. **Updating DP Table**:
   - For each project `(profit, duration, deadline)`, the DP array is updated from `deadline` to `duration` backwards. This ensures that each project is considered only once.
   - `dp[t] = max(dp[t], dp[t - duration] + profit)` updates the profit for time `t` by considering the profit of the current project.

4. **Result**:
   - The maximum value in the DP array `max(dp)` is the maximum profit that can be obtained.

### Running the Example

For the given example with `N = 4` and the specified projects, running the above code will print the maximum profit:

```python
# Expected Output: 18
```

This solution efficiently uses dynamic programming to determine the optimal set of projects to maximize profit within the given constraints.

"""


from typing import List, Tuple


def max_profit(projects: List[Tuple[int, int, int]]) -> int:
    """

    Args:
        projects (List[Tuple[int, int, int]]): list of tuples representing projects with profit, duration, and deadline

    Returns:
        int: maximum profit that can be obtained by selecting projects based on their profits, durations, and deadlines
    """
    # Sort projects by their deadlines
    projects.sort(key=lambda x: x[2])
    
    # Find the latest deadline
    max_deadline = max(project[2] for project in projects)
    
    # Initialize the DP array
    dp = [0] * (max_deadline + 1)
    
    for profit, duration, deadline in projects:
        # Update DP array backwards
        for t in range(deadline, duration - 1, -1):
            dp[t] = max(dp[t], dp[t - duration] + profit)
    
    return max(dp)

# # Example input
# N = 4
# projects = [
#     (7, 1, 3),
#     (10, 2, 3),
#     (6, 1, 2),
#     (5, 1, 1)
# ]

# # Calculate and print the maximum profit
# print(max_profit(projects))


if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    projects = []
    index = 1
    for _ in range(N):
        P = int(input_data[index])
        L = int(input_data[index + 1])
        D = int(input_data[index + 2])
        projects.append((P, L, D))
        index += 3
    
    # Calculate and print the maximum profit
    print(max_profit(projects))