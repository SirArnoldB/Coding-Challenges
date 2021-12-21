"""
Remove Nth Node From End of List
--------------------------------
Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

- Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
    >>> Input: head = [1,2,3,4,5], n = 2
    >>> Output: [1,2,3,5]

# Example 2:
    >>> Input: head = [1], n = 1
    >>> Output: []

# Example 3:
    >>> Input: head = [1,2], n = 1
    >>> Output: [1]

# Constraints:
    >>> The number of nodes in the list is sz.
    >>> 1 <= sz <= 30
    >>> 0 <= Node.val <= 100
    >>> 1 <= n <= sz
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Solution 1:
----------
'''
# O(n) - time | O(1) - space : where n is the number of nodes in the input head
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        Algorithm
        ---------
        - make initial pass through liked list to get length 
        - make second pass to remove any reference to nth to last node
        
        # Example:
        - Given linked list 1 -> 2 -> 3, n = 1; we want to return 1 -> 2
        
        - First pass, we get length = 3. Since n = 1, 
        - that means we want to remove the 3 - 1 = 2 node (with indexing starting at 0)
        
        - As we iterate through the list:
            - at node 1 -> numberOfNodesSeen = 0, previousNode = null
            - at node 2 -> numberOfNodesSeen = 1, previousNode = 1
            - at node 3 -> numberOfNodesSeen = 2, previousNode = 2 -> we set 
            - previousNode.next = node.next (node 3's next = null)
        '''
        # helper method to get the length of the linked list 
        def getLength(head):
            # intialize length to 0
            length = 0
            while head:
                # update the length, and head node 
                length += 1
                head = head.next
            return length 
        # get the position of the node we want to remove with indexing starting at 0
        nodeToRemove = getLength(head) - n
        # keeps track of the number of nodes that we have seen 
        numberOfNodesSeen = 0
        # dummy node
        previousNode = ListNode(0)
        previousNode.next = head
        
        dummyNode = previousNode
        
        while numberOfNodesSeen < nodeToRemove:
            numberOfNodesSeen += 1
            dummyNode = dummyNode.next
        
        dummyNode.next = dummyNode.next.next
            
        return previousNode.next

# ************************************************************************************************* #    
        
'''
Solution 2:
----------
'''

'''
Algorithm
---------
- Use two pointers first, and second. 
- The first pointer advances the list by n + 1 steps from the beginning, 
- while the second pointer starts from the beginning of the list. 
- Both pointers are exactly separated by n nodes apart. 
- We maintain this constant gap by advancing both pointers together until the first pointer arrives past the 
- last node. 
- The second pointer will be pointing at the nth node counting fron the last. 
- we relink the next pointer of the node referenced by the second pointer to point to the node's next next node. 

'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyNode = ListNode(0)
        dummyNode.next = head
        
        first = dummyNode
        second = dummyNode 
        
        # Advances first pointer so that the gap between first and second is n nodes apart
        i = 1
        while i <= n + 1:
            first = first.next
            i += 1
            
        # Move first to the end, maintaining the gap with second
        while first != None:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        return dummyNode.next
        