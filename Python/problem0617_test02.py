# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        ans = TreeNode(0)
        if t1 and not t2:
            ans = t1
        elif not t1 and t2:
            ans = t2
        else:
            ans.val = t1.val + t2.val
            ans.left = self.mergeTrees(t1.left, t2.left)
            ans.right = self.mergeTrees(t1.right, t2.right)
        return ans