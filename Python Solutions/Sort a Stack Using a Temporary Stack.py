'''
## Sort a stack using a temporary stack
---------------------------------------
- Write a program to sort a stack such that the smallest items are on top. 
- You can use an additional temporary stack, but you may not copy elements into any other data structure (such as an array). 
- The stack supports the following operations : push, pop, peek, isEmpty

Examples:

Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Input : [3, 5, 1, 4, 2, 8]
Output : [1, 2, 3, 4, 5, 8]
'''

### Solution 

# Algorithm
'''
1. Create a temporary stack, tempStack
2. While input stack is NOT empty:
    a. pop an element from the input stack, call it, lastElement
    b. while tempStack is NOT empty && top of stack is less than lastElement
        a. pop from tempStack and push it to the input stack.
    c. push lastElement into tempStack
3. The sorted numbers are in tempStack 
'''

# fucntion returns a sorted stack 
def sortStack(stack):
    # initialize the temporary stack
    tempStack = []
    while stack:
        # pop out the first element
        lastElement = stack.pop()
        # while tempStack is not empty, and top element in temp stack is less that lastElement
        while tempStack and tempStack[-1] > lastElement:
            # pop from the tempStack
            element = tempStack.pop()
            # push the element into the stack
            stack.append(element)
        # push lastElement into tempStack
        tempStack.append(lastElement)
    # tempStack contains the sorted stack
    return tempStack

# Tester code 

import unittest


class TestClass(unittest.TestCase):

    def test_sortStack(self):
        self.assertEqual(sortStack([34, 3, 31, 98, 92, 23]), [3, 23, 31, 34, 92, 98], "Should be [3, 23, 31, 34, 92, 98]")

if __name__ == '__main__':
    unittest.main()
