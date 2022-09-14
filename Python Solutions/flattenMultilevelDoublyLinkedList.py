# Source: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        if not head:
            return head
        
        dummy_node = Node(0)
        curr, stack = dummy_node, [head]
        
        while stack:
            temp = stack.pop()
            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)
            curr.next = temp
            temp.prev = curr
            temp.child = None
            curr = temp
        dummy_node.next.prev = None
        
        return dummy_node.next