'''
# Convert a n x m 1D array into a (n * m) x 1 2D array
'''
def unflatten(flat, n, m):
    if len(flat) != n * m:
        raise Exception
    # create 2D Array
    array = [[0 for _ in range(m)] for _ in range(n)]
    # n = number of rows; m = number of columns
    for r in range(n):
        for c in range(m):
            # Converting 2D to 1D:
            # rowIndex * noOfCols + colIndex
            array[r][c] = flat[r * m + c]

    return array

if __name__ == '__main__':
    array = [1, 2, 3, 4, 3, 6, 7, 8, 8, 3, 1, 3, 9, 12, 13, 45, 3, 5, 8, 9]
    print(unflatten(array, 5, 4) == [[1, 2, 3, 4], [3, 6, 7, 8], [8, 3, 1, 3], [9, 12, 13, 45], [3, 5, 8, 9]])