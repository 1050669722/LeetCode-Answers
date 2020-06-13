# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:25:57 2019

@author: Administrator
"""

class Solution:
    def sortedSquares(self, A: list) -> list:
#        B = []
#        for k in A:
#            B.append(k**2)
##        print(B)
##        C = self.merge_sort(B)
##        C = sorted(B)
#        B = self.MergeSort_fun2(B)
#        return B#C#
        
        a = []
        mark = 0
        temp = 0
        for k in A:
            if mark == 0 and k>=0:
                mark += 1
                temp = A.index(k)
                a.reverse()
            a.append(k**2)
#        a = self.MergeSort_fun1(a[:temp], a[temp:])
#        print(a)
        a = self.merge(a[:temp], a[temp:])
        return a
        
    def merge(self, left, right):
        ans = []
        p, q = 0, 0
        while p<len(left) and q<len(right):
            if left[p] <= right[q]:
                ans.append(left[p])
                p += 1
            else:
                ans.append(right[q])
                q += 1
        ans += left[p:]
        ans += right[q:]
        return ans
        
    def merge_sort(self, List):
#        print(List)
        if len(List)<=1:
            return List
        num = len(List) // 2
        left = self.merge_sort(List[:num])
        right = self.merge_sort(List[num:])
        print(self.merge(left, right))
        return self.merge(left, right)
    
    def MergeSort_fun1(self, left, right):
        result = []
        i, j = 0, 0
        while i<len(left) and j<len(right): #注意，左右穿插排列大小 #这里的i, j像是指针
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:] #是拼接不能用.append()
        result += right[j:]
        return result
        
    def MergeSort_fun2(self, List):
        if len(List) <= 1: #这一判断必须得有，否则一直递归下去，因为底层总会到只含有一个元素的列表
            return List
        num = len(List) // 2
        left = self.MergeSort_fun2(List[:num])
        right = self.MergeSort_fun2(List[num:])
#        print(self.MergeSort_fun1(left, right))
        return self.MergeSort_fun1(left, right)
        
        
        
        
solu = Solution()
A = [-4,-1,0,3,10]
#A = [-7,-3,2,3,11]
print(solu.sortedSquares(A))
#print(solu.merge_sort(A))
#print(solu.MergeSort_fun2(A))