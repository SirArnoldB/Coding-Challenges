''''
Palindrome Linked List
----------------------
Source: https://leetcode.com/problems/palindrome-linked-list/

- Given the head of a singly linked list, return true if it is a palindrome.

# Example 1:
    >>> Input: head = [1,2,2,1]
    >>> Output: true

# Example 2:
    >>> Input: head = [1,2]
    >>> Output: false
    
# Constraints:
    >>> The number of nodes in the list is in the range [1, 105].
    >>> 0 <= Node.val <= 9
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Solution 1
----------
# O(n) - time | O(1) - space: where n is the number of nodes in the input list 
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Algorithm
        '''
        # split the list in half and reverse the second half, 
        # Iterate through both lists in parallel to determine if they are palindromes
        
        - Find the length of the linked list 
        - Split the list in half - if odd length, keep the extra node in the first list, 
        - remove the second half list 
        - Iterate through both lists while the nodes are not Null, 
            a. if there is a mismatch, return False
        - If we made it through both lists without mismatches, return True, 
            a. if odd length, the excess node on the first list doesn't need to be checked
                since there is no comparison node
        '''
        # get the length of the list
        def getLength(node):
            # initialize length to 0
            length = 0
            
            while node:
                # update length 
                length += 1
                # advance the node
                node = node.next
            return length
        
        # get the reverse of a list 
        def getReverse(head):
            # initialize current node to pointe to the head node
            currentNode = head
            # initialize prevousNode to Null
            previousNode = None
            
            # loop through  the head
            while currentNode:
                # the next node 
                nextNode = currentNode.next
                
                # update currentnode to point to the previousNode
                currentNode.next = previousNode
                
                # update the curretNode and the previousNode
                previousNode = currentNode
                currentNode = nextNode 
            return previousNode
                
        
        # dummy node to make sure we do not modify the head node
        dummyNode = head
        
        # get the length of the list 
        nodeLength = getLength(dummyNode)
        
        # initilaize two list nodes to head 
        l1, l2 = head, head
        
        # advance l2 to get the other half of the head node
        for _ in range(nodeLength//2):
            l2 = l2.next
            
        # reverse the remaning half of l2
        reversel2 = getReverse(l2)
        
        # loop through l1, and reversel2. 
        # compare values at each node
        while l1 and reversel2:
            # mismatch found 
            if l1.val != reversel2.val:
                return False 
            # advance l1, and reversel2
            l1, reversel2 = l1.next, reversel2.next
        # no mismatch found, 
        return True

# ************************************************************* #   
        
'''
Solution 2: Using another data structure
----------
# O(n) - time | O(n) - space: wher n is the numver of nodes in the inpu head
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Algorithm
        '''
        # Sentence Summary
            # Move the LinkedList data into an array and check if the array is a palindrome

        1) Create an array
        2) Iterate through the LinkedList and add the elements to the array
        3) Check if the array is a palindrome with a two pointer solution
            a) Left and Right pointers that move towards the center
        4) If there are no mismatches, return True, else return False

        # Time Complexity: O(N)
        # Space Complexity: O(N)

        # Cons: The solution adds the complexity of moving data to another data structure
            Could we remove the need for that extra space?
        '''
        # array to store the elements of the linked list
        nodeList = []
        # for each node in head 
        while head:
            nodeList.append(head.val)
            head = head.next
        # check if array of a palindrome
        left, right = 0, len(nodeList) - 1
        while left < right:
            # if there is a mismatch, return false 
            if nodeList[left] != nodeList[right]:
                return False 
        # no mismatch found 
        return True