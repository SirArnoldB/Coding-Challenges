'''
# Intersection of Two Arrays
----------------------------
Source: https://leetcode.com/problems/intersection-of-two-arrays/
- Given two integer arrays nums1 and nums2, return an array of their intersection. 
- Each element in the result must be unique and you may return the result in any order.

# Example 1:
    # Input: nums1 = [1,2,2,1], nums2 = [2,2]
    # Output: [2]
# Example 2:
    # Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    # Output: [9,4]
# Explanation: [4,9] is also accepted.

# Constraints:
    # 1 <= nums1.length, nums2.length <= 1000
    # 0 <= nums1[i], nums2[i] <= 1000
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Algorithm:
        """
        # We create a set for both arrays, which gives us the unique numbers of each array.
        # Then, we perform set intersection to find the equal items amongst the sets.
        
        1) Create set A for nums1.
            a) Add all items of nums1 to A.
        2) Create set B for nums2.
            b) Add all items of nums2 to B.
        3) Perform set intersection of A and B.

        Time Complexity: O(N+M)
        Space Complexity: O(N+M)
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
    