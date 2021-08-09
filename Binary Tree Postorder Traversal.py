'''
# Binary Tree Postorder Traversal
---------------------------------
# Source: https://leetcode.com/problems/binary-tree-postorder-traversal/
- Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
    # Input: root = [1,null,2,3]
    # Output: [3,2,1]

# Example 2:
    # Input: root = []
    # Output: []

# Example 3:
    # Input: root = [1]
    # Output: [1]

# Example 4:
    # Input: root = [1,2]
    # Output: [2,1]

# Example 5:
    # Input: root = [1,null,2]
    # Output: [2,1]

# Constraints:
    # The number of the nodes in the tree is in the range [0, 100].
    # -100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### Method 1: # Using a flag to indicate whether the node has been visited or not.

class Solution(object):
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root, nodes = []):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited 
                    traversal.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    
        return traversal

### Method 2: Using a modified preorder (right subtree first). Then reversing the result.
class Solution(object):
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root, nodes = []):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # pre-order, right first 
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        # reverse the result 
        return traversal[::-1]



        





