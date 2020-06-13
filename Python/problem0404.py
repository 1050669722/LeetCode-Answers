# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:13:24 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return root.val
        if root.left != None and root.right == None:
            return self.sumOfLeftLeaves(root.left)
        if root.left == None and root.right != None:
            return self.sumOfLeftLeaves(root.right)#0#
        else:
            return self.sumOfLeftLeaves(root.left)# + self.sumOfLeftLeaves(root.right)
        
#        if root.left.left == None and root.left.right == None:
#            root.left.val
#        if root.right.left == None and root.right.right == None:
#            root.right.val
        
        
        
        
        
        