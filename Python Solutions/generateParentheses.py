# Source: https://leetcode.com/problems/generate-parentheses/

# Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

# Constraints:

# 1 <= n <= 8
def generateParenthesis(n):
    def dfs(level, path, closeCount, openCount, paths):
        if level == 2 * n:
            paths.append(''.join(path))
            return
        if openCount < n:
            path.append('(')
            dfs(level + 1, path, closeCount, openCount + 1, paths)
            path.pop()
        if closeCount < openCount:
            path.append(')')
            dfs(level + 1, path, closeCount + 1, openCount, paths)
            path.pop()
    paths = []
    dfs(0, [], 0, 0, paths)
    
    return paths