# Source: https://leetcode.com/problems/set-matrix-zeroes/
# Set Matrix Zeroes

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.


# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1


# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
from copy import deepcopy
import unittest

# Solution 1
# Time: O(m * n )
# Space: O(m + n)
def setZeroes(matrix) -> None:
    zeroed_rows = set()
    zeroed_cols = set()
    # Mark the rows and columns that are to be made zero
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                zeroed_rows.add(row)
                zeroed_cols.add(col)
    # Set the elements in rows and columns with zero to zero
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row in zeroed_rows or col in zeroed_cols:
                matrix[row][col] = 0
    return matrix


# Solution 2:
# Time: O(m * n)
# Space: O(1)
def zeroRow(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def zeroCol(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def optimizedSetZeroes(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row_has_zero = False
    col_has_zero = False

    # check if first row has a zero
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            row_has_zero = True
            break

    # check if first col has a zero
    for j in range(len(matrix)):
        if matrix[j][0] == 0:
            col_has_zero = True
            break

    # check for zeros in the rest of the array
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[row][col] == 0:
                # set the first element of the corressponding row and column to zero
                matrix[row][0] = 0
                matrix[0][col] = 0

    # zero the rows based on the state of the first column
    for row in range(1, len(matrix)):
        if matrix[row][0] == 0:
            zeroRow(matrix, row)

    # zero columns based on the state of the first column
    for col in range(1, len(matrix[0])):
        if matrix[0][col] == 0:
            zeroCol(matrix, col)

    # zero first row:
    if row_has_zero:
        zeroRow(matrix, 0)
    # zero first column
    if col_has_zero:
        zeroCol(matrix, 0)
    return matrix


class Test(unittest.TestCase):

    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    testable_functions = [
        setZeroes,
        optimizedSetZeroes,
    ]

    def test_zero_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()
