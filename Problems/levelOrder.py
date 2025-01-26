# Level order traversal (BFS) Time: O(n), Space: O(n)
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q = deque()
        q.append(root)
        ans = []
        while q:
            level = []
            n  = len(q)
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(level)
        return ans