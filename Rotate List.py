'''
# Rotate List
-------------
Source: https://leetcode.com/problems/rotate-list/
- Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
    >>> Input: head = [1,2,3,4,5], k = 2
    >>> Output: [4,5,1,2,3]

# Example 2:
    >>> Input: head = [0,1,2], k = 4
    >>> Output: [2,0,1]
 
# Constraints:
    >>> The number of nodes in the list is in the range [0, 500].
    >>> -100 <= Node.val <= 100
    >>> 0 <= k <= 2 * 109
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        ## Algorithm
        '''
        # Sentence Summary
            # Calculate the actual rotation amount and move that amount through the cyclical
                list and remove specific pointers.

        1) Calculate the size of the list
        2) Make the list circular
        3) Set the (LEN - K)th node to have a NULL next reference
        4) Return the node after the (LEN - K)th node, since it is the new start

        # Time Complexity: O(N)
        # Space Complexity: O(1)
        '''
        # edge cases
        if not head or k == 0:
            return head 
        
        # scan the list to determine the length 
        listLength = 1
        counter = head 
        while counter.next:
            listLength += 1
            counter = counter.next
        # the list length is now correct and, 
        # counter points to the lats node 
        # adjust k based on the list length  
        k = k % listLength
        
        # one more edge case - don't rotate at all
        if k == 0:
            return head 
        
        # add a link from the last node to the head node 
        # to make the make the list circular
        counter.next = head 
        
        # to rotate the list by k, we need to get to position # (listLength - k - 1)
        steps = listLength - k - 1
        newEnd = head 
        while steps > 0:
            newEnd = newEnd.next
            steps -= 1
        # newEnd now points to the node that should become the new tail
        # set the new head
        newHead = newEnd.next
        
        # make the tail not have a next
        newEnd.next = None
        # return tghe new head
        return newHead