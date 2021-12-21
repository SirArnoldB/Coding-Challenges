# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(m, n)) - time | O(max(m, n)) - space 
def sumOfLinkedLists(linkedListOne, linkedListTwo):
	# dummy node pointer to the head of our new list
	sumListNode = LinkedList(0)
	# represents the current npde
	sumTailNode = sumListNode 
	carry = 0
	
	nodeOne = linkedListOne
	nodeTwo = linkedListTwo
	while nodeOne is not None or nodeTwo is not None or carry != 0:
		# get the two values 
		valueOne = nodeOne.value if nodeOne is not None else 0
		valueTwo = nodeTwo.value if nodeTwo is not None else 0
		# get the sum of the values and the carry 
		sumOfValues = valueOne + valueTwo + carry
		
		newValue = sumOfValues % 10
		newNode = LinkedList(newValue)
		sumTailNode.next = newNode 
		sumTailNode = newNode
		
		# update the carry 
		carry = sumOfValues // 10
		nodeOne = nodeOne.next if nodeOne is not None else None
		nodeTwo = nodeTwo.next if nodeTwo is not None else None
		
	return sumListNode.next 
		