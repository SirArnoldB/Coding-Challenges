'''
# Swap Nodes in Pairs
---------------------
Source: https://leetcode.com/problems/swap-nodes-in-pairs/

- Given a linked list, swap every two adjacent nodes and return its head. 
- You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:
    >>> Input: head = [1,2,3,4]
    >>> Output: [2,1,4,3]

# Example 2:
    >>> Input: head = []
    >>> Output: []

# Example 3:
    >>> Input: head = [1]
    >>> Output: [1]

# Constraints:
    >>> The number of nodes in the list is in the range [0, 100].
    >>> 0 <= Node.val <= 100
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize everything 
        dummyNode = ListNode(0, head)
        # the node before the next pair of numbers
        beforeNode = dummyNode
        
        # for each pair of adjacent nodes
        while beforeNode.next != None and beforeNode.next.next: # as long as there are two nodes ahead
            # set up temporary pointers to the two nodes 
            firstNode = beforeNode.next
            secondNode = beforeNode.next.next
            
            # do pointer re-arrangement
            beforeNode.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            
            # Move everything forward to the next pair 
            beforeNode = firstNode
        
        # dummyNode.next is the beginning of the re-arranged list
        return dummyNode.next