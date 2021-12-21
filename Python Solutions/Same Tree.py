'''
# Same Tree
-----------
# Source: https://leetcode.com/problems/same-tree/
- Given the roots of two binary trees p and q, write a function to check if they are the same or not.
- Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
#     Input: p = [1,2,3], q = [1,2,3]
#     Output: true

# Example 2:
    # Input: p = [1,2], q = [1,null,2]
    # Output: false

# Example 3:
    # Input: p = [1,2,1], q = [1,1,2]
    # Output: false

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 1. Understand:
            # structure and nodes of trees must be the same 
            # edge case: one tree is empty, return false; both trees are empty - false 
        # 2. Match 
            # DFS Pre-order traversal for each tree: 
                # Root -> left subtree -> right subtree 
        # 3. Plan:
            # compare values of root nodes of p and q: return False if not the same
            # call is same on p.left and q.left
            # call is same on p.right and q.right 
            # O(n) - time | O(logn) - space (best case of completely balanced tree)
            # O(n) - space (for completely unbalanced tree)
        # 4. Implement 
        
        def same(p, q):
            
            if p is None or q is None:
                # p and q are both None
                if p is None and q is None: 
                    return True
                # one of p and q is None
                else: 
                    return False 
            # nodes of p and q are different
            if p.val != q.val:
                return False 
            # recursive call
            return same(p.left, q.left) and same(p.right, q.right)
        
        return same(p, q)