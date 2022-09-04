class Solution:
    def rotate(matrix):
        """
        Rotates the matrix representing an image by 90 degrees (clockwise).
        
        Source: https://leetcode.com/problems/rotate-image/
        """
        matrix_size = len(matrix)
        # first transpose the matrix
        for row in range(matrix_size):
            for col in range(row, matrix_size):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # flip the matrix symmetrically
        for row in range(matrix_size):
            for col in range(matrix_size//2):
                matrix[row][col], matrix[row][matrix_size - 1 - col] = matrix[row][matrix_size - 1 - col], matrix[row][col]
