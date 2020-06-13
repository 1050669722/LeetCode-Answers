# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:50:07 2019

@author: Administrator
"""

class Solution:
    def heightChecker(self, heights: list) -> int:
        temp = self.merge_sort(heights)
        res = 0
        for k in range(len(heights)):
            if temp[k] != heights[k]:
                res += 1
        return res
        
    def merge(self, left, right):
        p, q =0, 0
        ans = []
        while p<len(left) and q<len(right):
            if left[p]<=right[q]:
                ans.append(left[p])
                p += 1
            else:
                ans.append(right[q])
                q += 1
        ans += left[p:]
        ans += right[q:]
        return ans
        
    def merge_sort(self, List):
        if len(List)<=1:
            return List
        num = len(List) // 2
        left = self.merge_sort(List[:num])
        right = self.merge_sort(List[num:])
        return self.merge(left, right)
        
        
solu = Solution()
heights = [1,1,4,2,1,3]
print(solu.heightChecker(heights))