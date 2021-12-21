'''
# Partition List
----------------
Source: https://leetcode.com/problems/partition-list/
- Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
- You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:
    # Input: head = [1,4,3,2,5,2], x = 3
    # Output: [1,2,2,4,3,5]
# Example 2:
    # Input: head = [2,1], x = 2
    # Output: [1,2]

# Constraints:
    # The number of nodes in the list is in the range [0, 200].
    # -100 <= Node.val <= 100
    # -200 <= x <= 200
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # Algorith:
            # create two lists to store nodes before and after the node with value x
            # loop through the head, and update each list
            # after the loop, assign before.next to after.next
            # then assign after.next to null
            # return beforeHead
            
        # intialize everything
        # before keeps track of nodes before x
        # after keeps track of nodes greater or equal to x
        beforeHead = before = ListNode(0)
        afterHead = after = ListNode(0)
        
        # traverse through the head node 
        # and compare the value to the head to x
        while head:
            if head.val < x:
                before.next = head
                # advance before
                before = before.next
            else:
                after.next = head
                # advance after 
                after = after.next
            # advance the head
            head = head.next
        # assign before.next  to afterHead.next
        before.next = afterHead.next
        after.next = None
        
        # beforeHead is the correct required head
        return beforeHead.next