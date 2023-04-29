# Source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

# Space Complexity: O(n) - The height of the tree is the number of digits of the input phone number.
# Time Complexity: O(4^n * n)

    # Explanation
        # The time complexity of a backtracking algorithm is the number of nodes in the space-state tree multiplied by the operation at each node. 
        # In the worse case where we only have 7s and 9s in the input phone number, each node has 4 children. And the height of the tree is the number of digits of the phone number. 
        # Therefore the tree has maximum of 4^n nodes where n is the number of digits of the phone number. 
        # We also need O(n) to build a new string when we reach the leaf node so the total complexity is O(4^n * n).

def letterCombinations(digits):
    digits_map = {
    '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], 
    '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], 
    '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'] 
    }
    
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return digits_map[digits[0]]
    
    def dfs(level, curr_index, path, paths):
        if level == len(digits):
            paths.append(''.join(path))
            return 
        for letter in digits_map[digits[curr_index]]:
            path.append(letter)
            dfs(level + 1, curr_index + 1, path, paths)
            path.pop()
    paths = []
    dfs(0, 0, [], paths)
    return paths

if __name__ == "__main__":
    n = int(input())
    res = letterCombinations(str(n))
    for line in sorted(res):
        print(line)