"""
Longest Balanced Substring
--------------------------

- Write a function that takes in a string made up of parentheses ( ( and ) ). 
- The function should return an integer representing the length of the longest balanced substring with regards to parentheses.
- A string is said to be balanced if it has as many opening parentheses as it has closing parentheses, 
- and if no parenthesis is unmatched. Note that an opening parenthesis can't match a closing parenthesis that comes
- before it, and similarly, a closing parenthesis can't match an opening parenthesis that comes after it.

# Sample Input
    >>> string = "(()))("
#Sample Output
    >>> 4 // The longest balanced substring is "(())"
"""

'''
Solution 1
----------
'''
# O(n) - time | O(n) - space : where n is the length of the string
def longestBalancedSubstring(string):
	# keeps track of the longest substring length
	maxLength = 0
	# keeps track of the indexes of the characters in string
	indexStack = []
	# append -1 to the indexStack as a dummy value that indicates 
	# the very beginning of the array
	indexStack.append(-1)
	
	# for every bracket in the string
	for i in range(len(string)):
		# if the char is an opening bracket, 
		# add its index to the indexStack
		if string[i] == "(":
			indexStack.append(i)
		else:
			# remove the top element from the indexStack 
			indexStack.pop()
			# if the indexStack becomes empty, then the bracket is not matched
			# append the index of the char to the stack
			if len(indexStack) == 0:
				indexStack.append(i)
			else:
				# get the starting index for the balanced sub string
				balancedSubstringStartIdx = indexStack[len(indexStack) - 1]
				# find the length of the balanced substring
				currentLength = i - balancedSubstringStartIdx
				# update the maximum length
				maxLength = max(maxLength, currentLength)
	return maxLength
			
# *********************************************************************************** # 

'''
Solution 2
----------
'''

# O(n) - time | O(1) - space : where n is the length of the input string
def longestBalancedSubstring(string):
    # keeps track of the maximum substring length
    maxLength = 0
    # keeps track of the count of the opening and closing brackets
    openingCount = closingCount = 0
    
    # loop through the string from left to right
    for char in string:
        if char == "(":
            # increment the count for the opening parentheses
            openingCount += 1
        else:
            # increment the count for the closing parentheses
            closingCount += 1
        # check if the counters are the same
        if openingCount == closingCount:
            # update the maxLength
            maxLength = max(maxLength, closingCount * 2)
        # reset the counters if closing counter becomes greater thn the opening counter
        # because it means we have an umatched bracket
        elif closingCount > openingCount:
            openingCount = 0
            closingCount = 0
            
    # loop through the string from right to left
    # this caters for the edge cases we might have iterating from left to right
    openingCount = 0
    closingCount = 0
    
    for i in reversed(range(len(string))):
        char = string[i]
        
        if char == "(":
            openingCount += 1
        else:
            closingCount += 1
        # if the counters are the same
        if openingCount == closingCount:
            # update the maxLength
            maxLength = max(maxLength, openingCount * 2)
        # if we have more opening parentheses than there are closing 
        # reset the counters because we have an un matched parentheses
        elif openingCount > closingCount:
            openingCount = 0
            closingCount = 0
    return maxLength

# *********************************************************************************** # 

# Brute Force Approach 

# O(n^3) time | O(n) space - where n is
def longestBalancedSubstring(string):
    maxLength = 0
    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1, 2):
            if isBalanced(string[i:j]):
                currentLength = j - i
                maxLength = max(maxLength, currentLength)
    return maxLength

def isBalanced(string):
    openParensStack = []
    for char in string:
        if char == "(":
            openParensStack.append("(")
        elif len(openParensStack) > 0:
            openParensStack.pop()
        else:
            return False
    return len(openParensStack) == 0
