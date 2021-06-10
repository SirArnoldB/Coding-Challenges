"""
Longest Consecutive Sequence
----------------------------
Source : https://leetcode.com/problems/longest-consecutive-sequence/

- Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
- You must write an algorithm that runs in O(n) time.

# Example 1:

>>> Input: nums = [100,4,200,1,3,2]
>>> Output: 4
>>> Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

>>> Input: nums = [0,3,7,2,5,8,4,6,0,1]
>>> Output: 9

# Constraints:

>>> 0 <= nums.length <= 105
>>> -109 <= nums[i] <= 109
"""

'''
Solution
********
'''
# O(n) - time | O(n) - space
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        # Algorithm:
        - create a hash set of nums, set_nums
        - loop through the array, nums
        - keep track of the longest length count (longest) starting at 0
        - At index a:
            - if nums[a] - 1 in set: continue
                - this current number is not the start index of the sequence
            - else:
                - create two counters, currentNum = nums[a], and currentLen = 1
                - while currentNum + l is in the set:
                    - increment currentNum and currentLen
                - after loop is done, update longest length count, 
                    - longest = longest if longest > currentLen else currentLen
        - return longest
        """
        # create a hash set of nums; 
        # provides constant look up
        set_nums = set(nums)
        
        longest = 0
        
        # check each possible sequence from the start, and update the longest 
        # continuous sub-string
        for i in range(len(nums)):
            # if the current element is the starting element of a sequence
            if nums[i] - 1 not in set_nums:
                currentNum, currentLen = nums[i], 1
                # check for the next elements in the sequence 
                while currentNum + 1 in set_nums:
                    currentNum += 1
                    currentLen += 1
                # update longest if currentLen is greater, 
                longest = max(longest, currentLen)
        return longest 
        
        
'''        
### Brute Force Solution:
# O(nlogn) - time | O(1) - space : where n is the length of the input array
# the main 'for' loop does constant work n times, so the algorithm's complexity is dominated
# by the invocation of 'sort' which will run in O(nlogn) time. 
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)
'''