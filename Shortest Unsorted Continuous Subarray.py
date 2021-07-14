'''
### Shortest Unsorted Continuous Subarray
Source: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

- Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
- Return the shortest such subarray and output its length.

# Example 1:
    Input: nums = [2,6,4,8,10,9,15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Example 2:
    Input: nums = [1,2,3,4]
    Output: 0
# Example 3:
    Input: nums = [1]
    Output: 0

# Constraints:
    1 <= nums.length <= 104
    -105 <= nums[i] <= 105
'''
class Solution(object):
    def findUnsortedSubarray(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(arr) - 1
        # find the first number out of sorting order from the beginning
        while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
            left += 1

        if left == len(arr) - 1: # if the array is sorted
            return 0

        # find the first number out of sorting order from the end
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        # find the maximum and minimum of the subarray
        subarrayMax = -float('inf')
        subarrayMin = float('inf')
        for k in range(left, right + 1):
            subarrayMax = max(subarrayMax, arr[k])
            subarrayMin = min(subarrayMin, arr[k])

        # extend the subarray to include any number which is bigger than the minimum of the subarray 
        while left > 0 and arr[left - 1] > subarrayMin:
            left -= 1
        # extend the subarray to include any number which is smaller than the maximum of the subarray
        while right < len(arr) - 1 and arr[right + 1] < subarrayMax:
            right += 1

        return right - left + 1