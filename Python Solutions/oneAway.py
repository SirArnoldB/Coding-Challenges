# There are three types of edits that can be performed on strings: insert  a character,
# remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.


def checkEdits(shorter_str: str, longer_str: str) -> bool:
    idx1, idx2 = 0, 0
    foundDiff = False

    while idx1 < len(shorter_str) and idx2 < len(longer_str):
        if shorter_str[idx1] != longer_str[idx2]:
            if foundDiff:
                return False
            foundDiff = True

            if len(shorter_str) == len(longer_str):
                idx1 += 1
        elif shorter_str[idx1] == longer_str[idx2]:
            # if matching, move shorter pointer
            idx1 += 1
        idx2 += 1
    return True


def oneAway(first: str, second: str) -> bool:
    """Checks if two strings are one edit (or zero edits) away."""
    if abs(len(first) - len(second)) > 1:
        return False

    if len(first) < len(second):
        return checkEdits(first, second)
    return checkEdits(second, first)


import time
import unittest


class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]

    testable_functions = [oneAway]

    def test_one_away(self):

        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert f(text_a, text_b) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
