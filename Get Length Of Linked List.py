'''
# Get Length of Linked List
---------------------------
- Given a singly linked list, return its length

# Example:
    >>> Input:  1->2->3->4
    >>> Output: 4
'''
# Algorithm
'''
# 1-2 Sentence Summary
# Iterate through the LinkedList until we reach a null node and keep a counter
    variable as we go.

1) Create a counter variable
2) Iterate through the LinkedList while the head is not Null
    a) Increment the counter variable and
        move the current node pointer to the next node.
3) Since we have reached the end now, return the counter variable

# Time Complexity: O(N)
# Space Complexity: O(1)
'''
def listLength(head):
    # counter variable 
    length = 0
    while head:
        # increment the counter 
        length += 1
        # advance the head
        head = head.next
    return length