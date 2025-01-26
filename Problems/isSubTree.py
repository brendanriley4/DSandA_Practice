from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 and root2:
                return False
            if not root2 and root1:
                return False
            if root1.val != root2.val:
                return False
            return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)

        def hasSubtree(root):
            if not root:
                return False
            if sameTree(root, subRoot):
                return True

            return hasSubtree(root.left) or hasSubtree(root.right)

        return hasSubtree(root)

    # Time Complexity: O(m * n)
    # Space complexity: O()