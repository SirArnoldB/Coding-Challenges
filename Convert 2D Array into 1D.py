# Convert a n x m 2D array into a (n * m) x 1 1D array

# Solution 
def flatten(array):
    if not array:
        return []
    n, m = len(array), len(array[0])
    flat = [0] * (n * m)
    for r in range(n):
        for c in range(m):
            flat[r * m + c] = array[r][c]
    return flat 