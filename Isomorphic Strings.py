'''
# Isomorphic Strings
--------------------
Source: https://leetcode.com/problems/isomorphic-strings/

- Given two strings s and t, determine if they are isomorphic.
- Two strings s and t are isomorphic if the characters in s can be replaced to get t.
- All occurrences of a character must be replaced with another character while preserving the order of characters. 
- No two characters may map to the same character, but a character may map to itself.

# Example 1:
    >>> Input: s = "egg", t = "add"
    >>> Output: true
# Example 2:
    >>> Input: s = "foo", t = "bar"
    >>> Output: false
# Example 3:
    >>> Input: s = "paper", t = "title"
    >>> Output: true

# Constraints:
    >>> 1 <= s.length <= 5 * 104
    >>> t.length == s.length
    >>> s and t consist of any valid ascii character.
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 
        
        # keep track of the mapping of characters in s to t
        mapping = {}
        # keeps track of characters already mapped
        characterSet = set()
        # for each character in s and t
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            
            if char1 in mapping:
                if mapping[char1] != char2:
                    return False 
            else:
                if char2 in characterSet:
                    return False 
                characterSet.add(char2)
                mapping[char1] = char2
        return True 