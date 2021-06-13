'''
Two Number Sum
**************
Source: https://www.algoexpert.io/questions/Two%20Number%20Sum
- Write a function that takes in a non-empty array of distinct integers and an
- integer representing a target sum. If any two numbers in the input array sum
- up to the target sum, the function should return them in an array, in any order.
- If no two numbers sum up to the target sum, the function should return an empty array.
- Note that the target sum has to be obtained by summing two dierent integers
- in the array; you can't add a single integer to itself in order to obtain the target sum.
- You can assume that there will be at most one pair of numbers summing up to the target sum.

## Sample Input
>>> array = [3, 5, -4, 8, 11, 1, -1, 6]
>>> targetSum = 10

## Sample Output
>>> [-1, 11] // the numbers could be in reverse order
'''
'''
Solution 1: Efficient
----------
'''
# O(nlogn) - time | O(1) - space : where n is the lenght of the input array
def twoNumberSum(array, targetSum):
    # sort the array in place
    array.sort()
    # two pointers to keep track of the left and right number
    left, right = 0, len(array) - 1
    # loop until left pointer becomes greater than right pointer
    while left < right:
        # add the two numbers on the left and right
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            # if the sum equals target, return the two number
            # since we assume that there is at most one pair of numbers summing up to target
            return [array[left], array[right]]
        elif currentSum < targetSum:
            # since array is sorted, to increase the currentSum so that it becomes 
            # possibly equal to target, we incremenet the left pointer to increase the number
            left += 1
        elif currentSum > targetSum:
            # to reduce the sum to make it possibly equal to target sum, 
            # reguce the right number by decrementing the right pointer
            right -= 1
    return []
    _____________________________________________________________

'''
Solution 2: Efficient
---------------------
'''
# O(n) time | O(n) space - where n is the size of the array
def twoNumberSum(array, targetSum):
    #  set to store the elements that we would have traversed. 
    nums = set()
    # for each num in array, find its addend that would add up to targetSum
    # if the addend is in nums, return the two addends, 
    # else, store num in the set, and move on
    for num in array:
        poss_addend = targetSum - num
        if poss_addend in nums:
            return [num, poss_addend]
        else:
            nums.add(num)
    return []

'''
Solution 3: Brute Force
-----------------------
'''
# O(n^2) - time | O(n) - space | where n is the length of the input array
def twoNumberSum(array, targetSum):
	# For every number, check for a possible pair which gives us the target sum
	for num in array:
		i = 0
		while i < len(array):
			# checks if the pair is equal to target sum
			if num + array[i] == targetSum and array[i] != num:
				return [num, array[i]]
			i += 1
	# no two numbers sum up to the target sum
	return []