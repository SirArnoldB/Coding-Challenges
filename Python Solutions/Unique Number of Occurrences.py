"""
Unique Number of Occurrences:
-----------------------------
https://leetcode.com/problems/unique-number-of-occurrences/
- Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Examples:
*********

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
________________

Input: arr = [1,2]
Output: false
_________________

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
_________________

Constraints:

    # 1 <= arr.length <= 1000
    # -1000 <= arr[i] <= 1000
"""


# O(nlogn) - time | O(n) - space: where n is the number of elements in arr
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        '''
        - sort the arr
        - create a dict that keeps track of the occurrences we have 
        - if we find an occurrence thats already in dict, we return False, True otherwise
        - for i in arr:
            - check if arr[i] equals arr[i + 1]
            - if so, increment count, else 
            - check if count is already in the occurrences dict, 
            - if so, return False, 
            - else, add count to the occurrences dict
            - and change count to 1
        '''
        # keeps track of occurences of each number.
        occurrences = {}
        # sorting numbers in ascending order makes it easy to compare at number at i with that at i + 1.
        arr.sort()

        idx, count = 0, 1
        while idx < len(arr) - 1:
            if arr[idx] == arr[idx + 1]:
                count += 1
            else:
                if count in occurrences:
                    return False
                occurrences[count] = True
                count = 1
            idx += 1
            if idx == len(arr) - 1:
                if count in occurrences:
                    return False
                occurrences[count] = True
        return True