# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:59:29 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
#        if not root:
#            return []
#        ans = []
#        ans += self.postorderTraversal(root.left) #没调用这两行，就不会继续递归下去
#        ans += self.postorderTraversal(root.right)
#        ans.append(root.val)
#        return ans
        
#        current = root
#        stack = []
#        ans = []
#        while current or stack:
#            if current:
#                stack.append(current)
#                current = current.left
#            else:
#                current = stack.pop()
#                ans.append(current.val)
#                current = current.right #突然叉到右树上，把右树当做刚才的root，又来一遍这样的过程。
#        return ans
    
#        current = root
#        stack = []  # 数组模拟栈
#        ans = []
#        last_visit = root
#        while current or stack:
#            while current:
#                stack.append(current)
#                current = current.left
#            current = stack[-1]
#            if current.right is None or current.right == last_visit: #右结点是None，或者是访问过的结点
#                ans.append(current.val)
#                stack.pop()
#                last_visit = current #最后访问的结点
#                current = None
#            else:
#                current = current.right
#        return ans
        
        current = root
        stack = []
        ans = []
        last_visit = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack[-1]
            if (not current.right) or current.right == last_visit:
                ans.append(current.val)
                stack.pop()
                last_visit = current
                current = None #要回到某一步，这是后续遍历不同之处
            else:
                current = current.right #再一次，把右结点当做这一层原先的根结点
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        