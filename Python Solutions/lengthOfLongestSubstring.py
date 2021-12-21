"""
Longest Substring Without Repeating Characters
----------------------------------------------
# Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/

- Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
>>> Input: s = "abcabcbb"
>>> Output: 3
>>> Explanation: The answer is "abc", with the length of 3.

# Example 2:
>>> Input: s = "bbbbb"
>>> Output: 1
>>> Explanation: The answer is "b", with the length of 1.

# Example 3:
>>> Input: s = "pwwkew"
>>> Output: 3
>>> Explanation: The answer is "wke", with the length of 3.
>>> Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
>>> Input: s = ""
>>> Output: 0

# Constraints:
>>> 0 <= s.length <= 5 * 104
>>> s consists of English letters, digits, symbols and spaces.
"""
'''
Solution
******** 
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Algorithm
        '''
        - keep track of seen characters, seenChars = {}
        - keep track of maximum lenght of string, maxLen = 0 , substring lenght subStringLen = 0
        - loop through s:
            - char = s[i]
            - when char in seenChars, 
                - update maxLen
                - change loop counter to seenChars[char]
                - seenChars = {}
                - subStringLen = 0
            - else:
                - subStringLen += 1
                - seenChars[char] = i
                - i += 1
        '''
        if not s:
            return 0
        seenChars = {}
        maxLen = 1
        subStringLen = 0
        i = 0
        
        while i < len(s):
            # the character in s
            char = s[i]
            # is the character is already in the dictionary
            if char in seenChars:
                # update maxlen 
                maxLen = max(maxLen, subStringLen)
                # reset the counter, i, to tghe index of the first instance of the duplicate 
                # character plus 1
                i = seenChars[char] + 1
                # reset the dictionary and subStringLen
                seenChars = {}
                subStringLen = 0
            else:
                # update thge sub string lenght, and add the char to the seenChars dict
                subStringLen += 1
                seenChars[char] = i
                i += 1
        # return the maximum between maxLen and subStringLen
        return max(maxLen, subStringLen)