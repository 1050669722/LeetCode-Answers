# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:22:53 2019

@author: Administrator
"""

class Solution:
    def longestArithSeqLength(self, A: list) -> int:
#        ans = min(2, len(A))
#        for p in range(len(A)):
#            for q in range(p+2, len(A)):

#        result={}
#        maxv=2
#        for i in range(1,len(A)):
#            for j in range(i):
#                if (A[j]-A[i],j) not in result:
#                    result[(A[j]-A[i],i)]=2
#                else:
#                    result[(A[j]-A[i],i)]=result[(A[j]-A[i],j)]+1
#                    if result[(A[j]-A[i],i)]>maxv:
#                        maxv=result[(A[j]-A[i],i)]
#        return maxv
        
        d = {}
        maxv = 2
        for i in range(1,len(A)): #每轮变化的是末项（索引） #以后轮变为首项
            for j in range(i):
                if (j, A[j]-A[i]) not in d.keys(): #数学定义，一个等差数列的关键在于 首项（索引） 和 公差
                    d[(i, A[j]-A[i])] = 2
                else:
                    d[(i, A[j]-A[i])] = d[(j, A[j]-A[i])] + 1
                    if d[(i, A[j]-A[i])] > maxv:
                        maxv = d[(i, A[j]-A[i])]
#                print(d)
        return maxv
                
#        d = {}
#        maxv = 2
#        for i in range(1,len(A)):
#            for j in range(i):
#                try:
#                    d[(i, A[j]-A[i])] = d[(j, A[j]-A[i])] + 1
#                    maxv = max(maxv, d[(i, A[j]-A[i])])
#                except:
#                    d[(i, A[j]-A[i])] = 2
#        return maxv
        
solu = Solution()
A = [3,6,9,12]
A = [9,4,7,2,10]
A = [10, 3, 6, 9, 7, 1]
print(solu.longestArithSeqLength(A))