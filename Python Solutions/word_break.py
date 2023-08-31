# Given a string and a list of words, determine if the string can be constructed from concatenating words from the list of words. A word can be used multiple times.

# Input:

# target = "algomonster"
# words = ["algo", "monster"]
# Output: true

# Input:

# target = "aab"
# words = ["a", "c"]
# Output: false

import unittest


def word_break(target, words):
    # keep track of the words we have seen
    memo = {}

    def dfs(start_index):
        """Returns True if the target can be constructed from the list of words, False otherwise"""

        # base case: we have reached the end of the target string
        if start_index == len(target):
            return True

        # if we have seen this start_index before, return the result
        if start_index in memo:
            return memo[start_index]

        # otherwise, we have not seen this start_index before
        ans = False

        # try to match the target string with the words
        for word in words:
            if target[start_index:].startswith(word):
                if dfs(start_index + len(word)):
                    ans = True
                    break

        # memoize the result
        memo[start_index] = ans

        return ans

    return dfs(0)


class TestWordBreak(unittest.TestCase):
    def test_word_break(self):
        self.assertEqual(word_break("algomonster", ["algo", "monster"]), True)
        self.assertEqual(word_break("aab", ["a", "c"]), False)
        self.assertEqual(word_break("leetcode", ["leet", "code"]), True)
        self.assertEqual(word_break("applepenapple", ["apple", "pen"]), True)
        self.assertEqual(
            word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]), False
        )

    def test_word_break_empty_string(self):
        self.assertEqual(word_break("", ["a", "b"]), True)


if __name__ == "__main__":
    unittest.main()
