'''
# Array Of Products
# -----------------
# Source: https://www.algoexpert.io/questions/Array%20Of%20Products

# Write a function that takes in a non-empty array of integers and returns an array of the
# same length, where each element in the output array is equal to the product of every
# other number in the input array.
# In other words, the value at output[i] is equal to the product of every number in the
# input array other than input[i] .
# Note that you're expected to solve this problem without using division.

# Sample Input
# array = [5, 1, 4, 2]
# Sample Output
# [8, 40, 10, 20]
# // 8 is equal to 1 x 4 x 2
# // 40 is equal to 5 x 4 x 2
# // 10 is equal to 5 x 1 x 2
# // 20 is equal to 5 x 1 x 4
'''
# O(n) - time | O(n) - space : where n is the length of the input array
def arrayOfProducts(array):
    products = [0 for _ in range(len(array))]
    leftProducts = [0 for _ in range(len(array))]
    rightProducts = [0 for _ in range(len(array))]
    
    leftRunningProduct = 1
    for i in range(len(array)):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]
        
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]
        
    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]
        
    return products

import unittest

class TestArrayOfProducts(unittest.TestCase):
    def test_valid_input(self):
        self.assertEquals(arrayOfProducts([5, 1, 4, 2]), [8, 40, 10, 20])

if __name__ == "__main__":
    unittest.main()