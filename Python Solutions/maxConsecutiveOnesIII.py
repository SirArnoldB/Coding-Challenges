"""
### Max Consecutive Ones III
-----------------------------
# Source: https://leetcode.com/problems/max-consecutive-ones-iii/

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

"""


class Solution:
    # O(n) - time | O(1) - space: where n is the length of nums
    def longestOnes(nums, k):
        # keeps track of the maximum number of consecutive ones
        maxOnes = 0
        # start - starting index; end - ending index
        start = end = 0
        # keeps track of the number of zeros
        zerosCount = 0

        while end < len(nums):
            if nums[end] == 0:
                zerosCount += 1
            # advance the start index when the zerosCount > k
            while zerosCount > k:
                if nums[start] == 0:
                    zerosCount -= 1
                start += 1
            # update the maximum number of consecutive ones
            maxOnes = max(maxOnes, end - start + 1)
            end += 1
        return maxOnes

    if __name__ == 'main':
        print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6)  # True
        print(longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0,
              1, 1, 0, 0, 0, 1, 1, 1, 1], k=3) == 10)  # 10
