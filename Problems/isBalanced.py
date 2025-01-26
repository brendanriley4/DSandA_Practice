from typing import Optional
from unittest.mock import right


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        balanced = [True]

        def height(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left_height = height(root.left)
            if balanced[0] is False:
                return 0

            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0

            return 1 + max(left_height, right_height)

        height(root)
        return balanced[0]