"""

Insert a node to its correct sorted position in a sorted linked list

- Given a sorted list in increasing order and a single node, insert the node into the
- list’s correct sorted position. 
- The function should take an existing node and rearranges pointers to insert it into the list.

# Solutions
-----------
"""

# 1. Naive Approach
#######################


# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Helper function to print a given linked list
def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" —> ")
        ptr = ptr.next
    print("None")


# Function to insert a given node at its correct sorted position into
# a given list sorted in increasing order
def sortedInsert(head, newNode):
    # special case for the head end
    if head is None or head.data >= newNode.data:
        newNode.next = head
        head = newNode
        return head

    # Locate the node before the poof insertion
    current = head
    while current.next and current.next.data < newNode.data:
        current = current.next

    newNode.next = current.next
    current.next = newNode

    return head


if __name__ == "__main__":
    # input keys
    keys = [2, 4, 6, 8]

    # points to the head node of the linked list
    head = None

    # construct a linked list
    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    head = sortedInsert(head, Node(5))
    head = sortedInsert(head, Node(9))
    head = sortedInsert(head, Node(1))
    head = sortedInsert(head, Node(20))
    head = sortedInsert(head, Node(-20))

    # print linked list
    printList(head)
