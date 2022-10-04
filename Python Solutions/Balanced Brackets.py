"""
Balanced Brackets
-----------------
Source: https://www.algoexpert.io/questions/Balanced%20Brackets

- Write a function that takes in a string made up of brackets ( ( , [ , { , ) , ] , and } ) and
- other optional characters. 
- The function should return a boolean representing whether the string is balanced with regards to brackets.
- A string is said to be balanced if it has as many opening brackets of a certain type as it has
- closing brackets of that type and if no bracket is unmatched. 
- Note that an opening bracket can't match a corresponding closing bracket that comes before it, and similarly, a closing bracket
- can't match a corresponding opening bracket that comes after it. Also, brackets can't overlap each other as in [(]) .

# Sample Input
    >>> string = "([])(){}(())()()"
    >>> Sample Output
    >>> true // it's balanced
"""

'''
Solution
'''
# O(n) - time | O(n) - space : where n is the length of the input string
def balancedBrackets(string):
    # stack to keep track of opening brackets
	stack = []
	# hash map to keep track of mappings of closing brackets to opening brackets
	# gives us constant time lookup
	closingBrackets = {")": "(", "]": "[", "}": "{"}
	
	# set to keep track of opening brackets, 
	# gives us constant time look up
	openingBrackets = {"(", "{", "["}
	
	# for each bracket in the string 
	for char in string:
		# if char is a closing bracket
		if char in closingBrackets:
			# compare the top element in the stack with the char, 
			# if the stack is empty, assign top element to a dummy string, "#"
			top_element = stack.pop() if stack else "#"
			# compare the top element in the stack with the char, 
			if top_element != closingBrackets[char]:
				return False
		elif char in openingBrackets:
			stack.append(char)
			
	# In the end, if the stack is empty, then we have a valid expression.
	# The stack won't be empty for cases like ((()
	return not stack

import unittest

class TestBalancedBrackets(unittest.TestCase):
	def balancedBrackets(self):
		self.assertEquals(balancedBrackets("([])(){}(())()()"), True)

if __name__ == "__main__":
	unittest.main()
