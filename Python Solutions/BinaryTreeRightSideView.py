# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

from typing import Optional, List
from collections import deque
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Return an empty list if the root is None
        if not root:
            return []

        # Initialize a list to store the values of the rightmost nodes
        right_most_nodes = []
        # Initialize a queue with the root node for level order traversal
        queue = deque([root])

        # Loop until the queue is empty
        while queue:
            # Get the current level size
            size = len(queue)

            # Process all nodes of the current level
            for idx in range(size):
                # Pop a node from the front of the queue
                node = queue.popleft()
                # If it's the last node of the current level, add its value to the list
                if idx == size - 1:
                    right_most_nodes.append(node.val)

                # Add the node's left and right children to the queue
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

        # Return the list of rightmost nodes' values
        return right_most_nodes


class TestRightSideView(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_right_side_view_1(self) -> None:
        root = TreeNode(
            1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4))
        )
        expected = [1, 3, 4]
        self.assertEqual(self.sol.rightSideView(root), expected)

    def test_right_side_view_2(self) -> None:
        root = TreeNode(1, None, TreeNode(3))
        expected = [1, 3]
        self.assertEqual(self.sol.rightSideView(root), expected)

    def test_right_side_view_3(self) -> None:
        root = None
        expected: List[int] = []
        self.assertEqual(self.sol.rightSideView(root), expected)


if __name__ == "__main__":
    unittest.main()
