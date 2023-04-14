# Search in Rotated Sorted Array

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Helper function to find the pivot point
        def find_pivot(lo, hi):
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        # Helper function to perform binary search on the array
        def binary_search(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1

        n = len(nums)
        pivot = find_pivot(0, n - 1)

        # If pivot is 0, then the array is not rotated
        if pivot == 0:
            return binary_search(0, n - 1)
        elif target >= nums[0]:
            # If target is greater than or equal to the first element,
            # search in the first half of the array
            return binary_search(0, pivot - 1)
        else:
            # Otherwise, search in the second half of the array
            return binary_search(pivot, n - 1)
