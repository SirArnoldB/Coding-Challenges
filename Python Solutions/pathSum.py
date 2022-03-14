"""
Path Sum
--------
https://leetcode.com/problems/path-sum/

- Given the root of a binary tree and an integer targetSum, 
- return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
- A leaf is a node with no children.

Examples:
*********
                    5
                  /   \
                 4     8
                /     /  \
              11     13   4
             /  \           \
            7    2            1
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
______________

        1
      /   \
     2     3 
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

# ***************************************************************** # 

# Solution 2:

# ***************************************************************** # 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def hasPathSum(self, root, targetSu):
        if not root:
            return False 
        if not root.left and not root.right and root.val == targetSum:
            return True 
        
        targetSum -= root.val
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# ***************************************************************** # 

# Solution 3:

# ***************************************************************** # 

class Solution: 
    def hasPathSum(self, root, targetSum):
        if not root:
            return False 
        
        stack = [(root, root.val)]
        
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right and val == targetSum:
                return True
            if curr.right:
                stack.append((curr.right, val + curr.right.val))
            if curr.left:
                stack.append((curr.left, val + curr.left.val))
        return False 
    