# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        import sys
        ans = sys.maxsize
        pre = -1

        def worker(root):
            nonlocal ans, pre

            if not root:
                return None

            worker(root.left)

            if pre != -1: #如果pre在外部被定义成-sys.maxsize的话，这里就不用判断了
                ans = min(ans, root.val - pre)
            pre = root.val

            worker(root.right)

        worker(root)
        
        return ans

            


