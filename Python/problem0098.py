# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def inorder(root):
            if not root:
                return []

            ans = []
            ans += inorder(root.left)
            ans.append(root.val)
            ans += inorder(root.right)

            return ans
        
        ans = inorder(root)
        for k in range(1, len(ans)):
            if not (ans[k]>ans[k-1]):
                return False
        return True
