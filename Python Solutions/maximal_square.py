# Maximal Square
# Given a binary matrix, find out the largest size square sub-matrix with all 1's and return its area.

# Input
# matrix: a binary matrix
# Output
# the area of the largest square in the input matrix

# Examples
# Example 1:
# Input:

# matrix =
# [[1, 0, 1, 0, 0],
#  [1, 0, 1, 1, 1],
#  [1, 1, 1, 1, 0],
#  [1, 0, 0, 1, 0]]
# Output: 4

# Explanation:

# The largest square is of size 2x2 and area 4.

# Solution: Top-down DP
from typing import List


def maximal_square(matrix: List[List[int]]) -> int:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    max_side = 0

    dp = [[0] * (num_cols) for _ in range(num_rows)]

    # fill top row
    for col in range(num_cols):
        dp[0][col] = matrix[0][col]
        max_side = max(max_side, dp[0][col])

    # fill right column
    for row in range(num_rows):
        dp[row][0] = matrix[row][0]
        max_side = max(max_side, dp[row][0])

    # fill inner cells
    for row in range(1, num_rows):
        for col in range(1, num_cols):
            if matrix[row][col] == 1:
                # if the current cell is 1, then the max side length is 1 + the min of the three cells above it
                # (left, top, top-left) - this is because we can only form a square if all three cells are 1s as well (otherwise, we would have a rectangle)
                dp[row][col] = 1 + min(
                    dp[row][col - 1], dp[row - 1][col - 1], dp[row - 1][col]
                )
                max_side = max(dp[row][col], max_side)
    return max_side * max_side


if __name__ == "__main__":
    matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = maximal_square(matrix)
    print(res)
