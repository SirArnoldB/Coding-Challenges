"""
Question:
*********
Source: https://www.algoexpert.io/questions/Branch%20Sums
- Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from
leftmost branch sum to rightmost branch sum. 
- A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a
path of nodes in a tree that starts at the root node and ends at any leaf node. 
- Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null.

"""

'''
Solution
********
'''
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) - time | O(n) - space : where n is the number of nodes in the Binary Tree
def branchSums(root):
	"""
	- Main idea is that we will be calling a recursive function on each node 
	- starting with the root node that calculates the branched sums for the tree 
	- rooted at that node.
	- We also keep track of a running sum, which gives us the sum that we have obtained by
	- calculating/adding values from nodes above us at every recursive call in this whole algorithm. 
	- O(n) - time, since we are visiting every node in the tree
	- O(n) - space, 
		- 
	"""
	sums = []
	# append branch sums to the input list
	calculateBranchSums(root, 0, sums)
	return sums
	
def calculateBranchSums(node, runningSum, sums):
	if node is None:
		return 
	newRunningSum = runningSum + node.value
	# check whether or not we are at a leaf node
	# if so, append the newRunningSum to the sums list
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
		return 
	# if we are not at a leaf node, 
	# we keep calculating the branch sums
	# by recursivley calling calculateBranchSums
	calculateBranchSums(node.left, newRunningSum, sums)
	calculateBranchSums(node.right, newRunningSum, sums)