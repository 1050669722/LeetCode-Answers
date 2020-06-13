# -*- coding: utf-8 -*-
"""
Created on Wed May 29 21:22:24 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
#        if root == None:
#            return 0
#        count = 1
#        if root.left != None:
#            count += 1
#        self.maxDepth(root.left.left)
        
#        if root == None:
#            return 0
##        if root.left == None and root.right == None:
##            return 1
##        else:
##            return 2
#        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root != None else 0
        
        
        