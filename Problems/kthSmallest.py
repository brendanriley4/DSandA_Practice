from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        visited = [0]
        ans = [0]

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            visited[0] += 1
            if visited[0] == k:
                ans[0] = node.val
                return
            dfs(node.right)

        dfs(root)
        return ans[0]

