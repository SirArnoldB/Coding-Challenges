"""
Product Sum
-----------
Source: https://www.algoexpert.io/questions/Product%20Sum
- Write a function that takes in a "special" array and returns its product sum.
- A "special" array is a non-empty array that contains either integers or other "special" arrays. 
- The product sum of a "special" array is the sum of its elements, where "special" arrays inside it are summed themselves and then
- multiplied by their level of depth. The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1 ; the depth of the inner
- array in [[]] is 2 ; the depth of the innermost array in [[[]]] is 3 . Therefore, the product sum of [x, y] is x + y ; the product sum of [x, [y, z]] is x + 2 * (y + z) ;
- the product sum of [x, [y, [z]]] is x + 2 * (y + 3z) .
"""
# O(n) - time | O(d) - space : where n is the total  number of elements in the array
# including su-elements, and d is the greatest depth of "special" arrays in the array
def productSum(array):
	"""
	Algorithm:
	- call productSumHelper()
	- Inside productSumHelper:
		- initialize helperSum = 0
		- iterate through all of the array's elements 
		- if element is a number, multiply it by the multiplier and add the result to helperSum 
		- if the element is another "special array", add (multiplier * recursive call to productSumHelper) to helperSum 
		- the arguments for the productHelperSum will be the array element, and multiplier plus 1 
		- when all ements have been visited, return helperSum 
	"""
	return productSumHelper(array, 1)
def productSumHelper(array, multiplier):
	helperSum = 0
	# Base case 
	if array == []:
		helperSum += 0
	else:
		# iterate through all the elements in the array
		for element in array:
			# check the type of element
			if type(element) is int:
				helperSum += element
			else:
				# element is a "special array"
				# do a recursive call 
				helperSum += productSumHelper(element, multiplier + 1)
		return helperSum * multiplier

array = [9, [2, -3, 4], 1, [1, 1, [1, 1, 1]], [[[[3, 4, 1]]], 8], [1, 2, 3, 4, 5, [6, 7], -7], [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7], [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]], -3]
print(productSum(array))
# Ouput: 1351