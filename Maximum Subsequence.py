'''
Maximum Subsequence
-------------------
- A subsequence of a number is a series of (not necessarily contiguous) digits of the number. 
- For example, 12345 has subsequences that include 123, 234, 124, 245, etc. 
- Your task is to get the maximum subsequence below a certain length.

## There are two key insights for this problem:

- You need to split into the cases where the ones digit is used and the one where it is not. 
- In the case where it is, we want to reduce t since we used one of the digits, and in the case where it isn’t we do not.
- In the case where we are using the ones digit, you need to put the digit back onto the end, and the way to attach a digit d to the end of a number n is 10 * n + d.
'''

'''
Solution
--------
'''
def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.
    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    
    if n == 0 or t == 0:
        return 0
    with_ones = max_subseq(n//10, t-1) * 10 + n%10
    not_with = max_subseq(n//10, t)
    if with_ones > not_with:
        return with_ones
    else:
        return not_with