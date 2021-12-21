'''
# Source: https://leetcode.com/problems/reverse-linked-list/
# **********************************************************

# O(n) - time | O(1) - space : where n is the length of the linked list
________________________________________________________________________
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        """
        The idea is to use three pointers: next_node, current_node, and prev_node:
            >>> Initialize the three three pointers prev_node as None, current_node as head and next_node as None.
            >>> Iterate through the linked list. 
            >>> Inside the loop: 
                - Store the next_node before changing next of current_node: 
                    next_node = current_node.next
                - Then change next of current_node 
                - This reverses the linked list 
                    current_node.next = prev_node
                - Finally, move prev_node and current_node one step forward 
                    prev_node = current_node
                    current_node = next_node
        """
        
        # current is the main pointer running down the list 
        # the next pointer leads current, and the prev pointer trails current
        current_node = head 
        prev_node = None
        
        while (current_node != None):
            # the next pointer leads current
            next_node = current_node.next
            
            # reverse the pointer for the list
            # this is where the actual reversing happens
            current_node.next = prev_node
            
            # move the prev_node and current_node a step forward
            prev_node = current_node
            current_node = next_node
            
        return prev_node