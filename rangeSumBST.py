"""
Range Sum of BST 
----------------
https://leetcode.com/problems/range-sum-of-bst/

- Given the root node of a binary search tree and two integers low, and high, 
- return the sum of values of all nodes with a value in the inclusive range [low, high]

Examples
-------

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

*****
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # sum of values of the nodes in the given range
        sum_val = 0
        # if root is None, return 0
        if not root:
            return 0
        # check if the value of the root is within the given range
        # if so, add it to the sum of values of all nodes, sum_val
        elif root.val >=low  and root.val <= high:
            sum_val += root.val
        # recursive calls on the left and right nodes of the root node
        return sum_val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)