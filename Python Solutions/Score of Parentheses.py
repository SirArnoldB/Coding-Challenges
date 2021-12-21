'''
# Score of Parentheses
----------------------
Source: https://leetcode.com/problems/score-of-parentheses/
- Given a balanced parentheses string s, return the score of the string.
- The score of a balanced parentheses string is based on the following rule:
# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

>>> Example 1:
    # Input: s = "()"
    # Output: 1

>>> Example 2:
    # Input: s = "(())"
    # Output: 2

# Example 3:
    # Input: s = "()()"
    # Output: 2

# Example 4:
    # Input: s = "(()(()))"
    # Output: 6

# Constraints:
    # 2 <= s.length <= 50
    # s consists of only '(' and ')'.
    # s is a balanced parentheses string.
'''
# Solution 1
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Algorithm
            # Iterate through input string and use a Stack to keep track of all of the 
            # computations and incomplete pairings.
            # 1) Create a Stack
            # 2) Iterate through the input string from left to right:
            #     a) If we see a "(":
            #         i) Push it onto the Stack, since it started an incomplete pair
            #     b) If we see a ")":
            #         i) While the top of the stack is not a "(", which signals its pair
            #             - Keep a local score and sum the numbers popping off the stack, since 
            #                 AB is A + B
            #             - Once we reach the "(", 2 * local_score is the score of this pairing
            #                 NOTE: If local score is 0, the default score of the pair is 1
            #             - Push new local score onto stack, in case it is part of a larger pair
            # 3) Return the sum of the elements on the Stack, since it is only numbers now
            # Time Complexity: O(N) [One iteration through String, no full nested iterations]
            # Space Complexity: O(N) [Stack that can grow to size N]

        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                prev = stack.pop()
                score = 0
                while prev != "(":
                    score += prev
                    prev = stack.pop()
                stack.append(1 if score == 0 else score * 2)
        return sum(stack)

# Solution 2
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Algorithm
            # maintain the score at the current depth we are on
            # when we see an openning bracket, we increase our depth, and our score at the new depth is 0
            # when we see a closing bracket, we add twice the score of the previous deeper part, 
            # except when counting (), which has a score of 1
            # For example, when counting (()(())), our stack will look like this:
                # [0, 0] after parsing (
                # [0, 0, 0] after (
                # [0, 1] after )
                # [0, 1, 0] after (
                # [0, 1, 0, 0] after (
                # [0, 1, 1] after )
                # [0, 3] after )
                # [6] after )
                
            # implementation
            
            # the score of the current frame 
            stack = [0] 
            
            for paren in s:
                if paren == '(':
                    stack.append(0)
                else:
                    # when we see a closing bracket, we add twice the score of the previous deeper part, 
                    # except when counting (), which has a score of 1
                    prevScore = stack.pop()
                    
                    stack[-1] += max( 2 * prevScore, 1 )
            return stack.pop()