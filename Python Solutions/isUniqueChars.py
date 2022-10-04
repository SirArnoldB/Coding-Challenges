"""
Source: Cracking the coding interview 

Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?

"""


def isUniqueChars(str):
    if len(str) > 128:
        return False

    char_set = [False] * 128

    for i in range(len(str)):
        val = ord(str[i])
        if char_set[val]:
            return False
        char_set[val] = True
    return True


import unittest


class TestIsUniqueChars(unittest.TestCase):
    def test_unique_str(self):
        self.assertEqual(isUniqueChars("acxyz123"), True, "Should be True")
        self.assertEqual(isUniqueChars("abcABC"), True, "Should be True")
        self.assertEqual(isUniqueChars("a"), True, "Should be True")

    def test_non_unique_str(self):
        self.assertEqual(isUniqueChars("acxyz123" * 50), False, "Should be False")
        self.assertEqual(isUniqueChars("abcabc"), False, "Should be False")

if __name__ == "__main__":
    unittest.main()
