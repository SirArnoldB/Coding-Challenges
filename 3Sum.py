"""
Source: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

>>> Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

>>> Example 2:

Input: nums = []
Output: []

>>> Example 3:

Input: nums = [0]
Output: []

>>> Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""

# Solution:
class Solution:
    def threeSum(self, nums):
        # Sort nums in ascending order
        nums.sort()    # O(nlogn) 
        triplets = []
        targetSum = 0
        
        # fix the first numberwith the outer for loop
        for i in range(len(nums) - 2):
            # left and right indexes to fix the other two numbers
            left_idx = i + 1
            right_idx = len(nums) - 1
            # move the left and right indexes towards each other until they meet/pass each other 
            while left_idx < right_idx:
                # find the sum of all three numbers, and compare with the target sum
                three_sum = nums[i] + nums[left_idx] + nums[right_idx]
                if three_sum == targetSum:
                    triplet = [nums[i], nums[left_idx], nums[right_idx]]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    # we increment both indexes since the sum is equal to target sum
                    left_idx += 1
                    right_idx -= 1
                elif three_sum < targetSum:
                    # since nums is sorted, its certain that incrementing the left index will increase the three_sum
                    left_idx += 1
                elif three_sum > targetSum:
                    # since nums is sorted, its certain that decreasing the right index will decrease the three_sum
                    right_idx -= 1
        return triplets