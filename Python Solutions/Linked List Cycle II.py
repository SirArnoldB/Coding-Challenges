'''
Linked List Cycle II
--------------------
Source: https://leetcode.com/problems/linked-list-cycle-ii/

- Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
- There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
- Notice that you should not modify the linked list.

# Example 1:
    >>> Input: head = [3,2,0,-4], pos = 1
    >>> Output: tail connects to node index 1
    >>> Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:
    >>> Input: head = [1,2], pos = 0
    >>> Output: tail connects to node index 0
    >>> Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:
    >>> Input: head = [1], pos = -1
    >>> Output: no cycle
    >>> Explanation: There is no cycle in the linked list.

# Constraints:
    >>> The number of the nodes in the list is in the range [0, 104].
    >>> -105 <= Node.val <= 105
    >>> pos is -1 or a valid index in the linked-list.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# O(n) - time | O(1) - space: where n is the number of nodes in the input list 
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        Algorithm
        ---------
        # Phase 1
        - create two pointers, slow - moves at normal rate, and fast - moves twice as slow
        - if there is a cycle, slow and fast are going to meet 
        - when they meet, break
        
        # Phase 2
        - slow will start from the start, and fast will start from the point of intersection, 
        - except, now, both slow and fast are moving at the same pace - fast has been slowed down. 
        - where these two guys meet, that's the entrance to the cycle. 
        '''
        # if the list is empty 
        if head is None:
            return None 
        
        # find out where there is a cylce and intersection point of the cyle
        slow = fast = head
        cyclePresent = False 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                # we have a cylce,
                cyclePresent = True
                break 
        # if no cycle found 
        if cyclePresent == False: return None
                
        # find the cycle entrance
        # now, slow starts from the begining, and fast will start from the point of intersection
        # however fast has been slowed down to move at the same pace as slow. 
        # fast and slow will meet at the entrace of the cycle
        slow = head
        
        while fast is not slow:
            slow = slow.next
            fast = fast.next
            
        return fast