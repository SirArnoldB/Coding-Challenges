'''
# Reverse Linked List
---------------------
Source: https://www.algoexpert.io/questions/Reverse%20Linked%20List

- Write a function that takes in the head of a Singly Linked List, 
- reverses the list in place (i.e., doesn't create a brand new list), and returns its new head.
- Each LinkedList node has an integer value as well as a next node pointing to the next node in the list 
- or to None / null if it's the tail of the list.
- You can assume that the input Linked List will always have at least one node; in other words,
- the head will never be None / null .

# Sample Input
    >>> head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0
# Sample Output
    >>> 5 -> 4 -> 3 -> 2 -> 1 -> 0 // the new head node with value 5
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) - time | O(1)- space: where n is the number of nodes in the Linked List
def reverseLinkedList(head):
    # Algorithm
	'''
	# The idea is to use three pointers: newCurrentNode, currentNode, and previousNode:
		>>> Initialize the three three pointers previousNode as None, currentNode as head and newCurrentNode as None.
		>>> Iterate through the linked list. 
		>>> Inside the loop: 
			- Store the next_node before changing next of current_node: 
				newCurrentNode = currentNode.next
			- Then change next of currentNode 
			- This reverses the linked list 
				currentNode.next = previousNode
			- Finally, move previousNode and currentNode one step forward 
				previousNode = currentNode
				currentNode = nextNode
	'''
	# keeps track of the current head
	currentNode = head
	# keeps track of the node behind the current node 
	previousNode = None
	
	while currentNode != None:
		# get the new current Node 
		newCurrentNode = currentNode.next
		# make the pointer for the currentNode to point to 
		# the previousNode; reverses the list
		currentNode.next = previousNode
		# advance the previousNode; and currentNode
		previousNode = currentNode 
		currentNode = newCurrentNode
	return previousNode