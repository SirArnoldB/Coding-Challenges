'''
## Evaluate Reverse Polish Notation
-----------------------------------
Source: https://leetcode.com/problems/evaluate-reverse-polish-notation/

- Evaluate the value of an arithmetic expression in Reverse Polish Notation.
- Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
- Note that division between two integers should truncate toward zero.
- It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

# Example 1:
    # Input: tokens = ["2","1","+","3","*"]
    # Output: 9
    # Explanation: ((2 + 1) * 3) = 9
# Example 2:
    # Input: tokens = ["4","13","5","/","+"]
    # Output: 6
    # Explanation: (4 + (13 / 5)) = 6
# Example 3:
    # Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # Output: 22
    # Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22

# Constraints:
    # 1 <= tokens.length <= 104
    # tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''
import operator

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ### Algorithm
        """
        # Algorithm
            # For every element
            # If the element is a number, push it onto the stack
            # If the element is an operator, pop values from the stack. 
            # Process the sub-expression and push the result back to the stack
        # When there are no more elements to scan, the number in the stack is the result

        """
        # operations set
        opsSet = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}    
        
        # stack to keep track of the tokens which are numbers
        nums = []
        
        for token in tokens:
            if token in opsSet:
                # get the two last elements from the top of the stack
                b, a = nums.pop(), nums.pop()
                
                # get the operator 
                op = opsSet[token]
                
                # get the result of using the operator on the two numbers
                result = int(op(a, b))
                
                # push the result to the stack
                nums.append(result)
            else:
                # push the number onto the stack
                nums.append(int(token))
                            
        # nums only contains one element  
        return nums.pop()

