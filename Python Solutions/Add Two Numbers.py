'''
Add Two Numbers
---------------
Source: https://leetcode.com/problems/add-two-numbers/

- You are given two non-empty linked lists representing two non-negative integers. 
- The digits are stored in reverse order, and each of their nodes contains a single digit. 
- Add the two numbers and return the sum as a linked list.

- You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
    >>> Input: l1 = [2,4,3], l2 = [5,6,4]
    >>> Output: [7,0,8]
    >>> Explanation: 342 + 465 = 807.

# Example 2:
    >>> Input: l1 = [0], l2 = [0]
    >>> Output: [0]

# Example 3:
    >>> Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    >>> Output: [8,9,9,9,0,0,0,1]

# Constraints:
    >>> The number of nodes in each linked list is in the range [1, 100].
    >>> 0 <= Node.val <= 9
    >>> It is guaranteed that the list represents a number that does not have leading zeros.
'''

'''
Solution 1: Efficient
---------------------
# O(max(m, n)) - time | O(max(m, n)) - space: wherem and n are the lengths 
# of the input numbers
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if one of the nodes is empty
        if not l1 or not l2: return l1 if not l2 else l2
        
        # dummy node for the sum
        sumNode = ListNode(0)
        sumNodeTail = sumNode
        
        # the number that is carried over due to overflow after adding two numbers 
        carry = 0
        
        while l1 != None or l2 != None or carry:
            # get the values at the current nodes
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            
            # get the overall sum of the nodes, and the carry value 
            sumTotal = value1 + value2 + carry
            
            # get the remainder, 
            remainder = sumTotal % 10
            # update the carry
            carry = sumTotal // 10
            
            # create a new Node with the remainder as the value, and 
            # add it to the tail, sumNodeTail
            sumNodeTail.next = ListNode(remainder)
            sumNodeTail = sumNodeTail.next
            
            # update l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return sumNode.next

# ************************************************************************** #

'''
Solution 2: Brute Force Method
--------
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #strings to store the numbers we will be adding
        num1 = ""
        num2 = ""
        #if one of the ListNodes is none, return the other
        if not l1 or not l2: return l2 if not l1 else l1
        
        #use the while loop to get the numbers
        while l1 or l2:
            if l1:
                num1 += str(l1.val)
                l1 = l1.next
            if l2:
                num2 += str(l2.val) 
                l2 = l2.next
        #then find the sum of the reversed numbers, and convert it into a string     
        sum_nums = str(int(num1[::-1]) + int(num2[::-1]))
        
        #Dummy node which we will return as the sum 
        sum_node = ListNode(0) 
        tail_of_sum = sum_node
        
        #Convert each element in sum_nums to a node, and add it to the dummy listnode
        #we reverse the sum_nums string because we are supposed to return the listnode(sum) in reverse
        for ele in sum_nums[::-1]:
            tail_of_sum.next = ListNode(ele)
            tail_of_sum = tail_of_sum.next
            
        return sum_node.next
    
