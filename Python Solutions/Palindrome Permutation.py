"""
Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word that is the same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words. You can ignore casing and non-letter characters.

# Example:
    # Input: Tact Coa
    # Output: True (permutations: "taco cat", "atco cta", etc)
"""


from curses.ascii import isalpha

# Solution 1: Time: O(n) where n is the length of the string
# Use a hash table to count character frequency.
# Then check that no more than one character has an odd count


def getCharFrequencies(s: str, s_chars: object) -> None:
    for char in s.lower():
        if isalpha(char):
            s_chars[char] = s_chars.get(char, 0) + 1


def checkMaxOneOdd(char_map: object) -> bool:
    odd_char_count = 0
    for char, count in char_map.items():
        if count % 2 != 0:
            odd_char_count += 1
            # To be a permutation of a palindrome,
            # the string should have no more than one character that is odd
            if odd_char_count > 1:
                return False
    return True


def isPalindromePermutation(s: str):
    """Checks if a string is a permutation of a palindrome."""
    s_chars = {}
    getCharFrequencies(s, s_chars)
    return checkMaxOneOdd(s_chars)


import unittest


class TestIsPalindromePermutation(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [isPalindromePermutation]

    def testPalindromePermutation(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()
