import unittest

def rotateString(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False


class Test(unittest.TestCase):

    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]

    def testRotateString(self):
        for [s1, s2, expected] in self.test_cases:
            actual = rotateString(s1, s2)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()