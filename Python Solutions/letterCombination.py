# Find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.

# Input: 2
# Output: ["aa", "ab", "ba", "bb"]

# Input: 4
# Output: ["aaaa", "aaab", "aaba", "aabb", "abaa", "abab", "abba", "abbb", "baaa", "baab", "baba", "babb", "bbaa", "bbab", "bbba", "bbbb"]
from typing import List


def letter_combination(n: int) -> List[str]:
    # Base case: if n is 0, return an empty string
    if n == 0:
        return [""]

    # List of possible edges ('a' and 'b')
    edges = ["a", "b"]

    # If n is 1, return the edges list
    if n == 1:
        return edges

    # Recursive function to generate all combinations
    def dfs(level, path, paths):
        # If the level reaches n, add the current combination to the paths list
        if level == n:
            paths.append("".join(path))
            return
        # For each edge, add it to the path and recursively call the function
        for edge in edges:
            path.append(edge)
            dfs(level + 1, path, paths)
            path.pop()

    # Initialize an empty list to store the combinations
    paths = []
    # If n is greater than or equal to 2, call the dfs function
    if n >= 2:
        dfs(0, [], paths)
    return paths


if __name__ == "__main__":
    # Read the input value of n
    n = int(input())
    # Generate the letter combinations
    res = letter_combination(n)
    # Sort the combinations in lexicographical order and print them
    for line in sorted(res):
        print(line)
