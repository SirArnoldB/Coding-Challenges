'''
## Add Strings
--------------
Source: https://leetcode.com/problems/add-strings/
- Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
- You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
- You must also not convert the inputs to integers directly.

# Example 1:
    Input: num1 = "11", num2 = "123"
    Output: "134"
# Example 2:
    Input: num1 = "456", num2 = "77"
    Output: "533"  
# Example 3:
    Input: num1 = "0", num2 = "0"
    Output: "0"

# Constraints:
    1 <= num1.length, num2.length <= 104
    num1 and num2 consist of only digits.
    num1 and num2 don't have any leading zeros except for the zero itself.
'''
from math import remainder


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        resultant_sumultant_sum = []
        remainder = 0
        # set two pointers to the end of each string, 
        # digit - by - digit addition 
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        
        while p1 >= 0 or p2 >= 0: # stop when both strings are used entirely 
            # set x1 to be the digit from string num1 at index p1
            # if p1 has reached the beginning of num1, set x1 to 0
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            # set x2 to be the digit from string num2 at index p1
            # if p2 has reached the beginning of num2, set x2 to 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            
            # compute the sum of the two digits
            value = (x1 + x2 + remainder) % 10
            # compute the remainder 
            remainder = (x1 + x2 + remainder) // 10
            resultant_sum.append(str(value))
            # advance the pointers
            p1 -= 1
            p2 -= 1
        
        # if the remainder is still non-zero, we update the resultant_sum
        if remainder:
            resultant_sum.append(str(remainder))
        resultant_sum = resultant_sum[::-1]
        return ''.join(resultant_sum)
