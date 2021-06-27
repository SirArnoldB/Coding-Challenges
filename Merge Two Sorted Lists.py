'''
## Merge Two Sorted Lists
-------------------------
Source: https://leetcode.com/problems/merge-two-sorted-lists/

- Merge two sorted linked lists and return it as a sorted list. 
- The list should be made by splicing together the nodes of the first two lists.

# Example 1:
    >>> Input: l1 = [1,2,4], l2 = [1,3,4]
    >>> Output: [1,1,2,3,4,4]

# Example 2:
    >>> Input: l1 = [], l2 = []
    >>> Output: []

# Example 3:
    >>> Input: l1 = [], l2 = [0]
    >>> Output: [0]

# Constraints:
    >>> The number of nodes in both lists is in the range [0, 50].
    >>> -100 <= Node.val <= 100
    >>> Both l1 and l2 are sorted in non-decreasing order.
'''

'''
Solution: Using a dummy node
--------
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Algorithm
        '''
        - create a dummy node, mergedList to hold the merged list
        - loop through nodes 1 and 2,
        - if node2.val > node1.val, mergedListTail = node2, else node1
        - update mergedListTail,  
        - after the loop, check if there is any node in node1 or node2
        - if so, update mergedListTail.next
        '''
        # dummy node 
        mergedList = ListNode(0)
        mergedListTail = mergedList

        # compare node values of l1 and l2, and update the dummy node tail
        while l1 and l2:
            if l2.val < l1.val:
                mergedListTail.next = l2
                l2 = l2.next
            else:
                mergedListTail.next = l1
                l1 = l1.next
            
            mergedListTail = mergedListTail.next
        # if a node is still present in one of the two nodes, l1 and l2
        # if so, append it to the tail node since its already sorted
        if l2: mergedListTail.next = l2
        if l1: mergedListTail.next = l1
            
        return mergedList.next