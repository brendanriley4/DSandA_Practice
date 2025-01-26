from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bfs(node, node_min, node_max):
            if not node:
                return True
            if node.val <= node_min or node.val >= node_max:
                return False
            return bfs(node.left, node_min, node.val) and bfs(node.right, node.val, node_max)
        return bfs(root, float("-inf"), float("inf"))

        # CAN BE MADE BETTER THAN THIS
        # temp = [float('-inf')]
        # ans= [True]
        #
        # def dfs(node):
        #     if not node or ans[0] == False:
        #         return
        #     dfs(node.left)
        #     if node.val < temp[0]:
        #         ans[0] = False
        #         return
        #     temp[0] = node.val
        #     dfs(root.right)
        #
        # dfs(root)
        # return ans[0]