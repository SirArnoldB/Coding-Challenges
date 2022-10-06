# Source: https://www.pramp.com/challenge/3QnxW6xoPLTNl5jX5LM1

# Pancake Sort
# Given an array of integers arr:

# Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
# Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.
# Example:

# input:  arr = [1, 5, 4, 3, 2]

# output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
# Analyze the time and space complexities of your solution.

# Note: it’s called pancake sort because it resembles sorting pancakes on a plate with a spatula, where you can only use the spatula to flip some of the top pancakes in the plate. To read more about the problem, see the Pancake Sorting Wikipedia page.

# Constraints:

# [time limit] 5000ms

# [input] array.integer arr

# [input] integer k

# 0 ≤ k
# [output] array.integer


def flip(arr, k):
    left = 0
    while left < k:
        arr[left], arr[k - 1] = arr[k - 1], arr[left]
        left += 1
        k -= 1


def pancake_sort(arr):
    def getIndex(right):
        largest = arr[0]
        idx = 0
        for i in range(right):
            if arr[i] > largest:
                largest = arr[i]
                idx = i
        return idx

    right = len(arr)
    while right > 0:
        max_idx = getIndex(right)
        flip(arr, max_idx + 1)
        flip(arr, right)
        right -= 1
    return arr


import unittest


class TestPancakeSort(unittest.TestCase):
    def testOne(self):
        self.assertEqual(pancake_sort([1, 5, 4, 3, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(pancake_sort([1, 5, 2]), [1, 2, 5])
        self.assertEqual(pancake_sort([1, 4, 3, 2]), [1, 2, 3, 4])
        self.assertEqual(pancake_sort([2, 1]), [1, 2])
        self.assertEqual(pancake_sort([1]), [1])


if __name__ == "__main__":
    unittest.main()
