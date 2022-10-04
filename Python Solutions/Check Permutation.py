"""
Given two strings, write a method to decide if one is a permutation of the other.
"""
def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    letters = {}
    for char in s1:
        letters[char] = letters.get(char, 0) + 1
    for char in s2:
        letters[char] = letters.get(char, 0) - 1
        if letters[char] < 0:
            return False
    return True

import unittest

class TestcheckPermutation(unittest.TestCase):
    def test_perm(self):
        self.assertEqual(checkPermutation("abc", "bcd"), False)
        self.assertEqual(checkPermutation("abc", "bca"), True)
        self.assertEqual(checkPermutation("a", "bcd"), False)

if __name__ == "__main__":
    unittest.main()

