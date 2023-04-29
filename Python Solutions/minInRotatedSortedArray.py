# Source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Find Minimum in Rotated Sorted Array

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.


# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 


# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.
def findMin(nums) -> int:
    if len(nums) == 1:
        return nums[0]
    
    left, right = 0, len(nums) - 1
    
    # if the last element is greater than the first element, then there 
    # is no rotation
    if nums[right] > nums[0]:
        return nums[0]
    
    while left <= right:
        mid = left + (right - left)//2
        
        # point of change (inflection) from higher to lower 
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        # if the mid elements value is greater than the 0th element, 
        # then the least value lies somewhere to the right
        if nums[mid] > nums[0]:
            left = mid + 1
        # if nums[0] > mid value, then this means that the smallest value
        # is somewhere to the left 
        else:
            right = mid - 1

import unittest

class TestFindMin(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(findMin([0, 1, 2, 3]), 0)
        self.assertEqual(findMin([15, 45, 69]), 15)
        self.assertEqual(findMin([60]), 60)
    def test_rotated_array(self):
        self.assertEqual(findMin([4,5,6,7,0,1,2]), 0)
        self.assertEqual(findMin([3,4,5,1,2]), 1)
        self.assertEqual(findMin([1, 1, 3, 5, 8, 0]), 0)

if __name__ == '__main__':
    unittest.main()
