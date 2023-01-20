# Find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.

# Input: 2
# Output: ["aa", "ab", "ba", "bb"]

# Input: 4
# Output: ["aaaa", "aaab", "aaba", "aabb", "abaa", "abab", "abba", "abbb", "baaa", "baab", "baba", "babb", "bbaa", "bbab", "bbba", "bbbb"]
from typing import List


def letter_combination(n: int) -> List[str]:
    edges = ["a", "b"]
    if n == 1:
        return edges

    if n == 0:
        return [""]

    def dfs(level, path, paths):
        if level == n:
            paths.append("".join(path))
            return
        for edge in edges:
            path.append(edge)
            dfs(level + 1, path, paths)
            path.pop()

    paths = []
    if n >= 2:
        dfs(0, [], paths)
    return paths


if __name__ == "__main__":
    n = int(input())
    res = letter_combination(n)
    for line in sorted(res):
        print(line)
