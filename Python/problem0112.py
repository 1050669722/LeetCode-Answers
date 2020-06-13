# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:52:20 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#        if root == None:
#            return
##        temp = 0
##        temp += root.val
#        left_c = self.hasPathSum(root.left, sum)
#        right_c = self.hasPathSum(root.right, sum)
##        temp += self.hasPathSum(root.left)
##        temp += self.hasPathSum(root.right)
#        return left_c or right_c
        
        if root == None:
            return False
        elif root.left == None and root.right == None:
            return root.val == sum
        elif root.left != None and root.right == None:
            return self.hasPathSum(root.left, sum-root.val)
        elif root.left == None and root.right != None:
            return self.hasPathSum(root.right, sum-root.val)
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
            
        
        
        
        
        
        
        
        
        