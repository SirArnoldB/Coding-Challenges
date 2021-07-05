'''
# Intersection of Two Linked Lists
----------------------------------
Source: https://leetcode.com/problems/intersection-of-two-linked-lists/
- Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
- If the two linked lists have no intersection at all, return null.

- It is guaranteed that there are no cycles anywhere in the entire linked structure.
- Note that the linked lists must retain their original structure after the function returns.

# Example 1:
    >>> Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    >>> Output: Intersected at '8'
    >>> Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
    >>> From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
        There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
# Example 2:
    >>> Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    >>> Output: Intersected at '2'
    >>> Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
    >>> From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. 
        There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
# Example 3:
    >>> Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    >>> Output: No intersection
    >>> Explanation: From the head of A, it reads as [2,6,4]. 
        From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
    >>> Explanation: The two lists do not intersect, so return null.

# Constraints:
    # The number of nodes of listA is in the m.
    # The number of nodes of listB is in the n.
    # 0 <= m, n <= 3 * 104
    # 1 <= Node.val <= 105
    # 0 <= skipA <= m
    # 0 <= skipB <= n
    # intersectVal is 0 if listA and listB do not intersect.
    # intersectVal == listA[skipA + 1] == listB[skipB + 1] if listA and listB intersect.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Solution 1:
-----------
# O(n) - time | O(1) - space
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """   
        # given a node and length
        # fastforward it length times
        def fastForward(node, diffLen):
            while diffLen > 0:
                node = node.next
                diffLen -= 1
            return node

        # given a node, get the end node and the length of the list
        def getEnd(node):
            length = 1
            while node.next:
                node = node.next
                length += 1
            return node, length 
        
        # if one or both lists are empty
        if not headA or not headB:
            return None
        
        # get the length and end node of each head
        endA, lenA = getEnd(headA)
        endB, lenB = getEnd(headB)
        
        # edge case: if the end nodes are different, no intersection
        if endA != endB:
            return None
        
        # check which head is the longest
        if lenA > lenB:
            # the difference between the length of the two heads
            diffLen = lenA - lenB
            # fastfoward headA to make the same length as headB
            headA = fastForward(headA, diffLen)
            # headB = headB
        else:
            # the difference between the length of the two heads
            diffLen = lenB - lenA
            # fastfoward headB to make the same length as headB
            headB = fastForward(headB, diffLen)
            # headA = headA
        
        # get the intersection node ]
        while headA != headB:
            headA = headA.next
            headB = headB.next
        # since the nodes will be the same
        return headA
    
'''
Solution 2: Two Pointers
-----------
# O(n + m) - time | O(m) - space; where m and n are the number of 
# nodes in listA and listB
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """ 
        # keeps track of reference of each node in B
        nodes_in_B = set()
        # traverse node B to get each node reference
        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next
        # traverse each node in list A
        # check whether or not the set contains this node
        while headA is not None:
            # if we find the node pointed to by headA,
            # in our set containing nodes of B, then return the node
            if headA in nodes_in_B:
                return headA
            headA = headA.next

        return None
    
'''
Solution 3:
----------
# O(n + m) - time | O(1) - space; where m and n are the number of 
# nodes in listA and listB
# In the worst case, each list is traversed twice giving 2⋅M+2⋅N, 
# which is equivalent to O(N + M)O(N+M). 
# This is because the pointers firstly go down each list, 
# so that they can be "lined up" and then in the second iteration, 
# the intersection node is searched for.
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """ 
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
        # Note: In the case lists do not intersect, the pointers for A and B
        # will still line up in the 2nd iteration, just that here won't be
        # a common node down the list and both will reach their respective ends
        # at the same time. So pA will be NULL in that case.