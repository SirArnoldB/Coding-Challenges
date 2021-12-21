# Convert a n x m 2D array into a (n * m) x 1 1D array

# Solution 
def flatten(array):
    if not array:
        return []
    # n = number of rows, m = number of columns
    n, m = len(array), len(array[0])
    print(n, m)
    flat = [0] * (n * m)
    for r in range(n):
        for c in range(m):
            # Converting 2D to 1D:
            # rowIndex * noOfCols + colIndex
            flat[r * m + c] = array[r][c]
    return flat 

if __name__ == '__main__':
    array = [[1, 2, 3, 4], [3, 6, 7, 8], [8, 3, 1, 3], [9, 12, 13, 45], [3, 5, 8, 9]]
    print(flatten(array))