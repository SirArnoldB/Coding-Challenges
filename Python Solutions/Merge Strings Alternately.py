# Merge Strings Alternately
# Source: https://leetcode.com/problems/merge-strings-alternately/
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d


# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.
from itertools import zip_longest


def mergeAlternately(word1: str, word2: str) -> str:
    merged, alternate = [], False
    word1_idx, word2_idx = 0, 0
    while word1_idx < len(word1) and word2_idx < len(word2):
        if not alternate:
            merged.append(word1[word1_idx])
            word1_idx += 1
            alternate = True
        else:
            merged.append(word2[word2_idx])
            word2_idx += 1
            alternate = False
    if word1_idx < len(word1):
        merged.append(word1[word1_idx:])
    if word2_idx < len(word2):
        merged.append(word2[word2_idx:])
    return "".join(merged)


# Solution 2: using zip_longest
def mergeAlternately2(word1: str, word2: str) -> str:
    return "".join([a + b for a, b in zip_longest(word1, word2, fillvalue="")])


import unittest


class TestMergeAlternately(unittest.TestCase):
    def testMergeAlternately(self):
        self.assertEqual(mergeAlternately("abc", "pqr"), "apbqcr")

    def testMergeAlternately2(self):
        self.assertEqual(mergeAlternately("abc", "pqr"), "apbqcr")


if __name__ == "__main__":
    unittest.main()
