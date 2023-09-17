# Find the minimum path sum from top to bottom if given a triangle. Each step you may move to adjacent numbers on the row below.

# Input
# triangle: see example

# Output
# the minimum path sum

# Examples
# Example 1:
# Input:

# triangle = [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# Output: 11

# Explanation:

# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.

# Solution: Bottom-up DP

from typing import List
from math import inf


def minimum_total(triangle: List[List[int]]) -> int:
    num_rows = len(triangle)
    if num_rows == 0:
        return 0

    dp = [[0] * (row + 1) for row in range(num_rows)]
    for col in range(num_rows):
        dp[-1][col] = triangle[-1][col]

    for row in range(num_rows - 2, -1, -1):
        for col in range(row + 1):
            dp[row][col] += (
                min(dp[row + 1][col], dp[row + 1][col + 1]) + triangle[row][col]
            )
    return dp[0][0]


if __name__ == "__main__":
    triangle = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = minimum_total(triangle)
    print(res)


# Complexity Analysis
# Time Complexity: O(N^2), where N is the total number of elements in the triangle.
# Space Complexity: O(N^2), where N is the total number of elements in the triangle.

# Solution: Top-down DP

from typing import List
from math import inf


def minimum_total(triangle: List[List[int]]) -> int:
    num_rows = len(triangle)
    if num_rows == 0:
        return 0

    dp = [[0] * (row + 1) for row in range(num_rows)]
    dp[0][0] = triangle[0][0]

    for row in range(1, num_rows):
        for col in range(row + 1):
            if col == 0:
                dp[row][col] = dp[row - 1][col] + triangle[row][col]
            elif col == row:
                dp[row][col] = dp[row - 1][col - 1] + triangle[row][col]
            else:
                dp[row][col] = (
                    min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]
                )

    return min(dp[-1])


if __name__ == "__main__":
    triangle = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = minimum_total(triangle)
    print(res)


# Complexity Analysis
# Time Complexity: O(N^2), where N is the total number of elements in the triangle.
# Space Complexity: O(N^2), where N is the total number of elements in the triangle.
