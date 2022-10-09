from copy import deepcopy
import unittest

# Source: https://leetcode.com/problems/rotate-image/
def rotate(matrix):
    """
    Rotates the matrix representing an image by 90 degrees (clockwise).
    """
    matrix_size = len(matrix)
    # first transpose the matrix
    for row in range(matrix_size):
        for col in range(row, matrix_size):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    # flip the matrix symmetrically
    for row in range(matrix_size):
        for col in range(matrix_size // 2):
            matrix[row][col], matrix[row][matrix_size - 1 - col] = (
                matrix[row][matrix_size - 1 - col],
                matrix[row][col],
            )
    return matrix


class Test(unittest.TestCase):

    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    testable_functions = [
        rotate,
    ]

    def testRotateMatrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()
