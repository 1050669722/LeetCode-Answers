# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:14:24 2019

@author: Administrator
"""

class Solution:
    def majorityElement(self, nums: list) -> list:
#        x=0
#        y=0
#        cx=0
#        cy=0
#        for num in nums:
#            if (cx==0 or num == x) and num != y:
#                cx += 1
#                x=num
#            elif cy == 0 or num == y:
#                cy +=1
#                y = num
#            else:
#                cx -=1
#                cy -=1
#        cx = 0
#        cy = 0
#        for num in nums:
#            if num == x:
#                cx +=1
#            elif num ==y:
#                cy +=1
#        length = len(nums)
#        l=[]
#        if cx>int(length/3):
#            l.append(x)
#        if cy>int(length/3):
#            l.append(y)
#        return l
        
#        a, b, ca, cb, ans = None, None, 0, 0, []
#        for n in nums:
#            if   n  == a: ca += 1
#            elif n  == b: cb += 1
#            elif ca == 0: a, ca = n, 1 #初始化
#            elif cb == 0: b, cb = n, 1 #初始化
#            else: ca, cb = ca - 1, cb - 1
#        
#        ca, cb = 0, 0
#        for n in nums:
#            if   n == a: ca += 1
#            elif n == b: cb += 1
#        if ca > len(nums)//3: #最多和次最多的数是不是都多于n/3的向下取整
#            ans.append(a)
#        if cb > len(nums)//3:
#            ans.append(b)
#        return ans
        
        a, b, ca, cb, ans = None, None, 0, 0, []
        for k in nums:
            if k == a:
                ca += 1
            elif k == b:
                cb += 1
            elif ca == 0:
                a, ca = k, 1
            elif cb == 0:
                b, cb = k, 1
            else:
                ca -= 1
                cb -= 1
        ca, cb = 0, 0
        for k in nums:
            if k == a:
                ca += 1
            if k == b:
                cb += 1
        if ca > len(nums) // 3:
            ans.append(a)
        if cb > len(nums) // 3:
            ans.append(b)
        return ans

solu = Solution()
#nums = [3,2,3]
nums = [1,1,1,3,3,2,2,2]
print(solu.majorityElement(nums))
        








