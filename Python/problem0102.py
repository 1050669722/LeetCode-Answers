from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level): # node比root更具一般性
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
            return None

        helper(root, 0)
        return levels