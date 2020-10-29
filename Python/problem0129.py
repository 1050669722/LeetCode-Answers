# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 深度优先搜索
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def worker(curroot, pretotal):
            if not curroot:
                return 0
            total = pretotal * 10 + curroot.val
            if not (curroot.left or curroot.right):
                return total
            else:
                return worker(curroot.left, total) + worker(curroot.right, total)
        
        return worker(root, 0)
