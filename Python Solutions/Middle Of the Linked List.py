"""
Middle of the Linked List
-------------------------
Source: https://leetcode.com/problems/middle-of-the-linked-list/

- Given a non-empty, singly linked list with head node head, return a middle node of linked list.
- If there are two middle nodes, return the second middle node.

# Example 1:
    >>> Input: [1,2,3,4,5]
    >>> Output: Node 3 from this list (Serialization: [3,4,5])
        The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
        Note that we returned a ListNode object ans, such that:
        ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

# Example 2:
    >>> Input: [1,2,3,4,5,6]
    >>> Output: Node 4 from this list (Serialization: [4,5,6])
    >>> Since the list has two middle nodes with values 3 and 4, we return the second one.

# Note: The number of nodes in the given list will be between 1 and 100.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Solution 1: 
'''

# O(n) - time | O(1) - space : where n is the length of the input listNode
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        '''
        Algorithm
        ---------
        - Iterate through the linked list
        - keep track of the length of the linked list. 
        - Do a second iteration, and stop at node where numberOfNodesSeen = length//2
        - return the current Node
        '''
        # method to get the length of the listNode 
        def getLength(head):
            # keeps track of the length of the list node 
            length = 0
            # first iteration - to get the length of the list node
            while head:
                # update the length 
                length += 1

                head = head.next
            return length
        
        # get the middle of the list node
        middle = getLength(head)//2
        
        # keeps track of the number of nodes we have see
        numberOfNodesSeen = 0
        # second iteration - to get the middle node
        while head:
            # if number of nodes seen equals middle, we have found the middle node
            if numberOfNodesSeen == middle:
                return head
            # else increment the number of nodes seen
            numberOfNodesSeen += 1
            
            head = head.next

# ****************************************************************************** # 

'''
Solution 2: Fast and Slow Pointer
'''
# O(n) - time | O(1) - space : where n is the number of nodes in the given list
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        '''
        Algorithm:
        ----------
        - when traversing the list with a pointer slo, 
        - make another pointer fast that traverses twice as fast. 
        - when fast reaches the end of the list, slow must be in the middle
        '''
        # initialize slow and fast pointers as the headnode
        slow = fast = head
        while fast and fast.next:
            # slow is the normal pointer, goes one head node at a time
            slow = slow.next
            # fast is the faster pointer, goes twice as slow
            fast = fast.next.next
        # when fast reaches the end of the list, slow must be in the middle
        return slow