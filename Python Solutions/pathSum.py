"""
Path Sum
--------
https://leetcode.com/problems/path-sum/

- Given the root of a binary tree and an integer targetSum, 
- return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
- A leaf is a node with no children.

Examples:
*********

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
______________

Input: root = [1,2,3], targetSum = 5
Output: false
______________

Input: root = [1,2], targetSum = 0
Output: false
______________
"""
'''

Solution
********
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        sums = []
        # append te branch sums to the input list
        calculateBranchSums(root, 0, sums)
        # check if targetSum is in sums
        # if so, return True, False otherwise
        return True if targetSum in sums else False
    
# recursive function to calculate the branch sums
def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return 
    newRunningSum = runningSum + node.val
    # check if we have reached a leaf node
    # if so, append the sum to sums, and return
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    # recursive calls on the left and right child nodes
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)