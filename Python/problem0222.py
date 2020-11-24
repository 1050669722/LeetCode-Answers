# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def preorderTraversal(root):
            if not root:
                return []
            ans = []
            ans.append(root.val)
            ans += preorderTraversal(root.left)
            ans += preorderTraversal(root.right)
            return ans
        return len(preorderTraversal(root))
