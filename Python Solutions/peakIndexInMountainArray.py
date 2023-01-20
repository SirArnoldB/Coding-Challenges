# Source: https://leetcode.com/problems/peak-index-in-a-mountain-array/

# Peak Index in a Mountain Array

# An array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.


# Example 1:

# Input: arr = [0,1,0]
# Output: 1

# Example 2:

# Input: arr = [0,2,1,0]
# Output: 1

# Example 3:

# Input: arr = [0,10,5,2]
# Output: 1

# Constraints:

# 3 <= arr.length <= 105
# 0 <= arr[i] <= 106
# arr is guaranteed to be a mountain array.
from typing import List

def peakIndexInMountainArray(self, arr: List[int]) -> int:
    if len(arr) == 3:
        return arr[1]
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left)// 2
        
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        
        if arr[mid] > arr[-1] and arr[mid] > arr[mid + 1]:
            right = mid - 1
        else:
            left = mid + 1
                
import unittest

class TestFindMin(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(peakIndexInMountainArray([0, 1, 2, 3]), 0)
        self.assertEqual(peakIndexInMountainArray([15, 45, 69]), 15)
        self.assertEqual(peakIndexInMountainArray([60]), 60)
    def test_rotated_array(self):
        self.assertEqual(peakIndexInMountainArray([4,5,6,7,0,1,2]), 0)
        self.assertEqual(peakIndexInMountainArray([3,4,5,1,2]), 1)
        self.assertEqual(peakIndexInMountainArray([1, 1, 3, 5, 8, 0]), 0)

if __name__ == '__main__':
    unittest.main()
