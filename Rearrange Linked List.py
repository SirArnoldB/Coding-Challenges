'''

Rearrange Linked List
---------------------
- Write a function that takes in the head of a Singly Linked List and an integer k ,
- rearranges the list in place (i.e., doesn't create a brand new list) around nodes with
- value k , and returns its new head. 
- Rearranging a Linked List around nodes with value k means moving all nodes with a
- value smaller than k before all nodes with value k and moving all nodes with a value
- greater than k after all nodes with value k .
- All moved nodes should maintain their original relative ordering if possible.
- Note that the linked list should be rearranged even if it doesn't have any nodes with value k .
- Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None /
- null if it's the tail of the list. 
- You can assume that the input Linked List will always have at least one node; in other words, the head will never be None /
- null .


'''

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrangeLinkedList(head, k):
	
	smallerListHead = smallerListTail = None
	equalListHead = equalListTail = None
	greaterListHead = greaterListTail = None
	
	node = head
	while node is not None:
		if node.value < k:
			# we are dealing with the smaller List
			smallerListHead, smallerListTail = growLinkedList(smallerListHead, smallerListTail, node)
		elif node.value > k:
			# we are dealing with the greater List
			greaterListHead, greaterListTail = growLinkedList(greaterListHead, greaterListTail, node)
		else:
			# we are dealing with the equal list
			equalListHead, equalListTail = growLinkedList(equalListHead, equalListTail, node)
		# move on to the next node:
		prevNode = node
		node = node.next
		prevNode.next = None
		
	firstHead, firstTail = connectLinkedList(smallerListHead, smallerListTail, equalListHead, equalListTail)
	finalHead, finalTail = connectLinkedList(firstHead, firstTail, greaterListHead, greaterListTail)

	return finalHead
	
def growLinkedList(head, tail, node):
	newHead = head
	newTail = node 
	
	if newHead is None:
		newHead = node 
	if tail is not None:
		tail.next = node
		
	return (newHead, newTail)
		
def connectLinkedList(headOne, tailOne, headTwo, tailTwo):
	newHead = headTwo if headOne is None else headOne
	newTail = tailOne if tailTwo is None else tailTwo
	
	if tailOne is not None:
		tailOne.next = headTwo
		
	return (newHead, newTail)