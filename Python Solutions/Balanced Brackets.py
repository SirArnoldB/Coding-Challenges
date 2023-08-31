"""
Balanced Brackets
-----------------
Source: https://www.algoexpert.io/questions/Balanced%20Brackets

- Write a function that takes in a string made up of brackets ( ( , [ , { , ) , ] , and } ) and
- other optional bracketacters. 
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

"""
Solution
"""


# O(n) - time | O(n) - space : where n is the length of the input string
def balancedBrackets(string):
    stack = []
    bracketsMap = {")": "(", "]": "[", "}": "{"}
    openingBrackets = {"(", "{", "["}

    for bracket in string:
        # if bracket is a closing bracket
        if bracket in bracketsMap:
            # compare the top bracket in the stack with the bracket,
            # if the stack is empty, assign top bracket to a dummy string, "#"
            top_bracket = stack.pop() if stack else "#"
            # compare the top bracket in the stack with the bracket,
            if top_bracket != bracketsMap[bracket]:
                return False
        elif bracket in openingBrackets:
            stack.append(bracket)

    return not stack


import unittest


class TestBalancedBrackets(unittest.TestCase):
    def balancedBrackets(self):
        self.assertEquals(balancedBrackets("([])(){}(())()()"), True)


if __name__ == "__main__":
    unittest.main()
