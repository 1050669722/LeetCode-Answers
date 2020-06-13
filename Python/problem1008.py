from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # if not preorder:
        #     return None
        # root = TreeNode(preorder[0])
        # for k in range(1, len(preorder)):
        #     if preorder[k] < root.val:
        #         root.left = self.bstFromPreorder(preorder[k:])
        #     else:
        #         root.right = self.bstFromPreorder(preorder[k:])

        if not preorder:
            return None
        val = preorder[0]
        root = TreeNode(val)
        nums1, nums2 = [], []
        for num in preorder[1:]:
            if num < val:
                nums1.append(num)
            else:
                nums2.append(num)
        root.left = self.bstFromPreorder(nums1)
        root.right = self.bstFromPreorder(nums2)
        return root