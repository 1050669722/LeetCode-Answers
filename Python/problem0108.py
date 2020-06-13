# -*- coding: utf-8 -*-
"""
Created on Wed May 29 21:50:22 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if nums == []:
            return None
        num = len(nums) // 2
        T = TreeNode(nums[num])
        T.left = self.sortedArrayToBST(nums[:num])
        T.right = self.sortedArrayToBST(nums[num+1:])
        return T