# Source: https://leetcode.com/problems/invert-binary-tree/

# Invert Binary Tree

# Given the root of a binary tree, invert the tree, and return its root.


# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node):
        if node:
            node.left, node.right = self.dfs(node.right), self.dfs(node.left)
        return node
    
    def invertTree(self, root):
        return self.dfs(root)

# O(n) - time | O(n) - space
def invertBinaryTree(tree):
    queue = [tree]
    while queue:
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left