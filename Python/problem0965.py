# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:12:06 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
#        if root == None:
#            return True
#        if root.left == None and root.right == None:
#            return True
#        if root.left == None and root.right != None:
#            if root.val == root.left.val:
#                return True
#        if root.left != None and root.right == None:
#            if root.val == root.right.val:
#                return True
#        if root.val == root.left.val and root.val == root.right.val:
#            return True
        left_correct = (not root.left) or (root.left.val == root.val and self.isUnivalTree(root.left))      
        right_correct = (not root.right) or (root.right.val == root.val and self.isUnivalTree(root.right))
        return left_correct and right_correct