# Source: https://www.algoexpert.io/questions/Smallest%20Difference

'''
### SOLUTION 1:
'''
# O(nlogn) + O(mlogm) - time | O(1) - space: where n and m are the lengths of arrayOne and arrayTwo
def smallestDifference(arrayOne, arrayTwo):
    # sort the two arrays in place
    arrayOne.sort() # sorting in place, takes O(nlogn) - time |  O(1) - space
    arrayTwo.sort() # takes O(nlogn) - time | O(1) - space. 
    
    # pointer for arrayOne and arrayTwo
    array_one_idx = 0
    array_two_idx = 0
    # minimum difference to keep track of
    # initialize it to infinity to make it greater than any difference we have. it will make it easy to update. 
    minimum_diff = float('inf')
    # array to store the pair of numbers that give the smallest difference
    nums = []
    
    while array_one_idx < len(arrayOne) and array_two_idx < len(arrayTwo):
        # find the absolute difference:
        abs_diff = abs(arrayOne[array_one_idx] - arrayTwo[array_two_idx]) if arrayOne[array_one_idx] > arrayTwo[array_two_idx] else abs(arrayTwo[array_two_idx] - arrayOne[array_one_idx])
        # update the minimum difference
        if minimum_diff > abs_diff:
            minimum_diff = abs_diff
            nums = [arrayOne[array_one_idx], arrayTwo[array_two_idx]]
        # if absolute difference is zero, return nums....
        if abs_diff == 0:
            return nums
        elif abs_diff < 0:
            if arrayOne[array_one_idx] < arrayTwo[array_two_idx]:
                array_one_idx += 1
            else: 
                array_two_idx += 1
        else:
            if arrayOne[array_one_idx] < arrayTwo[array_two_idx]:
                array_one_idx += 1
            else:
                array_two_idx += 1
    return nums

'''
### SOLUTION 2:
***************
'''
# O(nlogn) + O(mlogm) - time | O(1) - space : where n and m are the length of arrayOne and arrayTwo
def smallestDifference(arrayOne, arrayTwo):
	# sort the array in place
	# if not allowed to sort in place, write the algorithm for sorting the arrays
	arrayOne.sort()
	arrayTwo.sort()
	# pointers for the two sorted arrays
	arrayOne_idx = 0
	arrayTwo_idx = 0
	# smallest difference to keep track of
	# initialize it to infinity because at the very beginning, 
	# infinity is gonna be greater than any difference, meaning we can update it accordingly
	smallest_diff = float('inf')
	# current difference
	current_diff = float('inf')
	# smallest pair that we are also keeping track of
	smallest_pair = []
	
	while arrayOne_idx < len(arrayOne) and arrayTwo_idx < len(arrayTwo):
		first_num = arrayOne[arrayOne_idx]
		second_num = arrayTwo[arrayTwo_idx]
		
		if first_num < second_num:
			# update the current difference
			current_diff = second_num - first_num
			# increment the arrayOne_idx pointer to make first_num potentially be closer to second_num
			# because we want to make the gap between the two numbers as smaller
			arrayOne_idx += 1
		elif second_num < first_num:
			# update the current difference
			current_diff = first_num - second_num 
			# increment the arrayTwo index pointer 
			# to make second_num potentially closer to first_num 
			arrayTwo_idx += 1
		else:
			return [first_num, second_num]
		# update the smallest difference
		if smallest_diff > current_diff:
			smallest_diff = current_diff 
			smallest_pair = [first_num, second_num]
	return smallest_pair