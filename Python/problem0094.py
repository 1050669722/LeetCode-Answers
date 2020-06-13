# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:26:24 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
#        if not root:
#            return []
#        ans = []
#        ans += self.inorderTraversal(root.left) #没调用这两行，就不会继续递归下去
#        ans.append(root.val)
#        ans += self.inorderTraversal(root.right)
#        return ans
        
        current = root
        stack = []
        ans = []
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                ans.append(current.val)
                current = current.right #突然叉到右树上，把右树当做刚才的root，又来一遍这样的过程。
        return ans
        
        
        