from typing import Optional

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

# Recursive pre order traversal (DFS) Time: O(n), Space: O(n)
# Process Node, Node.left, Node.right
def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)

# Recursive in order traversal (DFS) Time: O(n), Space: O(n)
# Process Node.left, Node, Node.right
def in_order(node):
    if not node:
        return
    pre_order(node.left)
    print(node)
    pre_order(node.right)

# Recursive post order traversal (DFS) Time: O(n), Space: O(n)
# Process Node.left, Node.right, Node
def post_order(node):
    if not node:
        return
    pre_order(node.left)
    pre_order(node.right)
    print(node)

# Iterative pre order traversal (DFS) Time: O(n), Space: O(n)
def pre_order_iterative(node):
    stk = [node]
    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.right)

# Level order traversal (BFS) Time: O(n), Space: O(n)
from collections import deque

def level_order(node):
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

# Check if value exists (DFS) Time: O(n), Space: O(n)
def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    return search(node.left, target) or search(node.right, target)

# Search a binary search tree (BST) Space: O(logn), Time: O(logn)
def search_bst(node, target):
    if not node:
        return False
    if node.vall == target:
        return True
    if target < node.val: return search_bst(node.left, target)
    else: return search_bst(node.right, target)