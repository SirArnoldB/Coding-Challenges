# Source: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Binary Tree Zigzag Level Order Traversal

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root)]:
        if not root: return []
        
        levels = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            size = len(queue)
            new_level = deque()
            
            for _ in range(size):
                node = queue.popleft()
                if left_to_right:
                    new_level.append(node.val)
                else:
                    new_level.appendleft(node.val)
                
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
                        
            levels.append(new_level)
            left_to_right = not left_to_right
        
        return levels