# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:26:11 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root.val == None:
            return 0
        count = 0
        if L<=root.val<=R:
            count += root.val
        if root.left != None:
            count += self.rangeSumBST(root.left, L, R)
        if root.right != None:
            count += self.rangeSumBST(root.right, L, R)
        return count
        
    
solu = Solution()

root, L, R = [10,5,15,3,7,None,18], 7, 15
a = TreeNode(10)
a.left = TreeNode(5)
a.right = TreeNode(15)
a.left.left = TreeNode(3)
a.left.right = TreeNode(7)
#a.right.left = TreeNode(None)
a.right.right = TreeNode(18)
print(solu.rangeSumBST(a, L, R))

root, L, R = [10,5,15,3,7,13,18,1,None,6], 6, 10
b = TreeNode(10)
b.left = TreeNode(5)
b.right = TreeNode(15)
a.left.left = TreeNode(3)
a.left.right = TreeNode(7)
a.right.left = TreeNode(13)
a.right.right = TreeNode(18)
a.left.left.left = TreeNode(1)
a.left.right.left = TreeNode(6)
print(solu.rangeSumBST(b, L, R))






