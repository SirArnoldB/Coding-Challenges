'''
Linked List Cycle
-----------------
# Source: https://leetcode.com/problems/linked-list-cycle/

- Given head, the head of a linked list, determine if the linked list has a cycle in it.
- There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
- Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
- Note that pos is not passed as a parameter.
- Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
    >>> Input: head = [3,2,0,-4], pos = 1
    >>> Output: true
    >>> Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
    >>> Input: head = [1,2], pos = 0
    >>> Output: true
    >>> Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
    >>> Input: head = [1], pos = -1
    >>> Output: false
    >>> Explanation: There is no cycle in the linked list.

# Constraints:
    >>> The number of the nodes in the list is in the range [0, 104].
    >>> -105 <= Node.val <= 105
    >>> pos is -1 or a valid index in the linked-list.
'''

'''
Solution1: Floyd's Cycle Finding Algorithm
----------
# O(n) - time | O(1) - space: where n is the number of nodes in the linked list 
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # initialize two pointers, fast and slow
        # fast moves twice as slow, while slow moves one node at a time , normal
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            # fast moves twice as slow
            fast = fast.next.next
            
            if fast == slow:
                # we have a cycle
                return True
        # if there s no cycle in the list, the fast pointer will eventually reach the end 
        return False 
            
'''
Solution 2: Using a hash set
----------
O(n) - time | O(n) - space: where n is the number of nodes in the list
'''     
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # Algorithm
        '''
        - Loop through the nodes one by one, 
        - record each node's reference in the hash set
        - if the current node is null, then we have reached the end of the list, 
        - therefore, no cycle
        - if current node's reference is in the hash table, we return true
        '''
        # set to store the nodes we have seen 
        nodesSeen = set()
        while head is not None:
            # if the head is in the set, we have found a cycle
            if head in nodesSeen:
                return True
            # add the head to the set 
            nodesSeen.add(head)
            head = head.next
        # no cycle
        return False 
            