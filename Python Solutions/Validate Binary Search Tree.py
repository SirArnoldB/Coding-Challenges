# Source: https://leetcode.com/problems/validate-binary-search-tree/

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, min_val, max_val):

        # Base case
        # Also serves to validate an empty subtree as a BST.
        if node is None:
            return True 

        # Check conditions that satisfy BST regulations  
        if node.val <= min_val or node.val >= max_val:
            return False      
        
        # Ensures to return True only if BST regulations are met at every node in the tree.
        return self.helper(node.left, min_val, node.val) and self.helper(node.right, node.val, max_val)    


    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Just calls the helper function to on returning the output.
        return self.helper(root, float("-inf"), float("inf"))





