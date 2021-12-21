'''
# Infix expression: 
    # The expression of the form a op b. 
    # When an operator is in-between every pair of operands. 
# Postfix expression: 
    # The expression of the form a b op. 
    # When an operator is followed for every pair of operands. 

# Examples 
    Input : abc++
    Output : (a + (b + c))

    Input  : ab*c+
    Output : ((a*b)+c)
'''

### Algorithm 
"""
1.While there are input symbols left 
…1.1 Read the next symbol from the input. 
2.If the symbol is an operand 
…2.1 Push it onto the stack. 
3.Otherwise, 
…3.1 the symbol is an operator. 
…3.2 Pop the top 2 values from the stack. 
…3.3 Put the operator, with the values as arguments and form a string. 
…3.4 Push the resulted string back to stack. 
4.If there is only one value in the stack 
…4.1 That value in the stack is the desired infix string. 
"""

# Impplementation 

# function to check if a value is an operand or not
def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))

# Get Infix for a given postfix expression
def getInfix(exp) :
    # stack to keep track of operands
    stack = []
    # for every char in the expression 
    for char in exp:    
        # Push operands
        if (isOperand(char)) :        
            stack.append(char)

        # We assume that input is a valid postfix and expect an operator.
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append("(" + operand2 + char + operand1 + ")")
    # There must be a single element in stack now which is the required infix.
    return stack[0]

# Driver Code
if __name__ == '__main__':
    exp = "ab*c+"
    print(getInfix(exp.strip()))