# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

# Example Inputs and Outputs
# Example 1:
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true

# Explanation: It is possible to divide nums into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

# Example 2:
# Input: nums = [1,2,3,4], k = 3
# Output: false

# Constraints
# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 104
# The frequency of each element is in the range [1, 4].

import unittest


# Solution
def canPartitionKSubsets(nums: list[int], k: int) -> bool:
    # Calculate the sum of all numbers in the array
    nums_sum = sum(nums)
    # If the sum cannot be evenly divided by k, it is not possible
    if nums_sum % k != 0:
        return False

    # Calculate the target sum for each subset
    target_sum = nums_sum // k
    # Sort the array in descending order to optimize pruning
    nums.sort(reverse=True)
    # Keep track of which numbers have been used in subsets
    used = [False] * len(nums)

    # Depth-first search function to explore all possible subsets
    def dfs(sub_sets_count, cur_sum, start_index):
        # If we have found k subsets, it is a valid partition
        if sub_sets_count == k:
            return True
        # If the current subset sum matches the target sum, move to the next subset
        if cur_sum == target_sum:
            return dfs(sub_sets_count + 1, 0, 0)

        # Iterate through the remaining numbers in the array
        for i in range(start_index, len(nums)):
            # If the number has been used or adding it exceeds the target sum, skip it
            if used[i] or cur_sum + nums[i] > target_sum:
                continue

            # Pruning step: if the current number is the same as the previous number
            # and the previous number hasn't been used, skip the current number
            if i > start_index and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            # Mark the current number as used
            used[i] = True
            # Recursive call to explore the next number and update the subset sum
            if dfs(sub_sets_count, cur_sum + nums[i], i + 1):
                return True
            # Undo the choice of using the current number and try the next number in the array
            used[i] = False

        # If no solution is found, return False
        return False

    # Start the depth-first search from the beginning of the array with an empty subset
    return dfs(0, 0, 0)


# Test Cases


class TestCanPartitionKSubsets(unittest.TestCase):
    def test_can_partition_k_subsets(self):
        self.assertEqual(canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4), True)
        self.assertEqual(canPartitionKSubsets([1, 2, 3, 4], 3), False)

    def test_can_partition_k_subsets_single_element(self):
        self.assertEqual(canPartitionKSubsets([1], 3), False)


if __name__ == "__main__":
    unittest.main()
