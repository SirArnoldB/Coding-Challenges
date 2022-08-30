class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Sorts nums in place, putting objects of the same color adjacent to each other.
        
        Source: https://leetcode.com/problems/sort-colors/?envType=study-plan&id=data-structure-ii
        """
        
        # left and right pointers to partition nums
        # left(values < 1) | middle(values = 1) | right(values > 1)
        left, right = 0, len(nums) - 1
        # pointer to scan through nums
        nums_p = 0
        
        while nums_p <= right:
            if nums[nums_p] > 1:
                nums[nums_p], nums[right] = nums[right], nums[nums_p]
                right -= 1
            elif nums[nums_p] < 1:
                nums[nums_p], nums[left] = nums[left], nums[nums_p]
                left += 1
                nums_p += 1
            else:
                nums_p += 1
