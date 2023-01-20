# Permutations

# Write a function that takes in an array of unique integres and returns an array of all 
# permutations of those integers in no particular order. 
# If the input array is empty, the function should return an empty array.
# Example:
# array = [1, 2, 3]
# Output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
def getPermutations(array):
    def dfs(level, used, permutation, permutations):
        # check if we have reached a leaf node
        if level == len(array):
            permutations.append(permutation[:])
            return 
            
        for i, num in enumerate(array):
            if used[i]:
                continue 
            # add num to permutation and mark it as used
            permutation.append(num)
            used[i] = True
            
            # recurse 
            dfs(level + 1, used, permutation, permutations)
            
            # remove letter from permutation and mark it as unused
            permutation.pop()
            used[i] = False 
            
    permutations = []
    if array: dfs(0, [False] * len(array), [], permutations)
    return permutations