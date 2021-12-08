'''
Valid Parentheses
-----------------
Source: https://leetcode.com/problems/valid-parentheses/

- Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
- An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.

# Example 1:
    >>> Input: s = "()"
    >>> Output: true

# Example 2:
    >>> Input: s = "()[]{}"
    >>> Output: true

# Example 3:
    >>> Input: s = "(]"
    >>> Output: false

# Example 4:
    >>> Input: s = "([)]"
    >>> Output: false

# Example 5:
    >>> Input: s = "{[]}"
    >>> Output: true

# Constraints:
    >>> 1 <= s.length <= 104
    >>> s consists of parentheses only '()[]{}'.
'''
'''
Solution 1
----------
'''
# O(n) - time | O(n) - space : where n is the length of s
# we traverse the given string one character at a time and push and pop operations on a stack take O(1) - time
class Solution:
    def isValid(self, s: str) -> bool:
        
        '''
        ## Algorithm

            - Initialize a stack S.
            - Process each bracket of the expression one at a time.
            - If we encounter an opening bracket, we simply push it onto the stack. 
            - This means we will process it later, let us simply move onto the sub-expression ahead.
            - If we encounter a closing bracket, then we check the element on top of the stack. 
            - If the element at the top of the stack is an opening bracket of the same type, then we               
            - pop it off the stack and continue processing. Else, this implies an invalid expression.
            - In the end, if we are left with a stack still having elements, then this implies an invalid expression.
        '''
        
        # stack to keep track of opening brackets
        stack = []
        i = 0
        while s and i < len(s):
            if stack and stack[-1] == "(" and s[i] == ")":
                s, i = s[i + 1 : ], 0
                stack.pop(-1)
            elif stack and stack[-1] == "{" and s[i] == "}":
                s, i = s[i + 1 : ], 0
                stack.pop(-1)
            elif stack and stack[-1] == "[" and s[i] == "]":
                s, i = s[i + 1 : ], 0
                stack.pop(-1)
            else: 
                stack.append(s[i])
                i += 1
        #print(stack)  
        return True if len(stack) == 0 else False

# ******************************************************************** #
        
'''
Solution 2
----------
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is a closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack