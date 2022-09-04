class Solution:
    def transpose(matrix):
        """
        Returns the transpose of the matrix.
        
        Source: https://leetcode.com/problems/transpose-matrix/
        """
        rows, cols = len(matrix), len(matrix[0])
        new_matrix = [[None] * rows for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                new_matrix[col][row] = matrix[row][col]
        return new_matrix