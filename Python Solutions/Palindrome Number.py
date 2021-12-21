"""
Palindrome Number:
******************
Source: https://leetcode.com/problems/palindrome-number/

- Given an integer x, return true if x is palindrome integer.

- An integer is a palindrome when it reads the same backward as forward. 
- For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false

Constraints: -231 <= x <= 231 - 1

"""
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    """
    Algorithm:
    ----------
    - Initialize variable reverse_num = 0  
    - Loop while x > 0  
        - Get the last_digit of x
        - Multiply reverse_num by 10 and add the last_digit  
        - Divide x by 10 to give the updated value of x   
    - Return reverse_num 
    
    Edge Cases:
    ----------
    - all negative numbers are not palindromes,so we can return false for all negative numbers. 
    - if the last digit of the number x is 0, then for it to be a palindrome, 
    - the first digit of the number also needs to be 0 -    Only 0 satisfies this property. 
    - To avoid integer overflow problem with the reverse number, we reverse half of the integer
    - the reverse of the last half should be the same as the first half of the number, if the  number is a palindrome. 
    """
    
    # take care of the edge cases 
    if x < 0 or (x % 10 == 0 and x != 0):
        return False 
    # initialize reversed_num to 0
    reversed_num = 0
    
    # to avoid overflow, we loop until x becomes smaller than reverse_num, 
    # because then, it means we have processed half of the number digits. 
    while x > reversed_num:
        last_digit = x % 10
        reversed_num = (reversed_num * 10) + last_digit
        x = x // 10
    
    # print(reversed_num)
    # When the length of x is an odd number, we can get rid of the middle digit by reversed_num // 10
    # For example when the input is 12321, at the end of the while loop we get:
        # x = 12, reversed_num = 123
    # since the middle digit doesn't matter in palidrome(it will always equal to itself), 
        # we can simply get rid of it.
    return x == reversed_num or x == reversed_num // 10

if __name__ == '__main__':
    x = [121121, 123, 44444, 678876, 1000, 0, 33333333]
    for num in x:
        print("{0} is a Palindrome: {1}".format(num, isPalindrome(num)))