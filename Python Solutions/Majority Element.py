# SOlution 1: Using HashMap
class Solution:
    def majorityElement(self, nums):
        """
        Return the majority element that appears more than ⌊n/2⌋ times.
        Assumes that the majority element always exists in the array.
        """
        numsCount = {}
        for num in nums:
            numsCount[num] = numsCount[num] + 1 if num in numsCount else 1
            if numsCount[num] > len(nums)//2:
                return num

# Solution 2: Using Boyer-Moore Voting Algorithm
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
class Solution:
    def majorityElement(self, nums):
        """
        Return the majority element that appears more than ⌊n/2⌋ times.
        Assumes that the majority element always exists in the array.
        """
        # Keeps track of the majority element
        candidate = None
        # keeps track of the count of the majority element
        count = 0
        for num in nums:
            # when count is zero, consider the current num as the candidate
            candidate = num if count == 0 else candidate
            # update the count for the majority element
            count += 1 if num == candidate else -1
        # the candidate now has the majority element
        return candidate
