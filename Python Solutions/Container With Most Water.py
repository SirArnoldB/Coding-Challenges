class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize the result, which keeps track of the maximum area
        res = 0
        # left pointer - keeps track of left index
        # right pointer - keeps track of the right index
        left , right = 0, len(height)-1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            # update the maximum area
            res = max(area, res)
            # This was necessary because the left and right pointer moves through the height once
            if height[left] < height[right]:
                # increment left to check for a new possible greater height
                left += 1
            else:
                # decrement right to check for the next height greater than the previous height
                # if the heights are equal, either increment left pointer or decrement right pointer
                right -= 1
        return res
                