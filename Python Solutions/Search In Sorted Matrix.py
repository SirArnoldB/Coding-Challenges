"""
# Search In Sorted Matrix
-------------------------
Source: https://www.algoexpert.io/questions/Search%20In%20Sorted%20Matrix

- You're given a two-dimensional array (a matrix) of distinct integers and a target integer. 
- Each row in the matrix is sorted, and each column is also sorted; the matrix
- doesn't necessarily have the same height and width.
- Write a function that returns an array of the row and column indices of the target integer if it's contained in the matrix, otherwise [-1, -1] .

    # Sample Input: matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
    ]
    target = 44

    # Sample Output
    # [3, 3]
"""
# O(n + m ) - time | O(1) - space: where n and m are the number of rows and columns
def searchInSortedMatrix(matrix, target):
    # traverse the matrix starting at the top right corner 
	row = 0
	# col value starts at the last value of the first row
	col = len(matrix[0]) - 1
	# traverse the matrix whilke the coordinates are still valid positions
	# in the matrix
	while row < len(matrix) and col >= 0:
		# compare the current value to the target value
		if matrix[row][col] > target:
			# eliminate all the numbers that are greater than our current 
			# number by moving to the left
			# decrement the column
			col -= 1
		elif matrix[row][col] < target:
			# move down by incrementing the row
			row += 1
		else:
			return [row, col]
	return [-1, -1]

# ******************************************************************************* #
			
# Brute Force Solution 
# O(n * m) - time | O(1) - space 
def searchInSortedMatrix(matrix, target):
    numRows = len(matrix)
    rcIndices = []
    for row in range(numRows):
        column = matrix[row]
        for col in range(len(column)):
            if matrix[row][col] == target:
                rcIndices.append(row)
                rcIndices.append(col)
    return rcIndices if rcIndices else [-1, -1]
