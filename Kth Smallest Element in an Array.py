'''
# Given an array and a number k where k is less than size of array, 
# we need to find the k’th smallest element in the given array. 
# It is given that all array elements are distinct.

# Examples:

# Input: [7, 10, 4, 3, 20, 15]
#     k = 3
# Output: 7

# Input: [7, 10, 4, 3, 20, 15]
#     k = 4
# Output: 10
'''

# Solution 1: 
# O(n log n) - time | O(1) - space. 

# # Summary: sort the array in place and return the element at k - 1
# def kthSmallest(arr, n, k):
#     # Sort the given array
#     arr.sort()
#     # Return k'th element in the sorted array
#     return arr[k-1]


### Solution 2: Quick Select
'''
# This is an optimization over method 1 if QuickSort is used as a sorting algorithm in first step. 
# In QuickSort, we pick a pivot element, then move the pivot element to its correct position and partition the surrounding array. 
# The idea is, not to do complete quicksort, but stop at the point where pivot itself is k’th smallest element. 
# Also, not to recur for both left and right sides of pivot, but recur for one of them according to the position of pivot. 
# The worst case time complexity of this method is O(n2), but it works in O(n) on average. 
'''

def kthSmallest(arr, k):
    '''
    :type arr List[int]]
    :type k int
    :rtype int
    '''
    return quickSelect(arr, 0, len(arr) - 1, k)

def quickSelect(arr, left, right, k):

    # If k is smaller than number of elements in array
    if (k > 0 and k <= right - left + 1):
    
        # Partition the array around last element and get position of pivot
        # element in sorted array
        pos = partition(arr, left, right)

        # If position is same as k
        if (pos - left == k - 1):
            return arr[pos]
        if (pos - left > k - 1): 
            # If position is more, # recur for left subarray
            return quickSelect(arr, left, pos - 1, k)

        # Else recur for right subarray
        return quickSelect(arr, pos + 1, right, k - pos + left - 1)

    # If k is more than number of elements in array
    return None

# Standard partition process of QuickSort().
# It considers the last element as pivot and moves all smaller element to left of it
# and greater elements to right
def partition(arr, left, right):

    x = arr[right]
    i = left
    for j in range(left, right):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

# Driver Code
if __name__ == "__main__":
    
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3;
    print("K'th smallest element is",
        kthSmallest(arr, k))