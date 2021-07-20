# Longest Substring Without Duplication
# --------------------------------------- # 
# Source: https://www.algoexpert.io/questions/Longest%20Substring%20Without%20Duplication

# Write a function that takes in a string and returns its
# longest substring without duplicate characters.
# You can assume that there will only be one longest
# substring without duplication.

# Sample Input
# string = "clementisacap"
# Sample Output
# "mentisac"

# Solution 
# O(n) - time | O(n) - space : where n is the length of the input string
def longestSubstringWithoutDuplication(s):
	"""
	:type s: str
	:rtype: int
	"""

	# Plan:

	# Keep track of window character uniqueness, 
	# with a character dictionary that tracks the count of chars
	# Keep track of current maximum length

	# Look at our window,
	# If it is entirely unique: 
		# Maybe update our Max?
		# Maybe update our longest Substring?
		# Move the right pointer
	# If it isn't unique: 
		# Move the left pointer

	if not s:
		return 0

	left = right = 0
	curMax = 0
	charDict = {s[0]: 1}
	isUnique = True

	while right < len(s):
		# Is the substring window unique?
		if isUnique:
			# Increment the right side of the window
			if right + 1 - left > curMax:
				# update the current max length 
				curMax = right + 1 - left
				longestIndexes = [left, right + 1]
				
			right += 1
			if right < len(s):
				charDict[s[right]] = charDict.get(s[right], 0) + 1
				if charDict[s[right]] > 1:
					isUnique = False

		else:
			# Increment the left side of the window
			charDict[s[left]] = charDict[s[left]] - 1
			left += 1
			if charDict[s[right]] == 1:
				isUnique = True

	return s[longestIndexes[0] : longestIndexes[1]]
