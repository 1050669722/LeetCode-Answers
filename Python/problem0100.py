# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:02:09 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True
        if p!=None and q==None:
            return False
        if p==None and q!=None:
            return False
        if p.val == q.val:
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            else:
                return False
        return False
            
            