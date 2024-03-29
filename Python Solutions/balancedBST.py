# Source: https://leetcode.com/problems/balanced-binary-tree/

# Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true


# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root) -> bool:
        self.balanced = True

        def dfs(root):
            if not root:
                return 0

            left_total = dfs(root.left)
            right_total = dfs(root.right)

            if abs(left_total - right_total) > 1:
                self.balanced = False

            return max(left_total, right_total) + 1

        dfs(root)

        return self.balanced
