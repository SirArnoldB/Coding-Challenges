# O(nlog n) - time | O(1) - space : n is the number of coins
def nonConstructibleChange(coins):
	"""
	Brute Force Method:
	*******************
	>>> Loop through all of the positive integers, 
	>>> untill you reach one that you cannot create 
	"""
	
	"""
	Optimal Solution:
	*****************
	sorting(O(nlogn)), iterating (O(n))
	
	>>> sort the input array
	>>> var change = num, will tell us how much change we can currently create
	>>> we can make all the values between 1..num inclusive
	>>> loop through the sorted list, and see how much change we can make with those coins
	>>> start with change = 0, check the first value. If the first value is 1, 
	>>> it means we can create 1, so we move on to the next one
	>>> check if the current coin is greater than the amount of change + 1, 
	>>> If yes, we return change + 1 because we won't be able to make it using the coins that we have
	>>> If the current coin is less or equal to the amount of change + 1, we add that to the current change
	>>> what this means is that we can create coin changes between 1... num, where num is current change + current coin which is less than or equal to our previous current change
	>>> If we reach the end of the list, that would mean that we cannot make 1 more than the current change that we have
	"""
	# sort the input array inplace
	coins.sort()      # O(nlogn) - time, O(1) - space (sorting the array in place)
	
	currentChangeCreated = 0
	# loop through all the coins
	# O(n) - time
	for coin in coins:
		# check the value of the coin
		if coin > currentChangeCreated + 1:
			# this means that we cannot create a coin change of currentChangeCreated + 1
			# therefore we have found the minimum amount of change that we cannot create
			return currentChangeCreated + 1
		# update the current change that we can actually create
		# add the current value of the coin to currentChangeCreated, 
		# this would mean that we can now create coin change up to the currentChangeCreated that we have
		currentChangeCreated += coin
	# Otherwise return the current change created + 1 
	# because thats the next value that we cannot create
	return currentChangeCreated + 1
