'''
Two Sum
-------
Source: https://leetcode.com/problems/two-sum/
- Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
- You may assume that each input would have exactly one solution, and you may not use the same element twice.
- You can return the answer in any order.

## Example 1:
>>> Input: nums = [2,7,11,15], target = 9
>>> Output: [0,1]
>>> Output: Because nums[0] + nums[1] == 9, we return [0, 1].

## Example 2:
>>> Input: nums = [3,2,4], target = 6
>>> Output: [1,2]

## Example 3:
>>> Input: nums = [3,3], target = 6
>>> Output: [0,1]
'''

'''
Solution 1: Efficient
-------------------
'''
# O(n) - time | O(n) - space : where n is the length of the input array
class Solution:
    def twoSum(nums, target):
        #  map to store the numbers we have seen 
        # the value for each number in the map will be the index of that number in nums
        nums_map = {}

        for i in range(len(nums)):
            # possible sum
            poss_addend = target - nums[i]
            if poss_addend in nums_map:
                # given that each input will have exactly one solution, 
                # return the indexes once there are found
                return [i, nums_map[poss_addend]]
            else:
                # if not, add the current number to the map, and have its index as the value
                nums_map[nums[i]] = i 
        return []

'''
Solution 2: Brute Force
-----------------------
'''
# O(n^2) - time | O(1) - space : where n is the length of the input array
class Solution:
    def twoSum(nums, target):
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if i != j:
                    if (nums[i] + nums[j]) == target:
                        return [i, j]
                j += 1
                
            i += 1
