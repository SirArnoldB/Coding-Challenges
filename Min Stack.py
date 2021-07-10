'''
## Min Stack
------------
Source: https://leetcode.com/problems/min-stack/

- Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
- Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# Example 1:
    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

# Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2

# Constraints:
    # -231 <= val <= 231 - 1
    # Methods pop, top and getMin operations will always be called on non-empty stacks.
    # At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # data stack 
        self.dataStack = []
        # minimum stack 
        self.minStack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.dataStack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        # if the top element in data stack is the same as the 
        # top element in the min stack, pop from min stack as well
        if self.minStack[-1] == self.dataStack[-1]:
            self.minStack.pop()
        # pop from the data stack
        self.dataStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.dataStack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # return the top element from the minimum stack
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()