'''
Remove Duplicates from Sorted List II
-------------------------------------
Source: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

- Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
- leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Example 1:
    >>> Input: head = [1,2,3,3,4,4,5]
    >>> Output: [1,2,5]

# Example 2:
    >>> Input: head = [1,1,1,2,3]
    >>> Output: [2,3]

# Constraints:
    >>> The number of nodes in the list is in the range [0, 300].
    >>> -100 <= Node.val <= 100
    >>> The list is guaranteed to be sorted in ascending order.
'''

# O(n) - time | O(1) - space: where n is the number of nodes in the head

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # sentinel node 
        sentinel = ListNode(0, head)
        
        # predecessor = the last node before the sublist of duplictes
        pred = sentinel 
        
        while head:
            # if it's a beginning of duplicates sublist, skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates 
                pred.next = head.next
            # otherwise, move predecessor
            else:
                pred = pred.next
            
            # move forward
            head = head.next
        
        return sentinel.next