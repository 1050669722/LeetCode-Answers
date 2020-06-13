# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:12:54 2019

@author: Administrator
"""

class Solution:
    def sortArrayByParity(self, A: list) -> list:
#        temp1, temp2 = [], []
#        for k in A:
#            if k%2 == 0:
#                temp1.append(k)
#            else:
#                temp2.append(k)
#        return temp1 + temp2
        
#        k = 0
#        for _ in range(len(A)):
#            if A[k]%2 != 0:
##                print(-1)
#                A.append(A[k])
##                print(A)
#                del A[k]
##                print(A)
#            else:
#                k += 1
#        return A
        
#        p = 0
#        while p<len(A):
#            if A[p]%2 != 0:
#                A.append(A[p])
#                del A[p]
        
#        length = len(A)
#        for k in range(length):
#            if A[k]%2 == 0:
#                A.append(A[k])
##                print(A)
#        for k in range(length):
#            if A[k]%2 != 0:
#                A.append(A[k])
##                print(A)
#        return A[length:]
        
#        if len(A) <= 1:
#            return A
#        p, q = 0, 1
#        while p<len(A) and q < len(A):
#            if A[q]%2 != 0:
#                q += 1
#            if A[p]%2 == 0:
#                p += 1
        
        p, q = 0, len(A)-1
        while p<q:
#            print(p,q)
            while A[p]%2 == 0 and p<q:#
#                print(-1)
                p += 1
            while A[q]%2 != 0 and p<q:#
                q -= 1
#            if p<q:
            A[p], A[q] = A[q], A[p]
        return A
        
solu = Solution()
A = [3,1,2,4]
#A = [0,1,2]
#A = [0, 2]
print(solu.sortArrayByParity(A))