# Source: https://leetcode.com/problems/palindrome-partitioning/

# Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.


# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.
from typing import List


def partition(s: str) -> List[List[str]]:
    # use backtracking with prunning 
        # if a prefix is not a valid palindrome, don't evaluate it 
    # start from the 0 and partition s into strings which are palindromes 
    # path = []
    # paths = [['a', 'b', 'c'], ['aa', 'b'] ]
    def isPalindrome(prefix):
        """Check is the current prefix is a palindrome."""
        return prefix == prefix[::-1]
    
    def dfs(start, path, paths):
        if start == len(s):
            paths.append(path[:])
            return 
        for i in range(start + 1, len(s) + 1):
            prefix = s[start: i]
            # prune if needed 
            if isPalindrome(prefix):
                path.append(prefix)
                # increment start index
                dfs(start + len(prefix), path, paths)
                path.pop()
    paths = []
    dfs(0, [], paths)
    return paths

if __name__ == "__main__":
    str = input()
    res = partition(str)
    for line in sorted(res):
        print(line)