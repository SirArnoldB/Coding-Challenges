'''
Solution: Bit Manipulation: O(n) - time | O(1) - space
'''
class Solution(object):
    def singleNumber(self, nums):
        """Returns the single element that appears once in the array nums."""

        # based on the idea that
        # a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b
        num = 0
        for val in nums:
            num ^= val
        return num