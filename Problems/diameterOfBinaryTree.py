from typing import Optional
from unittest.mock import right


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]

        def height(root):
            if root is None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            diameter = left_height + right_height

            max_diameter[0] = max(max_diameter[0], diameter)
            return 1 + max(left_height, right_height)

        height(root)
        return max_diameter[0]

