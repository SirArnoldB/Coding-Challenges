"""
Remove Element
**************
Source: https://leetcode.com/problems/remove-element/

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""
class Solution:
    # O(n) - time | O(1) - space
    def removeElement(self, nums: List[int], val: int) -> int:
        # left and right index to keep track of left and right values
        leftIdx, rightIdx = 0, len(nums) - 1
        
        while leftIdx < rightIdx:
            # advance the right pointer untill it points to 
            # a num not equal to val
            while nums[rightIdx] == val and rightIdx > leftIdx:
                rightIdx -= 1
            # advance the left pointer until it points to a num
            # equal to val
            while nums[leftIdx] != val and leftIdx < rightIdx:
                leftIdx += 1
            if leftIdx >= rightIdx:
                break
            else:
                # swap the values on the leftIdx and rightIdx
                # this moves all numbers equal to val to the end of the list
                nums[leftIdx], nums[rightIdx] = nums[rightIdx], nums[leftIdx]
                
        return rightIdx if (rightIdx == 0 and nums[rightIdx] == val) else rightIdx + 1
                
