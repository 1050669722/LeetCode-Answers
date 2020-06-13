# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:13:25 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#class Solution:
#    def longestUnivaluePath(self, root: TreeNode) -> int:
##        count1 = 0
##        count2 = 0
##        if root.val == root.left.val:
##            current = root
##            count1 += 1
##            root = root.left
##            count1 += self.longestUnivaluePath(root)
##            root = current
##        if root.val == root.right.val:
##            current = root
##            count2 += 1
##            root = root.right
##            count2 += self.longestUnivaluePath(root)
##            root = current
##        return max(count1, count2)
#        
#        ans = []
#        
#        if not root:
#            ans.append(0)
#            return max(ans)
#        
#        count1 = 0
#        count2 = 0
#        
#        if not root.left:
#            count1 = 0
#        elif root.val == root.left.val:
#            count1 += 1
#            ans += self.longestUnivaluePath(root.left)
#        else:
#            self.longestUnivaluePath(root.left)
#        
#        if not root.right:
#            count2 = 0
#        elif root.val == root.right.val:
#            count2 += 1
#            ans += self.longestUnivaluePath(root.right)
#        else:
#            self.longestUnivaluePath(root.left)
#        
#        ans.append(max(count1, count2))
#        
#        return max(ans)
            

class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans

#作者：LeetCode
#链接：https://leetcode-cn.com/problems/two-sum/solution/zui-chang-tong-zhi-lu-jing-by-leetcode/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
            
        
        
        