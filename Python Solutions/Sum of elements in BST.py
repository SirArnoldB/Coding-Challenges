'''
### Sum of All elements in a Binary Tree
'''

# Algorithm 
    # Step 1: What is the simplest possible input or the base case?
    # Step 2: Solve for left subtree
    # Step 3: Solve for right subtree
    # Step 4: Solve for current node 

# Implementation 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def treeSum(root):
    if root is None:
        return 0
    else:
        leftSum = treeSum(root.left)
        rightSum = treeSum(root.right)
        return root.val + leftSum + rightSum

