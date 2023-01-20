# Source: https://leetcode.com/problems/binary-tree-paths/

# Binary Tree Paths

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.


# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(self, root):
    if not root.left and not root.right:
        return [str(root.val)]
    
    def dfs(node, path, paths):
        if not node.left and not node.right:
            # process the current path
            paths.append('->'.join(path) + '->' + str(node.val))
            return
        path.append(str(node.val))
        if node.left:
            dfs(node.left, path, paths)
        if node.right:
            dfs(node.right, path, paths)
        # remove elements from the stack
        path.pop()
    
    # keeps track of all the paths in the tree
    paths = []
    
    if root: dfs(root, [], paths)
        
    return paths