'''
Number of Good Pairs
--------------------
Source: https://leetcode.com/problems/number-of-good-pairs/

- Given an array of integers nums. A pair (i,j) is called good if nums[i] == nums[j] and i < j.
- Return the number of good pairs.

# Example 1:
    >>> Input: nums = [1,2,3,1,1,3]
    >>> Output: 4
    >>> Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
    >>> Input: nums = [1,1,1,1]
    >>> Output: 6
    >>> Explanation: Each pair in the array are good.

# Example 3:
    >>> Input: nums = [1,2,3]
    >>> Output: 0

# Constraints:
    >>> 1 <= nums.length <= 100
    >>> 1 <= nums[i] <= 100
'''
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Algorithm
        '''
        - Count how many times each number appears. 
        - If a number appears n times, then n * (n – 1) // 2 good pairs can be made with this number.
        '''
        # keeps track of the frequency of each number
        numsMapping = {}
        # loop through nums and get the frequency of each number 
        for num in nums:
            if num not in numsMapping:
                numsMapping[num] = 1
            else:
                numsMapping[num] += 1
        # keeps track of the number of good pairs
        numGoodPairs = 0
        # get the count of good pairs 
        for num, count in numsMapping.items():
            if count > 1:
                numGoodPairs += count * (count - 1)//2
        return numGoodPairs