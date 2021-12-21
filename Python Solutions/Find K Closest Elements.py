'''
# Find K Closest Elements
-------------------------
Source: 

- Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
- The result should also be sorted in ascending order.
- An integer a is closer to x than an integer b if:
    >>> |a - x| < |b - x|, or
    >>> |a - x| == |b - x| and a < b

# Example 1:
    >>> Input: arr = [1,2,3,4,5], k = 4, x = 3
    >>> Output: [1,2,3,4]
# Example 2:
    >>> Input: arr = [1,2,3,4,5], k = 4, x = -1
    >>> Output: [1,2,3,4]

# Constraints:
    >>> 1 <= k <= arr.length
    >>> 1 <= arr.length <= 104
    >>> arr is sorted in ascending order.
    >>> -104 <= arr[i], x <= 104
'''
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # initialize everything
        n = len(arr)
        closestElements = []
        
        # Function to find the point where: elements before are smaller than or equal to x, 
        # and elements after are greater than x
        def getPoint(arr, leftIdx, rightIdx, x) :

            # Base cases
            if (arr[rightIdx] <= x) :
                # x is greater than all values 
                return rightIdx

            if (arr[leftIdx] > x) : 
                # x is smaller than all values 
                return leftIdx

            # get the middle piont
            midIdx = (leftIdx + rightIdx) // 2

            # If x is same as middle element, then we return mid
            if (arr[midIdx] <= x and arr[midIdx + 1] > x) :
                return midIdx

            # If x is greater than arr[midIdx], then
            if(arr[midIdx] < x) :
                return getPoint(arr, midIdx + 1, rightIdx, x)

            return getPoint(arr, leftIdx, midIdx - 1, x)
        
        # get the target Point
        targetPoint = getPoint(arr, 0, n - 1, x)
        
        # left index to search 
        if arr[targetPoint] == x:
            closestElements.append(arr[targetPoint])
            k -= 1
            leftIdx = targetPoint - 1
        else:
            leftIdx = targetPoint
            
        # right index to search 
        rightIdx = targetPoint + 1 
        # keep track of the count of elements we have in out closestElements list
        count = 0 

        # Compare elements on left and right of the targetPoint to find the k closest elements
        while (leftIdx >= 0 and rightIdx < n and count < k) :
            if abs(x - arr[leftIdx]) < abs(arr[rightIdx] - x) or (abs(x - arr[leftIdx]) == abs(arr[rightIdx] - x) and arr[leftIdx] < arr[rightIdx])  :
                closestElements.append(arr[leftIdx])
                leftIdx -= 1
            else :
                closestElements.append(arr[rightIdx])
                rightIdx += 1
            count += 1

        # if we have elements on the left but no more elements on the right
        # and we have not reached the count 
        while (count < k and leftIdx >= 0) :
            closestElements.append(arr[leftIdx])
            leftIdx -= 1
            count += 1

        # if we have elements on the right but no more elements on the left
        # and we have not reached the count 
        while (count < k and rightIdx < n) :
            closestElements.append(arr[rightIdx])
            rightIdx += 1
            count += 1
            
        closestElements.sort()
        return closestElements