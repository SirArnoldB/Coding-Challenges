# O(nlogn) - time | O(1) - space : where n is the number of queries
def minimumWaitingTime(queries):
    ## Understand:
	'''
	- executing the shortest query first is what will lead to the minimum waiting time
	- because all queries after it will also have to wait a short/minimum time
	- if we execute the query with the largest amount of time first, it means that
	- all the queries after it will have to wait a minimum of that amount of time
	- therefore, the idea is that we need to start with the query with the minimum amount of time
	'''
	## Algorithm
	#example of a greedy algorithm
	'''
	- sort the array in place O(nlogn) - time
	- keep track of the total waiting time, waitingTime = 0
	- loop through the sorted array of queries 
		- update the waitingTime
		- multiply the number of queries left by the duration of the current query
		- and add that to the total waiting time
	'''
	# if queries only has one entry
	if len(queries) == 1:
		return 0
	# sort the queries in place
	# queries arranged from the smallest to the largest
	queries.sort()
	# initialize the waiting time to 0
	waitingTime = 0
	n = len(queries) - 1
	# loop through the array 
	for i in range(n):
		# n - 1 gives the number of queries left excluding the current query
		waitingTime += queries[i] * (n - i)
	return waitingTime

"""
Minimum Waiting Time
--------------------
# Source: https://www.algoexpert.io/questions/Minimum%20Waiting%20Time

- You're given a non-empty array of positive integers representing the amounts of time that specic
- queries take to execute. Only one query can be executed at a time, but the queries can be executed in any order.
- A query's waiting time is dened as the amount of time that it must wait before its execution starts.
- In other words, if a query is executed second, then its waiting time is the duration of the rst query; if
- a query is executed third, then its waiting time is the sum of the durations of the rst two queries.

- Write a function that returns the minimum amount of total waiting time for all of the queries. For
- example, if you're given the queries of durations [1, 4, 5] , then the total waiting time if the
- queries were executed in the order of [5, 1, 4] would be (0) + (5) + (5 + 1) = 11 . 
- The first query of duration 5 would be executed immediately, so its waiting time would be 0 , the
- second query of duration 1 would have to wait 5 seconds (the duration of the rst query) to be
- executed, and the last query would have to wait the duration of the rst two queries before being executed.

# Note: you're allowed to mutate the input array.

# Sample Input
>>> queries = [3, 2, 1, 2, 6]

# Sample Output
>>> 17
"""