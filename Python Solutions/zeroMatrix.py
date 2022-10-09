from copy import deepcopy
import unittest

# Write an algorithm such that if an element in an M * N matrix is 0, its entire row and column are set to 0
def zeroMatrix(matrix):
    """Sets the entire row and column to zero if an element is zero in a n*m matrix."""
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    zeroed_rows, zeroed_cols = set(), set()

    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == 0:
                zeroed_rows.add(row)
                zeroed_cols.add(col)
    for row in range(num_rows):
        for col in range(num_cols):
            if row in zeroed_rows or col in zeroed_cols:
                matrix[row][col] = 0
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
    testable_functions = [zeroMatrix]

    def test_zero_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()
