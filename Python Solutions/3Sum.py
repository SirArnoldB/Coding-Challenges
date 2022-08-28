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
        # Sort the given array 
        nums.sort()
        # array to hold the triplets
        triplets = []

        # Outer loop to fix the first element
        for i in range(len(nums) - 2):
            # skip repeated element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Left and right pointers
            left = i + 1
            right = len(nums) - 1
            
            # Inner loop to find remaining pair
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # skip repeated elements
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
        return triplets