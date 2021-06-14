"""
Intersection of Two Arrays
--------------------------
Source: https://leetcode.com/problems/intersection-of-two-arrays/

- Given two integer arrays nums1 and nums2, return an array of their intersection. 
- Each element in the result must be unique and you may return the result in any order.

# Example 1:
>>> Input: nums1 = [1,2,2,1], nums2 = [2,2]
>>> Output: [2]

# Example 2:
>>> Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
>>> Output: [9,4]
>>> Explanation: [4,9] is also accepted.
 
# Constraints:
>>> 1 <= nums1.length, nums2.length <= 1000
>>> 0 <= nums1[i], nums2[i] <= 1000
"""
'''
Solution 1
----------
'''
class Solution:
    def intersection(nums1, nums2):
        '''
        # Algorithm 
        - Intersection; elements which appear in both arrays
        - create a set for nums1, nums1Set; 
        - create a set, interSection, to store the common elements; 
        - loop through nums2:
            - if nums2[i] in nums1Set:
                - add it to the interSection set
        - return interSection as a list
        '''
        nums1Set = set(nums1)
        interSection = set()
        for num in nums2:
            if num in nums1Set:
                interSection.add(num)
        return list(interSection)
        
'''
Solution 2
----------
'''
# O(n + m) - time (average) | O(n x m) - time (worst case)
class Solution:
    def intersection(nums1, nums2):
        # Use Built-in Set Intersection
        set1 = set(nums1) # O(n) - time
        set2 = set(nums2) # O(m) - time
        return list(set2 & set1)