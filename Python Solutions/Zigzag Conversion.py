# Zigzag Conversion
# Source: https://leetcode.com/problems/zigzag-conversion/description/

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);


# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

import unittest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]
        index, step = 0, 1

        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        joined_rows = ["".join(row) for row in rows]

        return "".join(joined_rows)


class TestSolution(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(Solution().convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(Solution().convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(Solution().convert("A", 1), "A")

    def test_invalid_input(self):
        self.assertEqual(Solution().convert("", 1), "")
        self.assertEqual(Solution().convert("PAYPALISHIRING", 0), "PAYPALISHIRING")
        self.assertEqual(Solution().convert("PAYPALISHIRING", 20), "PAYPALISHIRING")


if __name__ == "__main__":
    unittest.main()
