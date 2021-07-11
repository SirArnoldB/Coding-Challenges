'''
### Implement Queue using Stacks
Source:https://leetcode.com/problems/implement-queue-using-stacks/

- Implement a first in first out (FIFO) queue using only two stacks. 
- The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

- Implement the MyQueue class:
    # void push(int x) Pushes element x to the back of the queue.
    # int pop() Removes the element from the front of the queue and returns it.
    # int peek() Returns the element at the front of the queue.
    # boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
- You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively. 
- You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? 
# In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

# Example 1:

# Input
    ["MyQueue", "push", "push", "peek", "pop", "empty"]
    [[], [1], [2], [], [], []]
# Output
    [null, null, null, 1, 1, false]

# Explanation
    MyQueue myQueue = new MyQueue();
    myQueue.push(1); // queue is: [1]
    myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
    myQueue.peek(); // return 1
    myQueue.pop(); // return 1, queue is [2]
    myQueue.empty(); // return false

# Constraints:
    1 <= x <= 9
    At most 100 calls will be made to push, pop, peek, and empty.
    All the calls to pop and peek are valid.
'''
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mainStack = []
        self.sideStack = []
        

    def push(self, x): # O(1) - time
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.mainStack.append(x)
        

    def pop(self):  # O(n) - time | O(n) - space
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.mainStack) == 0:
            return None
            
        # pop to the side stack 
        for i in range(len(self.mainStack) - 1):
            self.sideStack.append(self.mainStack.pop())
        
        temp = self.mainStack.pop()
        
        # pop to the mainStack 
        while self.sideStack:
            self.mainStack.append(self.sideStack.pop())
            
        return temp

    def peek(self): # O(1) - time
        """
        Get the front element.
        :rtype: int
        """
        if len(self.mainStack) == 0:
            return None 
        
        return self.mainStack[0]
        

    def empty(self): # O(1) - time
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.mainStack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()








