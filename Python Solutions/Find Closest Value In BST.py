"""
Recursive Approach
******************
"""
# Average: O(log n) - time | O(log n) - space
# Worst Case: O(n) - time | O(n) - space 
# where n is the length of the tree
def findClosestValueInBst(tree, target):
	return findClosestValue(tree, target, float('inf'))

def findClosestValue(tree, target, closest):
	# Base case, when we have reaced the emd of the tree
	if tree is None:
		return closest
	# check for the smallest absolute difference
	# then update the closest value
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	# take advantage of the BST property
	# to decide whether to proceed with the left or right side of the tree
	if tree.value > target:
		# check the left side of the tree
		return findClosestValue(tree.left, target, closest)
	elif tree.value < target:
		# check the right side of the tree
		return findClosestValue(tree.right, target, closest)
	else:
		# found the closest value
		return closest
	
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ************************************************************* #

"""
Iterative Approach
******************
"""
# Average: O(log n) - time | O(1) - space
# Worst Case: O(n) - time | O(n) - space 
# where n is the length of the tree
def findClosestValueInBst(tree, target):
	closest_value = float('inf')
	current_node = tree
	while current_node is not None:
		# check for the smallest absolute difference
		# then update the closest value
		if abs(target - closest_value) > abs(target - current_node.value):
			closest_value = current_node.value
		# take advantage of the BST property
		# to decide whether to proceed with the left or right side of the tree
		if current_node.value > target:
			# check the left side of the tree
			current_node = current_node.left
		elif current_node.value < target:
			# check the right side of the tree
			current_node = current_node.right
		else:
			# found the closest value
			break
	return closest_value

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None