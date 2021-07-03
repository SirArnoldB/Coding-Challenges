'''
# Intersection of Two Arrays II
-------------------------------
Source: https://leetcode.com/problems/intersection-of-two-arrays-ii/
- Given two integer arrays nums1 and nums2, return an array of their intersection. 
- Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
    >>> Input: nums1 = [1,2,2,1], nums2 = [2,2]
    >>> Output: [2,2]
# Example 2:
    >>> Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    >>> Output: [4,9]
# Explanation: [9,4] is also accepted.

# Constraints:
    >>> 1 <= nums1.length, nums2.length <= 1000
    >>> 0 <= nums1[i], nums2[i] <= 1000
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # nums1 mapping 
        # loop through nums1
            # mapping each number to its count
        
        # intersection = []
        
        # loop nums2
            # check if num is in mappingnums1:
                # check if the count is not 0:
                    # append to intersection
                    # reduce the count of 
                    
        # keeps track of mapping of numbers in nums1 to their count
        nums1Mapping = {}
        # for each num in nums1, mapp it to its count
        for num in nums1:
            if num in nums1Mapping:
                nums1Mapping[num] += 1
            else:
                nums1Mapping[num] = 1
        # keeps track of the common elements between the two arrays
        intersection = []
        # for each num in nums2, if its in nums1Mapping, add it to the intersection array
        # if the count in nums1Mapping is greater than 0
        for num in nums2:
            if num in nums1Mapping:
                if nums1Mapping[num] > 0:
                    intersection.append(num)
                    nums1Mapping[num] -= 1
        # array of intersection
        return intersection

'''
# Follow up:
    >>> What if the given array is already sorted? How would you optimize your algorithm?
    >>> What if nums1's size is small compared to nums2's size? Which algorithm is better?
    >>> What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
    '''